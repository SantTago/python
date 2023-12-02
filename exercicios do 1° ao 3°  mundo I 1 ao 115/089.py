# ========================= COMO EU FIZ ====================

resu = []
conte = 0
while True:
    nome = [[],[],[]]
    
    nome[0].append(str(input("Nome: ")))
    if nome != 'f':
        conte += 1
        
    nome[1].append(float(input("Nota1: ")))
    nome[2].append(float(input("Nota2: ")))
    
    resu.append(nome[:])
   
    cont = str(input("Quer continuar? S | N :"))
    if cont in 'Nn':
        break

print('=-'*30)
print('''
N°.  Nome      Media
''')

for e ,numeros in enumerate(range(conte)): # para cada numero em conte ele vai da uma volta no for 
    for p in resu: # resu e a lista que recebe os valores assim que eles sai do while
        print(f'{e}  {resu[numeros][ 0 ]} {p[1], p[2]}') 
        break

media = 0
for pa in resu:
    media += pa
print(media)

#=============================como o professor fez =============================

ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1:"))
    nota2 = float(input("nota 2:"))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar ? S|N'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}') #:<4 para 4 casa a direita
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')

while True:
    print('-='*35)
    opc = int(input('Quer ver as notas de qual aluno? (999 para parar)'))
    if opc == 999:
        print('Finalizado.....')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}') 
        
    print('=========Volte Sempre=============')