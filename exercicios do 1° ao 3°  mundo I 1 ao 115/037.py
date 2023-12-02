#================ nao consegui fazer como o professor fez ============

# Exercício Python 37: Escreva um programa em Python que leia um 
# número inteiro qualquer e peça para o usuário escolher qual será a 
# base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.



num = int(input('DIGITE UM NUMERO INTEIRO'))
print('''ESCOLHA UM DAS BASES PARA CONVERÇAO
[ 1 ] CONVERTER PARA BINARIO
[ 2 ] PARA CONVERTER PARA OCTAL
[ 3 ] PARA CONVERTER PARA MEXADECIMAL''')
opçao = int(input('SUA OPÇAO'))
if opçao == 1:
    print('{} CONVERTIDO PARA BINARIO E {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} CONVERTIDO PARA OCTAL E {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} CONVERTIDO PARA MEXADECIMAL E {}'.format(num, hex(um)[2:]))
else:
    print('OPÇAO INVALIDA!! TENTE NOVAMENTE')
