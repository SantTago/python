#-------------------- como eu fiz--------------------------

# Exercício Python 7: Desenvolva um programa que leia as duas 
# notas de um aluno, calcule e mostre a sua média.

h = float(input('Digite a primeira nota  nota do aluno: '))
h1 = float(input('Digite a segunda nota do aluno: '))
h2 = h + h1
print('a media entre o valor {} mais o valor {} da {}'.format(h, h1 ,(h2/2)))


#-------------------- como o professor fez--------------------------

h = float(input('Digite a primeira nota  nota do aluno: '))
h1 = float(input('Digite a segunda nota do aluno: '))
h2 = (h + h1) / 2
print('A media entre {} mais o valor {} e igual {} '.format(h, h1, h2))