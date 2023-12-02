#======================= COMO EU FIZ ================================
from time import sleep


def contador(*num):
    print('=-' * 20)
    print('    Contagem de 1 ate 10  em 1')
    print('=-' * 20)
    for c in range(0,11):
        print(f'{c}',end=' ')
    print('<= FIM')
    
contador()

def cont(*nu):
    
    print('    Contagem de 10 ate 0 de 2 em 2')
    print('=-' * 20)
    for i in range(10, -1, -1):
        par = (i%2) == 1
        if par == 0:
            print(f'{i}',end=' ')
    print('<= FIM')
print('=-' * 20)
cont()
print('=-' * 20)
print('Agora e sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo:'))

def ficha():
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    print('Carregando','.'*20)
    sleep(1)
    for c in range(inicio,fim,passo):
        print(f'{c}',end=' ')
    print()
print('=-' * 20)
ficha()
print('=-' * 20)

#======================= COMO O PROFESSOR FEZ  ==============================

from time import sleep

def contador(i, f, p): # i = inicio | f = fim | p = passos
    if p < 0:
        p *= -1  # para colocar o numero negativo para possitivo
        
    if p == 0:
        p = 1
    
    print('-=' * 20)
    print(f'Contade de {i} ate {f} em {p}') # i inicio | f Fim | P Passos
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ', flush=True) # flush=True para fazer o sleep fuincionar certo se nao vai mostrar so quando finalizar a conatagem 
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont -= p # fazer o contador com - para seguir para os numeros negativos 
        print('FIM')
        print('-=' * 20)
      
      
# programa principal  
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora e sua vez de personalizar a contagem ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

