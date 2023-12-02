#===  ESSE FIZ CERTO MAIS COM DUAS LISTAS O PROF PEDIU COM APENAS COM UMAS  ==========================

pares = list()
impar = list()

for num in range(0,7):
    numeros = int(input(f'Digite o {num+1}° numero: '))

    if numeros % 2 == 0:
        pares.append(numeros)
    if numeros % 2 == 1:
        impar.append(numeros)


print(f'Os valores pares digitados foram {sorted(pares)}')
print(f'Os valores impares digitados foram {sorted(impar)}')

#======  COMO EU FIZ DO JEITO CERTO COM APENAS DUAS LISTAS ==========================


numeros = list()

for num in range(0,7):
    numeros.append(int(input(f'Digite o {num+1}° numero: ')))
    
pares = list()

impar = list()
    
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)


print(f'Os valores pares digitados foram {sorted(set(pares))}') # set para tirar numeros repetidos
print(f'Os valores Impar  digitados foram {sorted(set(impar))}') # set para tirar numeros repetidos



#=====================  COMO O PROFESSOR FEZ ==========================

num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor) 
    else:
        num[1].append(valor)
print(f'Os valores pares digitados foram {sorted(num[0])}')
print(f'Os valores impares digitados foram {sorted(num[1])}')

#===================outro jeito de deixar em ordem========================


num[0].sort() # dessa forma ele vai deixaer em ordem a lista selecionata  com num[0]
num[1].sort()

print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')