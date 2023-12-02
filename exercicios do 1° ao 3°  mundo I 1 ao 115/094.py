#=================== Como eu fiz==================================

lista = list()
mulheres = list()
dici = dict()
media = 0
while True:
    
    dici['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input("Sexo M | F : "))
        if sexo not in 'MmFf':
            print('ERRO! Por favor Respomda apenas M ou F')
        if sexo in 'MmFf':
            break
    
    if sexo in 'Mm': 
        dici['sexo'] = "Mascolino"
    if sexo in 'Ff':
        dici['sexo'] = "Feminino"
        mulheres.append(dici['nome'])
        
    dici['idade'] = int(input('idade: '))
        
    lista.append(dici.copy())
    dici.clear()
    print(lista)
    print('-=' * 30)
    
    while True: 
        continuar = str(input('Quer continuar? S | N :'))
        if continuar not in 'SsNn':
            print('ERRO! Responda apenas S ou N')
        if continuar in 'SsNn':
            break
        
    if continuar in 'Nn':
        break
print(f'- O grupo tem {len(lista)} pessoas') # len para contar quantas chaves de dicionarios tem na lista

for e , v in enumerate(lista):
    media += lista[e]['idade']
    med = media / len(lista)
    
print(f'- media de idade e {med:.0f} anos ')
print(f'- As mulheres cadastradas foram {mulheres}')
print('- Listas das pessoas que estao acima da media:')

for c, v in enumerate(lista):
    acima = lista[c]["idade"]
    
    print(f'{acima}')
    
    
#=================== Como o professor fez==================================

pessoa  = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]')).upper()[0] #[0] so a primeira letra maiuscula
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor difite apenas M ou F')
    pessoa['idade'] = int(input('Idade: ')) 
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar ? S | N :')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N :')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A media de idade e de {media:5.2f} anos ')
print('C) As mulheres cadastradas foram ', end=' ') # end= '' para nao pular de linha
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que stao acima da media:', end=' ')
for p in galera:
    if p['idade'] >= media:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v};',end=' ')
        print()
print('<< ENCERRADO >>')
        