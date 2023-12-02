#======================= COMO EU FIZ ================================
from time import sleep

def maior(): #* quando nao se sabe o tamanho do parametro 
    num = list()
    while True:
        num.append(int(input('Numero:')))
        resp = str(input("Quer continuar? (S | N): "))
        if resp in 'Nn':
            break
    print('-='*40)
    print('Analizando os valores passados...',flush=True)
    
    for i in num: # para cada numero na lista num
        print(f'{i}',end=' ',flush=True) # flush=True para o sleep funcionar ceeto
        sleep(0.5)
    print(f'foram informados {len(num)} valores ao todo') 
    if max(num) > 0: 
        print(f'O maior valor informado foi {max(num)}')
    if max(num) == 0:
        print('O maior valor informado e 0')
    print('-='*40)    
maior()
#======================= COMO O PROFESSOR FEZ  ================================ 

from time import sleep

def maior(*num):
    cont = maior = 0
    print('-=' *20)
    print('Analizando os valores passados....')
    for valor in num:
        print(f' {valor} ',end='',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor informado foi {maior}.')
 
#programa principal
maior(2, 9, 5, 7,1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior() 