#======================= como eu fiz ==============

# Exercício Python 041: A Confederação Nacional de Natação 
# precisa de um programa que leia o ano de nascimento de um 
# atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

import time
h = int(input('Digite sua data de nascimento:'))
h1 = h - 2023
print('sua idade e {} VEJA SUA CATEGORIA'.format(h1))
print('\033[32mANALIZANDO\033[35m...............')
time.sleep(2)
h2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
h3 = [-10, -11, -12, -13, -14]
h4 = [-15, -16, -17, -18, -19]
h5 = [-20]
if h1 in h2:
    print('Sua categoria e \033[36mMIRIM')
elif h1 in h3:
    print('Sua categoria e \033[35mINFANTIL')
elif h1 in h4:
    print('Sua categoria e \033[34mJUNIOR')
elif h1 in h5:
    print('Sua categoria e \033[33mSÊNIOR')
elif h1 <= -21:
    print('Sua categoria e \033[32mMASTER')

#======================= como o professor fez ==============

from datetime import date
atual = date.today().year
nascimento = int(input('ANO DE NASCIMENTO: '))
idade = atual - nascimento
print('O ATLETA EM {} ANOS'.format(idade))
if idade <= 9:
    print('CLASIFICAÇAOE E MIRIM')
elif idade <= 14:
    print('CLASIFICAÇAO E INFANTIL')
elif idade <= 19:
    print('CLASIFICAÇAO E JUNIOR')
elif idade <= 25:
    print('CLASSIFICAÇAO E SENIOR')
else:
    print('CLASSIFICAÇAO E MASTER')
