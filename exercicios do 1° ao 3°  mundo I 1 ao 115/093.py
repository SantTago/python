#=======================COMO EU FIZ =======================================

jogadores = dict()

jogadores['nome'] = str(input('Nome: '))
quant = int(input(f'Qunatas partidas {jogadores["nome"]} jogou?: '))

gol = list()
total = 0

for c in range(quant):
    gol.append(int(input(f'quantos gols na partida {c}: ')))
    total += c

jogadores['gols'] = gol
jogadores['total'] = total
print('-='*40)
print(jogadores)
print('-='*40)

for k, v in jogadores.items():
    print(f'O campo {k} tem o valor {v} ')
print('-='*40)
print(f'O jogador {jogadores["nome"]} jogou {quant} partidas')
for k, v in enumerate(gol):
    print(f'Na partida {k} Fez {v} gols.')
print(f'total de gols foi de {total}')

#=======================COMO O PROFESSOR FEZ=======================================

jogador = dict()
partidas = list()
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
