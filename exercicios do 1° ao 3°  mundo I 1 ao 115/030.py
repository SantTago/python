#-------------- como eu fiz --------------------------

# Exercício Python 30: Crie um programa que leia um número 
# inteiro e mostre na tela se ele é PAR ou ÍMPAR.


h = int(input('Digite um numero:'))
print('O numero que voce escolheu é')
if (h%2)==0:  #  % 2 para que ele retone 0  para impar e 1 para par
    print('Par') # se ele for 0 e Par
else:
    print('impar') # se ele for 1 e Impar

#-------------- como o professor fez  --------------------------


numero = int(input('Digite um numero qual quer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} e PAR'.format(resultado))
else:
    print('O numero {} e IMPAR'.format(resultado))

