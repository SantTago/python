#------------- nao consegui fazer -- Resultado do professor----------------

# Exercício Python 17: Faça um programa que leia o 
# comprimento do cateto oposto e do cateto adjacente de 
# um triângulo retângulo. Calcule e mostre o comprimento 
# da hipotenusa.

import math

h = float(input('Comprimento do cateto oposto: '))
h1 = float(input('Comprimento cateto oposto: '))
h2 = math.hypot(h, h1)
print('A ipotenusa vai medir {:.2f}'.format(h2))



h = float(input('Comprimento do cateto oposto: '))
h1 = float(input('Comprimento cateto oposto: '))
h2 = (h ** 2 + h1 ** 2) ** (1/2)
print('A ipotenusa vai medir {:.2f}'.format(h2))
