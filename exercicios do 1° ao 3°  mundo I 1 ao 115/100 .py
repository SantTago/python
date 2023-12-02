#======================= COMO EU FIZ ================================
from random import randint
sot = list()

def sorteia():
    for i in range(5):
        sot.append(randint(1,10))
    print('-='*30)
    print(f'Sorteando 5 valores da lista',end=' ')
    print(f'{sot}',end=' ')
    print("PRONTO!")

sorteia()
 
def soma():
    soma = 0
    for i in sot:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {sot}, temos {soma}')
    print('-='*30)

soma()

#======================= COMO O PROFESSOR FEZ  ================================ 

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista:',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f' {n} ', end='',flush=True)
        sleep(0.3)
    print('Fim')
    
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
    
numeros = list()

#programa principal
sorteia(numeros)
somapar(numeros)
