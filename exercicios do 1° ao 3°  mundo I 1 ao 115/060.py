#========== COMO EU FIZ =================
print('''
========== Calculadora fatorial ==========
''')
c = 1
n = int(input('DIGITE UM UM NUMERO: '))
for l in range(n, 1, -1):
    c *= l
print(c)


#========== COMO O PROFESOR FEZ =================

from math import factorial
n = int(input('DIGITE UM NUERO PARA VER SEU FATORIAL;'))
f = factorial(n)
print('O FATORIAL DE {} E {}'.format(n, f))

#==========#==========#==========#==========#==========#==========

n = int(input('DIGITE UM NUERO PARA VER SEU FATORIAL;'))
c = n
f = 1
print('CALCULANDO {}!'.format(n), end='')
while c > 0:
    print('faorial de {} x'.format(c), end=' ')
    print('x' if c < 1 else '=', end=' ')
    c = -1
    f *= c
print(f)

