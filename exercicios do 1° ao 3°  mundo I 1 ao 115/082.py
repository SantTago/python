
# =================== COMO EU FIZ ==============

lista = []
lista1 = []
lista2 = []

while True:
    lista.append(int(input("Digite um numero: ")))
    con = str(input("Quer continuar? S | N ")) .upper().strip()
  
    if con in 'N':
        break
    
    while True:
    
        if con not in 'NS':
            con = str(input("Quer continuar? S | N ")) .upper().strip()
        
        if con in 'S':
            break


print('-='*20)

print(f'lista completa {lista}')

print('-='*20)

for pares in lista:
    if pares % 2 == 0:
        lista1.append(pares)   # lista1.append(pares)  ele vai tira os valores pares da lista e vai colocar na lista pares
print(f'Os numeros pares sao {lista1}')

print('-='*20)

for impar in lista:
    if impar % 2 == 1:
        lista2.append(impar)   # lista1.append(impar)  ele vai pega os impar de uma lista e vai colocar na lista2
print(f'Os numeros impar sao {lista2}')

print('-='*20)

print("Fim do programa")
        

# =================== COMO O PROFESSOR FEZ ==============

num = list()
par = []
impar = [] 

while True:
    num.append(int(input('Digite um numero: ')))
    
    resp = str(input('Quer continuar ? S | N : '))
    if resp in 'Nn':
        break
    
for c,v in enumerate(num):
    if v % 2 ==0:
        par.append(v)
    
    elif v % 2 ==1:
        impar.append(v)
        
print(f'A soma de todos os valores e {num}')
print(f'A lista dos pares e {par}')
print(f'A lista dos impar e {impar}')