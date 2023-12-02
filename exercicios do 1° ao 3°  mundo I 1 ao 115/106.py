#========== COMO EU FIZ =====================

def ajuda():
    
    while True:
        print('\33[30;42m~' * 40)
        print('  SISTEMA DE AJUDA PyHelp')
        print('~' * 40)
        resp = str(input("Função ou Biblioteca: "))
        print('\33[30;44m~' * 40)
        
        print(f'  \033[mAcessando o Manual do comando {resp}')
        
        
        
        print('\33[30;44~\033[7;30;41' * 40)

        print(f'{help(resp)}')
        

ajuda()

#============= COMO O PROFESOR FEZ =====================

from time import sleep
c = ('\033[m',        # - 0 sem cores  
     '\033[0;30;41m', # - 1 vermelho
     '\033[0;30;42m', # - 2 vermelho
     '\033[0;30;43m', # - 3 amarelo
     '\033[0;30;44m', # - 4 azul
     '\033[0;30;45m', # - 5 roxo
     '\033[0;30;46m'  # - 6 branco
    );  # NAO ESQUECER DOS ; | # com essa dupla o valor 0 e sem cor e 1 vale a cor vermelha 

def ajuda(con): # com recebe a variavel do nome da dunçao que ta sendo pesquisada 
    print(c[6], end='')
    print(f'Acessando o manual do comando \'{con}\'', 4)
    sleep(2)
    help(con)
    print(c[0],end='')
    
    

def titulo(msg, cor=0): # recebe tudo que tiver em titulo("  ")
    print(c[cor],end='') # variavel cor=0
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0],end='')
    
    
    
#programa principal
comando = ' ' # comando começa vazio para receber o valor de comnado \ comando = str(input......
while True:
    
    titulo('Sistema de ajuda Pyhelp', 2) # str de titulo vai para def titulo que vai para msg
    comando = str(input(" Função ou biblioteca: "))
    if comando.upper() == 'FIM': # .upper para deixar tudo maiusculo
        break
    else:
        ajuda(comando)
    

titulo("Ate logo!", 1)  # toda comando titulo(" ") subtitui pelo msg