#========== COMO EU FIZ =================
h1 = 0
h2 = 0
h3 = 1
h4 = 0
h7 = 0
h = 0
p = 0
nu = 0
for num in range(1,3):
    h1 = int(input('{}° VALOR :'.format(num)))
    h += h1
    h3 = h3 * h1
print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do Programa
''')
while h2 != 5:
    h2 = int(input('ESCOLHA UMA OPÇAO PARA PROCEGUIR: '))
    if h2 == 1:
        print(' A SOMA EMTRE ELES DA {}'.format(h))
    elif h2 == 2:
        print('A MULTIPLICAÇAO DA {}'.format(h3))
    elif h2 == 3:
        print('O MAIOR NUMERO E {}'.format(maior))
    elif h2 == 4:
        h += h1
        h3 = h3 * h1
        print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do Programa
''')
        for l in range(1,3):
            h7 = int(input('{}° VALOR :'.format(l)))
while h7 != 5:
    if h2 == 1:
            print(' A SOMA EMTRE ELES DA {}'.format(h))
    elif h2 == 2:
            print('A MULTIPLICAÇAO DA {}'.format(h3))
    elif h2 == 3:
            print('O MAIOR NUMERO E {}'.format(maior))

#========== COMO O PROFESOR FEZ =================

n1 = int(input('PRIMEIRO NUMERO: '))
n2 = int(input('SEGUNDO NUMERO: '))
opçao = 0
while opçao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opçao = int(input('QUAL  E SUA OPÇAO? '))
    if opçao  == 1:
        soma = n1 + n2
        print(' A SOMA ENTRE {} + {} = {}'.format(n1, n2,soma ))
    elif opçao == 2:
        produto = n1 * n2
        print('A MULTIPLICAÇAO ENTRE {} X {} = {}'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior  = n1
        print('O MAIOR NUMERO Emtre {} e {} o maior numero e {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('INFORME O NUMERO NOVAMENTE')
        n1 = int(input('PRIMEIRO NUMERO: '))
        n2 = int(input('SEGUNDO NUMERO: '))
    else:
        print('OPÇAO INVALIDA! TENTE NOVAMENTE!1')
    print('-='*20)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')


























