#--------------- como eu fiz -----------------------

# Exercício Python 28: Escreva um programa que faça o computador 
# “pensar” em um número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador. O 
# programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice

print('\033[35m----O JOGO VAI COMEÇAR!!----\033[m')

h = int(input('\033[31mEscolha um numero entre 0 e 5 :\033[m'))
lista = [1,2,3,4,5]
h1 = choice(lista)
print('\033[31mVocê escolheu o N° {} \033[m'.format(h))
print('\033[35mEscolhido pelo PC foi N° {} \033[m]'.format(h1))
if h == h1:
    print('\033[36mPARABÉNS VC VENCEU!!!!!!!!!!!\033[m')
else:
    print('\033[36mVOCE PERDEU!\033[m')

print('------------- FIM ------------')


#--------------- como o professor fez -----------------------

from random import randint
from time import sleep

computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5 tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em qual numero eu pensei? '))
print('PROCESSANDO.....')
sleep(3)
if computador == jogador:
    print('PARABÉNS VOCE CONSEGUIL ME VENCEU!!')
else:
    print('EU VENCI! Eu pensei no numero {} e voce no {}'.format(computador, jogador))
