#-------------- como eu fiz --------------------------

# Exercício Python 33: Faça um programa que leia três números 
# e mostre qual é o maior e qual é o menor.

h = float(input('Quanto e seu salrario? : '))
h1 = h*10
h2 = h1/100
h3 = h+h2
#-----------
h4 = h*15
h5 = h4/100
h6 = h+h5
if h >= 1250: # menor ou igual a 1250 gamha 15% de almento
    print('Seu novo Salario e de R$: {:.2f}'.format(h3))
else:
    print('Seu novo salario e de R$: {:.2f}'.format(h6))
print('---Parabéns pelo aumento---')#quem ganha mais que 1250 ganha 10% de almento


#-------------- como o professor fez  --------------------------

salario = float(input('Digite seu salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)  # variavel dentro do if
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava R$:{:.2f} agora vai ganhar R$:{:.2f}'.format(salario, novo))
