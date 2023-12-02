#====================COMO EU FIZ ============================

from random import randint

from time import sleep

print('''
====================================
======== JOGO DA MEGA SENA ==========
====================================
''')

num = int(input('Quantos jogos vc quer ? '))

print(f'======== Sorteando {num} Jogos =========')

palpite = []  # lista que vai receber toda vez que sair do for 

for contagem in range(num): # contagem para cada numero de num 
    
    temp = [] # temp lista temporaria para colocar dentro da lista palpite
    
    for cada in range(6):  # para cada numero em range uma casa
        sorteio = randint(1,60)
        
        if sorteio in temp:  # se o sorteio tiver em temp 
            sorteio = randint(1,60)
            temp.append(sorteio) # caso tenha numero ele coloca 
        else:
            temp.append(sorteio) # se nao ele nao coloca nada 
    
    temp.sort() # sort() para deixar o numero do menor para o maior 
    palpite.append(temp[:]) # palpite recebe uma copia da lista sort[:]
    

    print(f'Jogo {contagem+1}:{palpite[contagem]}') # palpite[contagem] para a possiçao do palpite
    
    #================ COMO O PROFESSOR FEZ ==================   

    
from random import randint
from time import sleep

print('-' * 30)
print('      JOGO DA MEGA SENA    ')
print('-' * 30)



jogos = []
tot = 1
quant = int(input('Quantos jogos vcquer que eu sorteie ? : '))


while tot <= quant: # se a qauntidade for menor ou igual a quant ele vai parar 
    lista = list()
    cont = 0 # conte tem que ta dentro do wlile 
    while True:
        num = randint(1,60) # raviavel com randint
        if num not in lista: # se NUM nao tiver ba lista
            lista.append(num) # se naq otiver ele vai colocar dentro de lista
            cont += 1
        if cont >= 6: # se cont for maior ou igual a 6 
            break
        
    lista.sort() # sort para deixar do menor para o amior 
    jogos.append(lista[:])
    lista.clear()
    tot += 1
  
print(f'-' * 15, "Sorteando {quant} Jogos : ",'-' * 15)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} {l}')    # para cada elemento dentro de jogos
    sleep(1)
print('-=' * 5, "<Boa sorte>", '-=' * 5 )