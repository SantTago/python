#----------------------Como eu fiz---------------------------

# Exercício Python 43: Desenvolva uma lógica que leia o peso 
# e a altura de uma pessoa, calcule seu Índice de Massa Corporal 
# (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida


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


