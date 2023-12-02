#============= COMO EU FIZ =================

# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número 
# que o usuário escolher, só que agora utilizando um laço for.

from time import sleep
h1 = int(input('NUMERO PARA VER SUA TABOADA: '))
for h in range(0, 11):
    sleep(1)
    h2 = h1*h
    print('\033[36m{} X \033[34m{} = \033[31m{} '.format( h1, h, h2))
print('-------------FIM-----------')


#============= COMO O PROFESSOR FEZ =================v