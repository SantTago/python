
# =================== COMO EU FIZ ==============


num = []


for c in range(0,5):
    num.append(int(input('DIGITE UM NUMERO: '))) #.append para colocar  na  lista
    
print('-='*30)

for p , v in enumerate(num):
    print(f'Na posiçao {p} foi digitado o numero {v}')
    
print('-='*30)

ma = max(num)
mi = min(num)
pos = num.index(ma) # .index para mostrar a posiçao de um objeto
posi = num.index(mi)


print(f'voce digitou  os valores:\n {num}')
print(f'o maior valor foi {ma} na posiçao {pos+1}')
print(f'o menor valor foi {mi} na posiçao {posi+1}')


print('-='*30)

# =================== COMO O PROFESSOR FEZ ==============


listanum = []
mai = 0
men = 0

for c in range(0,5):
    listanum.append(int(input(f"Digite um valor para a posiçao {c}: ")))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
            
print('-=' *30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posiçao ', end=' ')

for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')

print()
print(f'O meno valor digitado foi {men} na posiçao ',end=' ')

for c , v in enumerate(listanum):
    if v == men:
        print(f'{c}...', end=' ')