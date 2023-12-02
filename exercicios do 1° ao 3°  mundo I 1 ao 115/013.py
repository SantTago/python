
#-------------------Como eu fiz------------------------------

# Exercício Python 13: Faça um algoritmo que leia o salário 
# de um funcionário e mostre seu novo salário, com 15% de aumento.

h = float(input('Quanto e seu salrario? : '))
h1 = h*15
h2 = h1/100
h3 = h+h2
print('Seu salario de R$:{:.3f} agora e R$: {:.3f} vc teve 15% de aumento'.format(h,h3))




#-------------------Como o professor fez---------------------

preço = float(input('Quanto e seu salario: '))
novo = preço +(preço *15 /100)
print('O produto que custava R${}  na promoçao de 5% vai custar R${}'.format(preço,novo))
