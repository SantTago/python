pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
print(pessoas['nome'])
#==========================================================================
pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
      # quando for formatado tem que ser " duplas 
 #==========================================================================     
pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
print(pessoas.keys()) # .keys() para chamar os nomed das chaves 
#==========================================================================
pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
print(pessoas.values()) # .values() para ver os valores como gustavo M 29
#==========================================================================
pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
for k in pessoas.keys(): # para cada elemento em pessoas . keys trais o nome das chaves 
    print(k)
#==========================================================================
pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
for k, v in pessoas.items(): # para cada elemento em pessoas .values() trais o nome de dentro das chaves
    print(f'{k} = {v}') # k recebe valor de pessoas e V recebe o valor de dentro das chaves 
#==========================================================================
pessoas = {'nome':'Gustavo','sexo':'M','idade':29}
del pessoas['sexo'] # del para apagar um item no dicionario
for k, v in pessoas.items(): # para cada elemento em pessoas .values() trais o nome de dentro das chaves
    print(f'{k} = {v}') # k recebe valor de pessoas e V recebe o valor de dentro das chaves 
#==========================================================================
pessoas['nome'] = 'Pedro' #  pessoas['nome'] = 'Pedro' dessa forma ele vai substituir o nome pelo o do pedro

pessoas['peso'] = 89,7  # para criar um item no dicionario e so criar o nome e dar o valor 
#==========================================================================
# dicionario dentro de uma lista 
brasil = []
estado1 = {'uf':'Rio de janeiro','sigla':'RJ'}
estado2 = {'uf':'Sao Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])  # [0] dentro da lista  ['uf] do diconario
#==========================================================================
estado = dict() # para abrir um diconario 
brasil = list() # para a abir uma lista
for c in range(0,3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # .copy() para fazer uma copia de um dicionario  

for e in brasil: # para cada elemento em brasil
    #for k, v in e.items(): # para cada elemento dentro docionario
    #print(f'O campo {k} tem o valor  {v}')  
    for v in e.values(): # vai mostra para cada valor em dicionario dentro da lista
        print(v,end='')
    print()  
#==========================================================================