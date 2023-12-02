"""Utilitários para obter uma senha e/ou o nome de usuário atual.

getpass(prompt[, stream]) - Solicita uma senha, com o eco desativado.
getuser() - Obtém o nome de usuário do ambiente ou banco de dados de senhas.

GetPassWarning - Este UserWarning é emitido quando getpass() não pode impedir
                 eco do conteúdo da senha durante a leitura.

No Windows, o módulo msvcrt será usado.

"""

# Autores: Piers Lauder (original)
# Guido van Rossum (suporte e limpeza do Windows)
# Gregory P. Smith (suporte tty & GetPassWarning)

import contextlib
import io
import os
import sys
import warnings

__all__ = ["getpass","getuser","GetPassWarning"]


class GetPassWarning(UserWarning): pass


def unix_getpass(prompt='Password: ', stream=None):
    """Solicita uma senha, com o eco desligado.

    Argumentos:
      prompt: Escrito no fluxo para solicitar a entrada. Senha padrão: '
      stream: Um objeto de arquivo gravável para exibir o prompt. O padrão é
              o tty. Se nenhum tty estiver disponível, o padrão será sys.stderr.
    Retorna:
      A entrada seKr3t.
    Levanta:
      EOFError: Se nossa entrada tty ou stdin foi fechada.
      GetPassWarning: Quando não conseguimos desligar o eco na entrada.

    Sempre restaura as configurações do terminal antes de retornar.
    """
    passwd = None
    with contextlib.ExitStack() as stack:
        try:
            # Sempre tente ler e escrever diretamente no tty primeiro.
            fd = os.open('/dev/tty', os.O_RDWR|os.O_NOCTTY)
            tty = io.FileIO(fd, 'w+')
            stack.enter_context(tty)
            input = io.TextIOWrapper(tty)
            stack.enter_context(input)
            if not stream:
                stream = input
        except OSError:
            # Se isso falhar, veja se stdin pode ser controlado.
            stack.close()
            try:
                fd = sys.stdin.fileno()
            except (AttributeError, ValueError):
                fd = None
                passwd = fallback_getpass(prompt, stream)
            input = sys.stdin
            if not stream:
                stream = sys.stderr

        if fd is not None:
            try:
                old = termios.tcgetattr(fd)     # a copy to save
                new = old[:]
                new[3] &= ~termios.ECHO  # 3 == 'lflags'
                tcsetattr_flags = termios.TCSAFLUSH
                if hasattr(termios, 'TCSASOFT'):
                    tcsetattr_flags |= termios.TCSASOFT
                try:
                    termios.tcsetattr(fd, tcsetattr_flags, new)
                    passwd = _raw_input(prompt, stream, input=input)
                finally:
                    termios.tcsetattr(fd, tcsetattr_flags, old)
                    stream.flush()  # issue7208
            except termios.error:
                if passwd is not None:
                    # _raw_input com sucesso. O tcsetattr final falhou. Aumentar novamente
                    # em vez de deixar o terminal em um estado desconhecido.
                    raise
                # Não podemos controlar o tty ou stdin. Desista e use IO normal.
                # fallback_getpass() gera um aviso apropriado.
                if stream is not input:
                    # limpe objetos de arquivo não utilizados antes de bloquear
                    stack.close()
                passwd = fallback_getpass(prompt, stream)

        stream.write('\n')
        return passwd


def win_getpass(prompt='Password: ', stream=None):
    """Prompt for password with echo off, using Windows getwch()."""
    if sys.stdin is not sys.__stdin__:
        return fallback_getpass(prompt, stream)

    for c in prompt:
        msvcrt.putwch(c)
    pw = ""
    while 1:
        c = msvcrt.getwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            pw = pw[:-1]
        else:
            pw = pw + c
    msvcrt.putwch('\r')
    msvcrt.putwch('\n')
    return pw


def fallback_getpass(prompt='Password: ', stream=None):
    warnings.warn("Can not control echo on the terminal.", GetPassWarning,
                  stacklevel=2)
    if not stream:
        stream = sys.stderr
    print("Warning: Password input may be echoed.", file=stream)
    return _raw_input(prompt, stream)


def _raw_input(prompt="", stream=None, input=None):
    # Isso não salva a string no histórico da linha de leitura GNU.
    if not stream:
        stream = sys.stderr
    if not input:
        input = sys.stdin
    prompt = str(prompt)
    if prompt:
        try:
            stream.write(prompt)
        except UnicodeEncodeError:
            # Use o manipulador de erros de substituição para imprimir o máximo possível.
            prompt = prompt.encode(stream.encoding, 'replace')
            prompt = prompt.decode(stream.encoding)
            stream.write(prompt)
        stream.flush()
    # OBSERVAÇÃO: a API Python C chama flocfile() (e unlock) durante readline.
    line = input.readline()
    if not line:
        raise EOFError
    if line[-1] == '\n':
        line = line[:-1]
    return line


def getuser():
    """
    Obtenha o nome de usuário do banco de dados de ambiente ou senha.

    Primeiro tente várias variáveis ​​de ambiente, então a senha
    base de dados. Isso funciona no Windows, desde que USERNAME esteja definido.

    """
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        user = os.environ.get(name)
        if user:
            return user

    # Se isso falhar, a exceção irá "explicar" porque
    import pwd
    return pwd.getpwuid(os.getuid())[0]

# Vincule o nome getpass à função apropriada
try:
    import termios
    # é possível que haja termios incompatíveis do
    # McMillan Installer, verifique se temos um termios compatível com UNIX
    termios.tcgetattr, termios.tcsetattr
except (ImportError, AttributeError):
    try:
        import msvcrt
    except ImportError:
        getpass = fallback_getpass
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass
