
# =================== COMO EU FIZ ==============

lista = []
conte = 0



while True:
    lista.append(int(input("Digite um valor: ")))
    cont = str(input("Quer continuar? S | N ")) .upper().strip()
    conte += 1
    
    
    if cont in 'N':
        print('-='*20)
        
        print(f'Voce digitou {conte} elementos ')
        
        print('-='*20)
        break
    
    while True:
        if cont not in "SN":
            cont = str(input("Quer continuar? S | N ")) .upper().strip()

        if cont in 'S': 
            break

lista = list(set(lista))   # list(set) para tirar repetidos
lista.sort(reverse=True)   # lista.sort(reverse=True)  para colocar a lista de trais para frente

print(f'Os valores em ordem decrecente sao {lista}')

print('-='*20)

if 5 in lista:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 nao foi encontrado na lista')
    
print('-='*20)
        
            
print("FIM DO PROGRAMA")
        

# =================== COMO O PROFESSOR FEZ ==============

valores = []

while True:
    
    valores.append(int(input("Digite um valor: ")))
    
    res = str(input('Quer continuar? S | N : '))
    
    if res in 'Nn':
        break
    
print(f'Voce diditou {len(valores)} valores')  # len para contar quantos elementos tem na lista 

valores.sort(reverse=True) # reverse=True paracolocar de trais para frente 

print(f'Os valores na ordem decrecemte e {valores}')

if 5 in valores:
    print('O valor 5 esta na lista')
else:
    print('O valor a 5 NAO esta na lista')