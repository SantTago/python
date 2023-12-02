
# =================== COMO EU FIZ ==============

numeros = list()

for v in range(0,6):
    lista = int(input("Digite um numero: "))
    
       
    if lista not in numeros:
        numeros.append(lista)
        print('Valor adicionado com SUCESSO!')
            
    else:
        print('Valor REPETIDO! Não Registado')
        
#lista.sort()  # .sort() fora do print ele faz a mesma coisa do sorted dentro do print
print(sorted(numeros)) # sorted(lista) para corganizar do menor para o maior    ******dentro do print -ATENÇAO AQUI TIAGO


   
#print(list(set(lista)))  para tirar numeros repetidos
#lista.sort() para colocar em ordem
    

# =================== COMO O PROFESSOR FEZ ==============

lista = []

for c in range(0,5):
    
    n = int(input("Digite um numero: "))
    
    if c == 0 :  
        lista.append(n)
        
    elif n > lista[-1]: #-1 para pegar o ultimo elemento da lista
        lista.append(n)
        
    elif n < lista[len(lista)]:
        lista.append(n)
print(lista)