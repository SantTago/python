#-------------- como eu fiz --------------------------

# Exercício Python 040: Crie um programa que leia duas 
# notas de um aluno e calcule sua média, mostrando uma 
# mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

import time
h = float(input('primeira nota: '))
h1 = float(input('segunda nota: '))
h2 = (h + h1) / 2
print('\033[32mANALIZANDO\033[36m................................')
time.sleep(2)
print('SUA NOTA É {}'.format(h2))
if h2 <= 5.0:
    print('\033[31mREPROVADO')
    print('\033[31mESTUDE BASTANTE!!!')
elif h2 <= 6.9:
    print('\033[36mRECUPERAÇÃO')
    print('\033[31mESTUDE MAIS!!!')
elif h2 >= 7:
    print('\033[32mAPROVADO')
    print('\033[32mPARABENS!!!')
print('-='*20)

#-------------- como o professor fez --------------------------

nota1 = float(input('DIGITE A PRIMEIRA NOTA'))
nota2 = float(input('DIGITE A SEGUNDA NOTA '))
media = (nota1 + nota2) / 2
print('TIRANDO {:.1f} E {:.1f},A MEDIA DO ALUNO E {:.1f}'.format(nota1, nota2, media))
if 7 > media >=5:
    print('O ALUNO ESTAR DE RECUPERAÇAO')
elif media < 5:
    print('O ALUNO ESTAR REPROVADO')
elif media >= 7:
    print('APROVADO!!!!')

