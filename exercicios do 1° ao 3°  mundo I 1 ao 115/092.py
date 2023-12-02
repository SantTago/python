#=================== Como eu fiz==================================
ficha = dict()

while True:
    ficha['nome'] = str(input("Nome:"))
    ficha['ano'] = int(input("Ano de nascimento: "))

    ficha['ctps'] = int(input("Carteira de trabalho (0 nao tem): "))
    if ficha['ctps'] == 0:
        break
    if ficha['ctps'] > 0:
        ficha['contrataçao'] = int(input("Ano de contratação: "))
    
        ficha['salario'] = float(input("Salario R$:"))
    print('='*45)
    print(ficha)
    ficha['ano'] -2023 
    #if 
    for k, v in ficha.items():
        print(f'{k} tem o valor {v}')
    con = 2023 - ficha['contrataçao'] 
    if con >= 35:
        print(f'aposentadoria tem o valor de {con}')
    else:
        print(f'falta {35 - con} anos para voce se aposentar')
    break
print('='*20, 'Fim', '=' * 20)

#=================== Como o professor fez==================================

from datetime import datetime # para importa o calendario
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc # datetime para a data # now ano atual # year Dia atual
dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de contrataçao:'))
    dados['salario'] = float(input('Salario R$:'))
    dados['aposentadoria'] = dados['idade'] + (dados['contrataçao'] + 35) - datetime.now().year # idade + (ano de contrataçao + 35) - date... ano atual 
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')