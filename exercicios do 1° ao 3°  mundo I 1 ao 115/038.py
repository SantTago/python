#-------------- como eu fiz --------------------------

# Exercício Python 038: Escreva um programa que leia dois números 
# inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

h = int(input('digie um Numero:'))
h2 = int(input('digte outro numero:'))
if h > h2:
    print('\033[33mo primeiro valor {} e maior que {}'.format(h, h2))
elif h < h2:
    print('\033[32mO segundo valor {} e maior '.format(h2))
elif h == h2:
    print('\033[36mnao exie valor maior os dois valores sao iguais')



#-------------- como O PROFESSOR FEZ --------------------------

n1 = int(input('DIGITE UM VALOR: '))
n2 = int(input('DIGITE O SEGUNDO VALOR: '))
if n1 > n2:
    print('O PRIMEIRO VALOR E MAIOR')
elif n2 > n1:
    print('O SEGUNDO VALOR E MAIOR')
else:
    print('OS DOIS VALORES E IGUAIS')
