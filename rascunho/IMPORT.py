import math
num = int(input('digite um valor:'))
raiz = math.sqrt(num)
print('A raiz quadrada de {} e {} '.format(num,math.trunc(raiz)))

#-------------------- rasculo das aulas --------------------

from math import sqrt, trunc
num = int(input('Digite um valor: '))
raiz = sqrt(num)
print('A raiz quadrada de {} e {}'.format(num,trunc(raiz)))

import random  #numero aleatorios
num = random.random()
print(num)

import random
num = random.randint(1, 100)  #randint numeros aleatorios entre a , bc
print(num)

import emoji
print(emoji.emojize('La Mundo :thinking_face:'))