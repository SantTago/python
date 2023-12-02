#-------------- como eu fiz --------------------------

# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = str(input('digite seu nome completo: '))
print(nome.upper()) #maisculas
print(nome.lower()) #minisculas
nome1 = nome.split() #colocando em grupos
nome2 = "".join(nome1) #reagrupando as palavras
print(len(nome2))  #quantas letras tem no nome
print(len(nome1[0])) #quabtas letras tem a primeiro nome

#-------------- como o professor fez  --------------------------

nome = str(input('Digite seu nome completo: ')).strip()
print('analizando seu nome....')
print('Seu nome em maiusculas: {} '.format(nome.upper()))
print('Seu nome em minusculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} Letras '.format(nome.find(' ')))
