#==================== COMO EU FIZ ============================
#==================== COM 3 LISTAS ============================

coluna0 = [[],[],[]]
coluna1 = [[],[],[]]
coluna2 = [[],[],[]]


for c in range(0,3):
    colu0 = int(input(f'Digite um numero para a posiçao [0,{c}]: '))
    
    if c == 0:
        coluna0[0].append(colu0)
    
    if c == 1:
        coluna0[1].append(colu0)
    
    if c == 2:
        coluna0[2].append(colu0)
    
for c in range(0,3):
    colu1 = int(input(f'Digite um numero para a posiçao [1,{c}]: '))
    
    if c == 0:
        coluna1[0].append(colu1)
    
    if c == 1:
        coluna1[1].append(colu1)
    
    if c == 2:
        coluna1[2].append(colu1)
   
for c in range(0,3):
    colu2 = int(input(f'Digite um numero para a posiçao [2,{c}]: '))

    if c == 0:
        coluna2[0].append(colu2)
    
    if c == 1:
        coluna2[1].append(colu2)
    
    if c == 2:
        coluna2[2].append(colu2)

print('=-'*30)



print(f'{coluna0}')
print(f'{coluna1}')
print(f'{coluna2}')
 
 #==================== COMO EU FIZ ============================   
#====================COMO EU FIZ COM UMA LISTA  ===============

coluna0 = [[],[],[],[],[],[],[],[],[]]

for c in range(0,3):
    colu0 = int(input(f'Digite um numero para a posiçao [0,{c}]: '))
    
    if c == 0:
        coluna0[0].append(colu0)
    
    if c == 1:
        coluna0[1].append(colu0)
    
    if c == 2:
        coluna0[2].append(colu0)
    
for c in range(0,3):
    colu1 = int(input(f'Digite um numero para a posiçao [1,{c}]: '))
    
    if c == 0:
        coluna0[3].append(colu1)
    
    if c == 1:
        coluna0[4].append(colu1)
    
    if c == 2:
        coluna0[5].append(colu1)
   
for c in range(0,3):
    colu2 = int(input(f'Digite um numero para a posiçao [2,{c}]: '))

    if c == 0:
        coluna0[6].append(colu2)
    
    if c == 1:
        coluna0[7].append(colu2)
    
    if c == 2:
        coluna0[8].append(colu2)

print('=-'*30)

print(f'{coluna0[0:3]}\n{coluna0[3:6]}\n{coluna0[6:9]}')


#====================COMO O PROFESSOR FEZ =====================


matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3): 
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l},{c}: ')) # matriz [l] para matriz e [c] para as colunas
print('-='*20)
for l in range(0,3): 
    for c in range(0,3):
        print(f'[{matriz[l] [c]:^5}]',end=' ')  # [ {} ]  cochetes fora das cahves mostra que e uma lista no print :^5 para colocar em 5 casas flutuantes
    print() # esse print  serve para quebra a linha  toda vez que a coluna terminar  
