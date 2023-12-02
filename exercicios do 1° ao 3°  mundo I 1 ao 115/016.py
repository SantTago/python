#--------------como eu fiz-----------------------

# Exercício Python 16: Crie um programa que leia um 
# número Real qualquer pelo teclado e mostre na tela a 
# sua porção Inteira.

from math import trunc
h = float(input('Digite um valor Real: '))
h1 = trunc(h)
print('o valor real de  {:.3f}'.format(h))
print('O numero {} tem a parte inteira {} '.format(h,h1))

#-------------como o professor fez-------------------------

import math
num = float(input('Digite um valor: '))
print('O valor digitado e {} e sua parte inteira e {}'.format(num,math.trunc(num)))

num = float(input('Digite um valor: '))
print('O valor digitado e {} e sua parte inteira e {}'.format(num,int(num)))
