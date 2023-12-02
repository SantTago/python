
#------------------COOMO eu fiz --------------------------
ida = 0
for h in range(1):
    nome = str(input('\033[32m {}° QUANL E SEU NOME?  '.format(h))).upper()
    idade = int(input(' {}° digite sua idade: '.format(h)))
    print('''
QUAL SEU SEXO? =====================>
    \n\033[33m[ 0 ] MASCOLINO   \n\033[35m[ 1 ] FEMININO
''')
    sexo = int(input('0 / 1 ? '))
    print('\033[34m========================== ')
    ida += idade
    h2 = ida /3
print('A MEDIA DE IDADE DO GRUPO E DE {}'.format(h2))
if sexo == 0:
    print('\033[32mHOMEM')
elif sexo == 1:
    print('\033[33mMULHER')
else:
    print('\033[36mOPÇAO INVALIDA')
# consegui ate aqui

#------------------COOMO O PROFESSOR FEZ --------------------------

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('----------{}° Pessoa ------'.format(p))
    nome = str(input('Nome: ')) .strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ M / F ]')).strip()
    somaidade += idade
    if p == 1 and sexo in "Mn":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade /4
print('A MEDIA DO GRUPO E {}'.format(mediaidade))
print('O HOMEM MAIS VELHO TEM {} E O NOME DELE E {}'.format(maioridadehomem, nomevelho))
print('AO TODO SAO {] MULHERES COM MENOS DE 20 ANOS'.format(totmulher20))


























