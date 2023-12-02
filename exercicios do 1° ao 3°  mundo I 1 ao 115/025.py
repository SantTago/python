#-------------- como eu fiz --------------------------

# Exercício Python 25: Crie um programa que leia o 
# nome de uma pessoa e diga se ela tem “SILVA” no nome.

h = str(input('Digite seu nome completo: '))
h1 = h.title()
print('Silva' in h1)



#-------------- como o professor fez  --------------------------

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silval? {} '.format('SILVA' in nome.upper()))

