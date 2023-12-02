#------------- nao consegui fazer -- Resultado do professor----------------

# Exercício Python 18: Faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
 
import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo e {} e o  seno e {:.2f}  '.format(angulo, seno))
conceno = math.cos(math.radians(angulo))
print('O angulo e {} Conceno e {:.2f} '.format(angulo, conceno))
tangente = math.tan(math.radians(angulo))
print('O angulo e {} A tangente e {:.2f} '.format(angulo, tangente))


from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
print('O angulo e {} e o  seno e {:.2f}  '.format(angulo, seno))
conceno = cos(radians(angulo))
print('O angulo e {} Conceno e {:.2f} '.format(angulo, conceno))
tangente = tan(radians(angulo))
print('O angulo e {} A tangente e {:.2f} '.format(angulo, tangente))


