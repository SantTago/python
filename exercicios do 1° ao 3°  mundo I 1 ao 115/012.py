
#-------------------Como eu fiz------------------------------

# Exercício Python 12: Faça um algoritmo que leia o 
# preço de um produto e mostre seu novo preço, com 5% de desconto.

h = float(input('Digite o valor do produto: '))
h1 = h*5
h2 = h1/100
h3 = h-h2
print('Valor do produto R$:{:.2f} Reais' .format(h))
print('Com desconto de 5%  R$:{:.2f} Reais '.format(h3))


#-------------------Como o professor fez---------------------


preço = float(input('Qual e o preço do produto: '))
novo = preço -(preço *5 /100)
print('O produto que custava R${}  na promoçao de 5% vai custar R${}'.format(preço,novo))