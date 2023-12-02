#------------------como O PROFESSOR FEZ-------------------
tot = 0
num = int(input('DIGITE UM NUMERO: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mo numero {} foi divizivel {} vezes'.format(num, tot))
if tot == 2:
    print('E POR ISSO ELE E PRIMO')
else:
    print('E POR ISSO ELE NAO E PRIMO')

# amarelo e divisivel e vermelho nao e !