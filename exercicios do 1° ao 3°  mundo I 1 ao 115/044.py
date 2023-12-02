#----------------------Como eu fiz---------------------------

# Exercício Python 44: Elabore um programa que calcule o 
# valor a ser pago por um produto, considerando o seu preço 
# normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros



import math
peso = float(input('DIGITE SEU PESO EM KG: '))
altura = float(input('DIGITE SUA ALTURA: '))
IMC = float(peso/(altura*altura))
print('O SEU IMC E {:.1f} '.format(IMC))
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC < 25:
    print('PESO IDEIAL')
elif IMC < 30:
    print('SOBREPESO')
elif IMC < 40:
    print('OBSIDADE')
elif IMC < 100:
    print('OBESIDADE MORBTA')

# ----------------------Como O PROFESSOR FEZ ---------------------------
peso = float(input('DIGITE SEU PESO EM KG: '))
altura = float(input('DIGITE SUA ALTURA: '))
IMC = float(peso/(altura*altura))
print('O SEU IMC E {:.1f} '.format(IMC))
if IMC < 18.5:
    print('VOCE ESTAR ABAIXO DO PESO NORMAL')
elif 18.5 <= IMC < 25:
    print('PARABENS SEU PESO E IDEIAL')
elif 25 <= IMC < 30:
    print('VOCE ESTAR EM SOBREPESO')
elif 30 <= IMC < 40:
    print('CUIDADO OBSIDADE')
elif 40 <= IMC < 100:
    print('PROCURE UM MEDICO!!!! OBESIDADE MORBTA')


#=================== como eu fiz ==================

print('''==========LOJAS TIAGO======''')
h = float(input('QUAL O VALOR DA SUAS COMPRAS R$:'))
print('''
[ 1 ] A VISTA OU CHEQUE C/ 10%
[ 2 ] A VISTA NO CARTAO DE CREDITO C/ 5%
[ 3 ] 2X NO CARTAO DE CREDITO
[ 4 ] 3x no cartado de credito c/ 20% de acrecimo''')
h1 = int(input('QUAL E A OPÇAO? '))
h2 = int(input('EM QUATAS VEZES VC QUER PARCELAR ?'))
if h1 == 1:
    print('A VISTA OU CHEQUE C/ 10% DE DESCONTO R$: {}'.format(h-(h*10)/100))
elif h1 == 2:
    print('A VISTA NO CARTAO DE CREDITO C/ 5% DE DESCONTO R$: {}'.format(h - (h * 5) / 100))
elif h1 == 3:
    print('2X NO CARTAO DE CREDITO VALOR NORMAL {}'.format(h))
elif h1 == 4:
    print('3x ou mais no cartado de credito c/ 20% de acrecimo VALOR FINAL R$: {}'.format(h + (h * 20) / 100))










