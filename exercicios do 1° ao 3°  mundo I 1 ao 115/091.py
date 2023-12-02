#=========== como eu fiz =====================

from random import randint
from operator import itemgetter # operador | itemgetter para fazer a interaçao dentro do dicionario

valores = dict()
   
valores['jogador1'] = randint(1,6)
valores['jogador2'] = randint(1,6)
valores['jogador3'] = randint(1,6)
valores['jogador4'] = randint(1,6)

print(valores)
print()
print(f'Valores sorteados:')
for p, s in valores.items():  # k para valores das keys e S para cada ementro dentro da chave
    print(f'O Jogador {p} tirou = {s}')
    #break
ranking = list()
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True ) # para colocar dentro da lista do maior para o menor 
print('Rancking dos jogadores')
for i , a in enumerate(ranking): # tem que tratar um lista com enumerete 
    print(f'{i+1}° Lugar {a[0]} = {a[1]} ')
    
 #=========== como o professor fez ===================== 

from random import randint
from time import sleep
from operator import itemgetter # operador para colocar dicionario em ordem | itemgetter para fazer isso dentro do diconario com key=itemgetter(1))
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

ranking = list()
print('Valores sorteados')
for k, v in jogo.items(): # k de keys de chaves V para os valores de dentro das chaves 
    print(f'{k} Tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True) #key=itemgetter(1)) (0) para o valore das chaves e 1 para os valoresa  # reverse=True para cvolocar do maior para o menor 

for k , v in enumerate(ranking):
    print(f'{k+1}° Lugar: {v[0]} = {v[1]}')
    sleep(1)

