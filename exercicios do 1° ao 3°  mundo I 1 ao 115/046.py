#============= COMO EU FIZ =================

# Exercício Python 46: Faça um programa que mostre na tela uma 
# contagem regressiva para o estouro de fogos de artifício, indo 
# de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
h1 = int(input('NUMERO PARA VER SUA TABOADA: '))
for h in range(0, 11):
  
    h2 = h1*h
    print('\033[36m{} X \033[34m{} = \033[31m{} '.format( h1, h, h2))
print('-------------FIM-----------')


#============= COMO O PROFESSOR FEZ =================
