#====================== COMO EU FIZ =====================================

jogador = dict()
partidas = list()
dados = list()
while True:
    partidas.clear()
    jogador['nome'] = str(input('Nome do jagador:'))
    tot = int(input(f'qunatas partidas o {jogador["nome"]} jogou ? '))
    for c in range(0, tot):
        partidas.append(int(input(f'        Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:] #copida de partidas | lista |
    jogador['total'] = sum(partidas) # sum para somar todos dentro de uma lista
    print('-=' * 30)
    print(jogador)
    print('-=' * 30)

    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
    print('-=' * 30)
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

    for i, v in enumerate(jogador['gols']):
        print(f'        Na partida {i}, fez {v}.')
    print(f'Foi um total de {jogador["total"]} gols ')
    dados.append(jogador.copy())
    
    cont = str(input('Quer continuar? S | N :'))
    if cont in 'Nn':
        break
    
print('-=' * 30)
print('cod nome      gols      total')
print('-------------------------------')
   
for v,d in enumerate(dados):
    print(f'{v}   {dados[v]["nome"]}     {dados[v]["gols"]}     {dados[0]["total"]}')
    

while True:
    cara = int(input('mostrar dados de qual jogador? '))
    if cara != 999:
        print(f'{dados[cara]}')
    
    if cara == 999:
        break
print('<<< ENCERRADO >>>')

     
#====================== COMO EU FIZ =====================================

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jagador:'))
    tot = int(input(f'qunatas partidas o {jogador["nome"]} jogou ? '))
    for c in range(0, tot):
        partidas.append(int(input(f'        Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:] #copida de partidas | lista |
    jogador['total'] = sum(partidas) # sum para somar todos dentro de uma lista
    time.append(jogador.copy())
    partidas.clear()
    while True:
        resp = str(input('Quer continuar ? S | N : ')).upper()[0] # upper para deixar tudo maiusculo e [0] paa pegar o primeira letra 
        if resp in 'SN':
            break
        print('ERRO! Respinda apenas S ou N')
    if resp == 'N':
        break

print('cod' ,end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k , v in enumerate(time):
    print(f' {k:>1} ',end='')
    for d in v.values(): # values para ver o nomes das chaves do dicionario 
        print(f' {str(d):<15} ', end=' ')
    print()
print('-=' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! nao existe jogador com codigo {busca}')
    else:
        print(f'------LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} ele fez {g} gols')
    print('-' * 40)
print('<<<VOLTE SEMPRE! FIM DE PROGRAMA>>>')