# =================== COMO EU FIZ ==============

lista = []
while True:
    lista.append(int(input("Digite um numero:" )))
    cont = str(input("Quer continucar? S | N  ")).upper().strip()
    lista = list(set(lista)) # set() e definir  para tirar numeros ou nomes repetidos junto com list()
    lista.sort()  # sort() para corganizar do menor para o maior    for do print
    
    
    if cont == "N":
        
        print('-='* 20)
        
        print(lista) 
        print('FIM DO PROGRAMA!')
                
        break
    
    while True:
        
        if cont not in "NS":
            cont = str(input("Quer continucar? S | N  ")).upper().strip()
            
        if cont in "S":
            break
                
# =================== COMO O PROFESSOR FEZ ==============

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionadocom sucesso!')
    else:
        print('Valor dublicado! nao vou adicionar')   
             
    r = str(input('Quer continuar?  S | N : '))
    
    if r in'Nn':
        break
    
numeros.sort() # para colocar em ordem menor para o maior
print(f'Voce digitou os numeros {(numeros)}') 

