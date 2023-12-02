#-------------- como eu fiz --------------------------

# Exercício Python 23: Faça um programa que leia um número 
# de 0 a 9999 e mostre na tela cada um dos dígitos separados.



h = input('digite um numero: ')
print('unidade: {} '.format(h[3]))
print('dezena: {}'.format(h[2]))
print('centena: {}'.format(h[1]))
print('milhar: {}'.format(h[0]))


#-------------- como o professor fez  --------------------------

num = int(input('Digite um numero: '))
n =str(num)
print('Analizando o numero: {}'.format(num))
print('Unidade: {} '.format(h[3]))
print('Dezena: {} '.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {} '.format(n[0]))


num =int(input('Digite um numero: '))
h = num // 1 % 10
h1 = num // 10 % 10
h2 = num // 100 % 10
h3 = num // 1000 % 10
print('Analizando o numero: {}'.format(num))
print('Unidade: {} '.format(h))
print('Dezena: {} '.format(h1))
print('Centena: {}'.format(h2))
print('Milhar: {} '.format(h3))
