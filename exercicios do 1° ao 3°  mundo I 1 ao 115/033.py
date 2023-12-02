# -------------- como eu fiz --------------------------

# Exercício Python 33: Faça um programa que leia três 
# números e mostre qual é o maior e qual é o menor.

h = int(input('Digite um numero com 3 DIGITOS: '))
h1 = str(h)
h2 = h1[0]
h3 = h1[1]
h4 = h1[2]
h5 = min(h2, h3, h4)  # min para chamar o menor valor
h6 = max(h2, h3, h4)  # max para chamar o maior valor
print('1° : {} '.format(h1[0]))
print('2° : {}'.format(h1[1]))
print('3° : {} '.format(h1[2]))
print('O maior valor e {}'.format(h6))
print('O menor valor e {}'.format(h5))

# -------------- como o professor fez  --------------------------

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Twecwiro valor:'))
# VERIFICANDO....
menor = a
if a > b and b < c:
    menor = b
if c < a and c < b:
    menor = c
# VERIFICANDO.....
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor e {} '.format(maior))
print('O menor valor e {} '.format(menor))
