#------------------como eu fiz--------------------------
from datetime import date
cont = 0
menor = 0
for ist in range(1, 8):
    ano = int(input('\033[32mDIGITE O  ANO DO SEU NASCIMMENTO:'))
    soma = date.today().year -ano
    cont += soma >= 18
    menor += soma <= 17
    print('{} ANOS '.format(soma))
if soma >= 18:
    print('\033[36mTEM {} MIORES DE IDADE E'.format(cont))
    print('{} MENORES DE IDADE'.format(menor))


#------------------COOMO O PROFESSOR FEZ --------------------------
totm = 0
totn = 0
from datetime import date
atual = date.today().year
for pess in range(1,8):
    nasc = int(input('QUAL O  ANO DE NSCIMENTO'))
    idade = atual - nasc
    if idade >= 21:
        totm += 1
    else:
        totn += 1
print('AO TODOS TIVEMOS {} PESSSOAS \033[31mMAIOR\033[m DE IDADE'.format(totm))
print('AO TODOS TIVEMOS {} PESSSOAS \033[36mMENOR\033[m DE IDADE'.format(totn))

