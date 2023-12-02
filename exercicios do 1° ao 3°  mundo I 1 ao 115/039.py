#-------------- como eu fiz -------------------------

# Exercício Python 39: Faça um programa que leia o ano de nascimento 
# de um jovem e informe, de acordo com a sua idade, se ele ainda vai 
# se alistar ao serviço militar, se é a hora exata de se alistar ou se 
# já passou do tempo do alistamento. Seu programa também deverá mostrar 
# o tempo que falta ou que passou do prazo.

import time

h = int(input('Qual e sua data nascimento'))
h1 = h -2023
print('\033[36mCAREGANDO\033[34m........................')
print(h1)
h2 = [-10, -11, -12, -13, -14, -15]
h3 = [-16, -17]
h4 = [-18]
time.sleep(2)
if h1 >= -15:
    print('\033[36mAINDA NAO TA NA HORA PARA SE ALISTAR!!')
elif h1 in h3:
    print('\033[35mFIQUE ATENTO QUE FALTA POOUO PARA SE ALISTAR')
elif h1 in h4:
    print('\033[34mPROCURE UMA BASE PARA SE APRESENTAR AO SERVIÇO!!!')



#-------------- como O PROFESSOR FEZ -------------------------

from datetime import date #datetime data Hora
atual = date.today().year # data . hoje(). ano
nasc = int(input('ANO DE NASCIMENTO: '))
idade = atual -nasc
print('QUEM NASCEU EM {} TEM {} ANOS, EM {}'.format(nasc, idade, atual))
if idade == 18:
    print('VOCE TEM QUE SE ALISTAR IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('AINDA FALTA {} ANOS PARA SE ALISTAR'.format(saldo))
    print('SEU ALISTAMENTO SERA EM {} ANO'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('VOCE JA DEVERIA TER SE ALISTADO A {} ANOS'.format(saldo))




