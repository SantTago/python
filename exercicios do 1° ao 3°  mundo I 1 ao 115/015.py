#--------------como eu fiz-----------------------

# Exercício Python 15: Escreva um programa que pergunte a quantidade 
# de Km percorridos por um carro alugado e a quantidade de dias pelos 
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
# custa R$60 por dia e R$0,15 por Km rodado.

h = float(input('Quantos Km vc andou? '))
h1 = int(input('Quantos dias vc ficou com o carro? '))
h2 = h*0.15
h3 = h1*60.00
print('vc ficou {} Dias R$:{:.2f}'.format(h1,h3))
print('vc andou {}Km R$:{:.2f}'.format(h,h2))
print('Seu custo foi de R$:{:.2f}'.format(h2+h3))

#-------------como o professor fez-------------------------

dias = int(input('quantos dias alugados? '))
km = float(input('quantos dias rodados? '))
pago =(dias *60) + (km *0.15)
print('O total a pagar e de {}'.format(pago))
