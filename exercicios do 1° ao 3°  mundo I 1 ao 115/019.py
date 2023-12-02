#------------- como eu fiz----------------

# Exercício Python 19: Um professor quer sortear um dos seus 
# quatro alunos para apagar o quadro. Faça um programa que 
# ajude ele, lendo o nome dos alunos e escrevendo na tela 
# o nome do escolhido.

import random
h = input('digite o nome dos alunos: \n1:')
h1 = input('2:')
h2 = input('3:')
h3 = input('4:')
h4 = (h,h1,h2,h3) #[usar esse nodo de [] todos dentro sera sorteados]
h5 = random.choice(h4)
print('O aluno esconhido foi o {}'.format(h5))

#-------------como o professor fez----------------

from random import choice

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
h4 = str(input('quarto aluno'))
lista = [h1,h2,h3,h4]
escolhido = choice(lista)
print('O valuno escolhidofoi {} '.format(escolhido))

