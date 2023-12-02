#====================COMO EU FIZ ============================

nome = list()
peso = []
conte = men = menor = 0

while True:
    nome.append(str(input('Nome: ')))
    peso.append(float(input("Peso: ")))
    cont = str(input('Quer continuar ? S | N : '))
    
    if cont not in 'Nn':
        conte += 1
        
    if cont in 'Nn':
        break
    
tod = list()

tod.append(nome) # tod recebe a lista nome e a lista idade separadas em uma unica lista
tod.append(peso[:])

print('-='*30)


print(f'Voce cadastrou {conte + 1} pessoas ')    
print(tod)

for p in tod:
    if p[1] == men:
        print(f'{p[0]}')

print(f'o maior peso foi de {max(tod[1])}Kg. Peso de')  # nao ahei os  nomess dos  maiores 
print(f'o menor peso foi de {min(tod[1])}Kg. Peso de')  # nao ahei os  nomess dos  mmenor
 
print('-='*30)
 

#====================COMO O PROFESSOR FEZ ============================

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: '))) 
    
    if len(princ) == 0:  # len para contar quantos elementos tem na lista lembando que a contagem começa com 0 ...
        mai = men = temp[1] 
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
        
    
    princ.append(temp[:])  #qunado fazer uma copia tem que limpar  a lista anterior para nao ter ligaçao \ usar o.clear
    temp.clear() # o clear tem que ser usado loggo apos  a lista que vai receber as outras listas se por antes a lista fica vazia  
    
    resp = str(input('Quer continuar? N | S'))
    if resp in 'Nn':
        break
    
print(f'Os dados foram{princ}')
print(f'voce cadastro {len(princ)} pessoas') # ao ivem de usar o cont tem como fazer com len que contas quantos tem dentro da lista

print(f'O maior peso foi de {mai}Kg . peso  de ',end=' ')

for p in princ:           # soluçao para  mostra  todas as  pessoas  com maior peso
    if p[1] == mai:
        print(f'[{p[0]}]',end=' ')  # [] fora das {}  para mostrra no print
 
print()

print(f'O menor peso foi de {men}Kg',end=' ')

for p in princ:           # soluçao para  mostra  todas as  pessoas  com maior peso
    if p[1] == men:
        print(f'[{p[0]}]',end=' ')  # [] fora das {}  para mostrra no print
 
print()