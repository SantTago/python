#---------------- COMO EU FIZ --------------------

import random
from time import sleep
c = 0
a = 1
h = 0
novo = int(input('''
    =====VAMOS JOGAR=====
ESCOLHA UM NUMERO ENTRE 0 A 10: '''))
print('COMPUTADOR PENSANDO..........................')
sleep(1)
computador = random.randint(0, 10)
print('computador: {} | JOGADOR {}'.format(computador, novo))
print('\033[36m==============================================\033[m')
while novo != h:
    h = random.randint(0, 10)
    a += 1
    novo = int(input('\033[31mTENTE NOVAMENTE!!! \033[m\nESCOLHA UM NUMERO ENTRE 1 A 10:'))
    print('\033[34mANALIZANDO\033[33m..................................\033[m')
    sleep(1)
    print('\033[33mcomputador: {} \033[m| \033[34mJOGADOR {}\033[m'.format(h, novo))
    print('\033[36m==============================================\033[m')
print('\033[32mPARABENS VOCE ACERTOU!\033[m')
print('voce tentou {} vezes'.format(a))
print('FIM DE JOGO!')
print('\033[36m==============================================\033[m''')


#============= como o professor fez ===============

from random import randint
computador =  randint(0, 10)
print('SOU SEU COMPUTADOR ACABEI DE PENSAR EM UM NUMRO ENTRE 0 A 10')
print('SERA QUE VC CONSEGUI ADIVINHAR QUAL FOI?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('QUAL O SEU PALPITE?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS....TENTE MAIS UMA VEZ')
        elif jogador > computador:
            print('MENOS....TENTE MAIS UMA VEZ')
print('ACERTOU! VOCE TEVE  {} PALPITES'.format(palpites))












