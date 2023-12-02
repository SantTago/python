# Exercício Python 36: Escreva um programa para aprovar o 
# empréstimo bancário para a compra de uma casa. Pergunte o 
# valor da casa, o salário do comprador e em quantos anos ele 
# vai pagar. A prestação mensal não pode exceder 30% do salário 
# ou então o empréstimo será negado.


nome = str(input('Digite seu nome: '))
if nome == 'Tiago':
    print('que nome bonito {}'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Matheus':
    print('Seu nome e bem popular aqui no BRASIL')
elif nome == 'Ana' or nome == 'Bruna':
    print('Que belo nome feminino!')
else:
    print('Seu nome e bem comum!')
print('Seja bem vindo {}!'.format(nome))

#-------------- como eu fiz --------------------------
import time
valor = float(input('Quanto custasua  casa? '))
salario = float(input('Qunato e seu salario? '))
m = int(input('E  quantos anos vc quer pagar? '))
print('\033[34mANALIZANDO\033[m\033[33m................\033[m')
time.sleep(3)
h1 = salario*30
h2  = h1/100
c = valor/(m*12)
if c <= h2:
    print('Seu financiamento foi \033[34m APROVADO!!\033[m')
else:
    print('seu financiamento foi \033[31m REPROVADO!!\033[m')
print('='*30)




#-------------- como o professor fez  --------------------------

casa = float(input('QUANTO CUSTA A CASA R$: '))
SALARIO = float(input('QUANTO E SEU SALARIO R$: '))
anos = int(input('EM QUANTOS ANOS VC QUER PAGAR? '))
prestaçao = casa/ (anos*12)
print('PARA PAGAR UM CASA DE R$: {:.2f} EM {} ANOS'.format(casa, anos),end = '')
print('A PRESTAÇAO SERA {}'.format(prestaçao))
minimo = salario * 30 / 100
if prestaçao <= minimo:
    print('EMPRESTIMO PODE SER CONCEDITO')
else:
    print('EMPRESTIMO NEGADO!!')
