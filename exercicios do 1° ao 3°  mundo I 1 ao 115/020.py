#------------- como eu fiz----------------

# Exercício Python 20: O mesmo professor do 
# desafio 19 quer sortear a ordem de apresentação 
# de trabalhos dos alunos. Faça um programa que leia 
# o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

h = str(input('Primeiro aluno: '))
h1 = str(input('segundo aluno: '))
h2 = str(input('terceiro aluno: '))
h3 = str(input('quarto aluno: '))
h4 = [h,h1,h2,h3]
shuffle(h4)
print ('A orden de apresentaçao sera')
print(h4)

#------------- como o professor fez----------------

from random import shuffle

n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentaçao sera')
print(lista)



