#=========== como eu fiz ===============
h = '0'
h1 = 1
while h !='.':
    h1 = ['F', 'M']
    print('''
M - MASCOLINO
F - FEMININO 
''')
    h = str(input('[ M | F ] : ')).upper()
    if h == 'M':
        print('seja bem vindo!')
    elif h == 'F':
        print('seja vem vinda!')
    else:
        print('\033[31mDIGITE CORRETAMENTE\033[m')
#  NAO CONSEGUI FAZER CONTINUAR SE TIVER ERRADO
# TODAS A OPÇOES REPETE

#----------------- COMO O PROFESSOR FEZ --------------------------

sexo = str(input('DIGITE SEU SEXO [M/F] :  ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('DADOS INVALIDOS. POR FAVOR, INFORME SEU SEXO: ')).strip().upper()[0]
print('SEXO {} REGISTRADO COM SUCESSO!!'.format(sexo))



