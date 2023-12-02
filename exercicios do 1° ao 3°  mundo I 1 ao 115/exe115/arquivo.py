from lib import *



def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # o nome recebe o nome do arquivo.txt e o 'rt' e para fazer a leitura do aquivo
        a.close() # close para fechar 
    except FileNotFoundError:  # FileNotFoundError se o arquivo nao for encontrado
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt ->  escreva um aquivo de texto o + e para criar um arquivo caso ele nao existra
        a.close() # para fechar 
    except:
        Print('Houve um ERRO na criaçao do arquivo')
    else:
        print(f'Arquivo {nome} Criado com sucesso!!')
    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # 'rt' para leitura de TXT
    except:
        print('ERRO ao ler o arquivo!!')
    else:
        cabeçario('PESSOAS CADASTRADAS')
        for linha in a:
            dado =linha.split(';') # split para soltar todas as paavras 
            dado[1] = dado[1].replace('\n', ' ') # .replace para trocar o \n por nada
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close # caso tudo ocorra ok ou nao ele vai finalizar o programa
        
def cadastrar(arq, nome = 'Desaconhecido', idade = 0):
    try:
        a = open(arq, 'at') # a -> de append | t -> texto
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')# write para escrever dentro do arquivo txt
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(linha())
            print(f"Novo Cadastro de {nome} adiconado")
            a.close # para fechar