#-------------- como eu fiz --------------------------

# Exercício Python 32: Faça um programa que leia 
# um ano qualquer e mostre se ele é bissexto.

h = str(input('Digite um numero: '))
if h == 66:
    print('Seu numero e BISSEXTO '.format(h1))
else:
    print('Seu numero NÃo É BISSEXTO'.format(h1))


#-------------- como o professor fez  --------------------------


ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')