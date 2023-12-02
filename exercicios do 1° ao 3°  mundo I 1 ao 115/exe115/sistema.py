import lib
from arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq): # se nao exite o arquivo
    criarArquivo(arq) # caso nao tenha o arquivo ele vai criar com essa funçao
#lib.cabeçario("SISTEMA ARQUIVO VERSAO V1.0")

while True:
    respota = lib.menu(['Ver Pessoas Cadastradas', 'Cadastra nova Pessoas ','Sair do sistema'])
    if respota == 1:  # opçao de listar o conteudo de um arquivo txt
        lerArquivo(arq)
    
    elif respota == 2:
        lib.cabeçario('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        
        cadastrar(arq, nome, idade)
        
    elif respota == 3:
        lib.cabeçario('Saindo do programa....Ate logo!')
        break
    
    else:
        print('\033[31mERRO! Digite uma opçao valida!\033[m')
    sleep(1) 