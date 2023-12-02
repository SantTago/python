#-------------- como eu fiz --------------------------

# Exercício Python 27: Faça um programa que leia o nome 
# completo de uma pessoa, mostrando em seguida o primeiro e o 
# último nome separadamente.

h = str(input('digite seu nome completo: '))
n = h.upper()
h1 = n.split()
h2 = h1[0]
h3 = h1[3]
print('Primeiro: {}'.format(h2))
print('ultimo: {}'.format(h3))


#-------------- como o professor fez  --------------------------

h = str(input('digite seu nome completo: ')).strip()
nome = h.split()
print('Ola e um prazer em te conhecer seu nome tem ')
print('seu primeiro nome e {} '.format(nome[0]))
print('seu ultimo nome e {}'.format(nome[len(nome)-1]))