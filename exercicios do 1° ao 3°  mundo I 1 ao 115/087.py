#====================COMO EU FIZ ============================

matriz = [[0,0,0],[0,0,0],[0,0,0]]

par = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l},{c}: ')) #  nao esquecer de colocar matriz[l][c] 
        
print('-='*30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ')
    print()
    
for p in matriz:
    
    if p[0] % 2 == 0:
        par += p[0]
       
        
    if p[1] % 2 == 0:
        par += p[1]
        
        
    if p[2] % 2 == 0:
        par += p[2]
        

print(f'A soma de todos os valores pares e {par}')

coluna = maior = 0

for n in matriz: # para cada elemento dentro da matriz
    coluna += n[2] # para somar apenas a coluna  3  do lado  idreito

    
for n in matriz[1]:
    if n > maior:
        maior = n
    
        
print(f'A soma dos valores da terceira coluna e {coluna}')
print(f'O maior  valor da segunda coluna e {maior}')



#====================COMO O PROFESSOR FEZ ============================

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = maior = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l},{c} : '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end=' ') # para colocar em 5 casas flutuantes tem que ta formatado 
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos numeros pares e {spar}')
for l in range(0,3):
    scol += matriz[l][2]   # esse for e para cada fazer o range de 0 a 2 para pqgar todos os sumeros da trceira coluna 
print(f'A soma da terceira coluna e {scol}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda coluna e {maior}')