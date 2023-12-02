
lista = list()
lista.append('Gustavo')
lista.append(20)

galera = list()
galera.append(lista[:]) # [:]  Para gerar uma copia do arquivo 
 
lista[0] = 'Maria'  # lista [0] e a primeira lista = 'Maria substitue o nome pelo oque ta dentro da lista
lista[1] = 25
galera.append(lista[:])

print(galera)

#========================================================================

galera = [['Joao',19],['Ana', 33],['Joaquim', 13],['Maria',45]]
galera[3][0] = 'Tiago'    # dessa forma muda o nome de dentro da lista ou numero 
print(galera)

#========================================================================

galera = [['Joao',19],['Ana', 33],['Joaquim', 13],['Maria',45]]
print(galera[0])    
print(galera[0][0])
print(galera[2][1])  # [] [] listas

#========================================================================

galera = [['Joao',19],['Ana', 33],['Joaquim', 13],['Maria',45]]
for p in galera:  # para cada pessoa em galera 
    print(p[1]) # lista das listas 
    
#========================================================================
    
    galera = [['Joao',19],['Ana', 33],['Joaquim', 13],['Maria',45]]
for p in galera:  # para cada pessoa em galera 
    print(f'{p[0]} tem {p[1]} anos de idade') # 0 ta chmando o nomes e 1 as idades
    
#========================================================================
    
galera = list()
dados = list()
for c in range(0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(input('Digite sua idade: '))
    galera.append(dados[:])
    dados.clear() # clear e para linpar a lista quando for passada para outra lista    | se nao a lista mostra todos um por um 
print(galera)
    
galera = list()
dados = list()
for c in range(0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(input('Digite sua idade: '))
    galera.append(dados)  # se esquecer os [:]-Copia ele vai aparecer com as listas fechadas pq o clear vai limpar todas as lstas
    dados.clear() # clear e para linpar a lista quando for passada para outra lista    | se nao a lista mostra todos um por um 
print(galera)
    
#========================================================================
    
galera = list()
dados = list()
totmai = totmeno = 0

for c in range(0,3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(input('Digite sua idade: '))
    galera.append(dados[:])
    dados.clear() # clear e para linpar a lista quando for passada para outra lista    | se nao a lista mostra todos um por um 
    
for p in galera:
    if p[1] >= 21:  # p[1]  para cada idade em galera
        print(f'{p[0]} e maior de idade')  # p[0]   primeira pessoa da lista
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmeno += 1

print(f'temos {totmai} maior de idade e {totmeno} menores de idade ')