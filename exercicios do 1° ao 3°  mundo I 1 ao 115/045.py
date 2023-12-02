#=================  COMO EU FIZ ==============

#Exercício Python 45: Crie um programa que faça o 
# computador jogar Jokenpô com você.

from time import sleep
import random
print('''SUAS OPÇOES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
h = int(input('QUAL E A SUA JOGADA? '))
h2 = random.randint(0, 2)
print('JO')
sleep(2)
print('kEN')
sleep(1)
print('POW!!!!')
print('-='*20)
print('VOCE ESCOLHEU {} '.format(lista[h]))
print('O COMPUTADOER ESCOLHEU {}'.format(lista[h2]))
if h2 == 0:
    if h == 0:
        print('EMPAATE')
    elif h == 1:
        print('JOGADOR GANHOU')
    elif h == 2:
        print('COMPUTADOR  GANHOU')
    else:
        print('OPÇAO INVALIDA')
elif h2 == 1:
    if h == 0:
        print('COMPUTADOR GANHOU!!')
    elif h == 1:
        print('EMPATE!!')
    elif h == 2:
        print('JOGADOR GANHOU!!!!')
    else:
        print('OPÇAO INVALIDA!!')
elif h2 == 2:
    if h == 0:
        print('JOGADOR GANHOU!!')
    elif h == 1:
        print('COMPUTADOR GANHOU!!!')
    elif h == 2:
        print('EMPATE!!')






#=================  COMO O PROFESSOR FEZ ==============

from random import randint
item = ('PEDRA ', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''SUAS OPÇOES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESORA''')
jogador = int(input('QUAL E A SUA JOOGADA '))
print('='*25)
print('O COMUTADOR ESCOLHEU {}'.format(item[computador]))
print('O JOGADOR ESCOHEU {}'.format(item[jogador]))
print('='*25)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU!!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('JOGADA INVALIDA')

