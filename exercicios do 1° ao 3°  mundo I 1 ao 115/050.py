#------------------como eu fiz--------------------------

# Exercício Python 50: Desenvolva um programa que leia seis 
# números inteiros e mostre a soma apenas daqueles que forem 
# pares. Se o valor digitado for ímpar, desconsidere-o.

h2 = 0
for h in range(1, 7):
    num = int(input('\033[32mDIGITE UM NUMERO: '))
    h1 = (num % 2) == 1
    h2 += num - h1
    if h1 == 0:
        print('\033[36mPAR')
    elif h1 == 1:
        print('\033[35mIMPAR')
    print('''=======================================''')
print('\033[34mA SOMA DE TODOS OS PAR DA \033[32m{} '.format(h2))


#------------------como O PROFESSOR FEZ-------------------

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('DIGIEUM NUMERO: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('VOCE INFORMOU {} NUMEROS PARES E A SOMA DA {}'.format(cont, soma))


