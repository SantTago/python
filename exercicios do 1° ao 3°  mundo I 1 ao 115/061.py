#========== COMO EU FIZ =================

c = 0
while c != 1:
    primeiro = int(input('''
PRIMEIRO TERMO: '''''))
    razao = int(input('RAZAO: '))
    decimo = primeiro + (10 - 1) * razao  # PARA MOSTRAR ATE A 10 CASA
    for c in range(primeiro, decimo + razao, razao):
        print('{}'.format(c), end=' -> ')
print('ACABOU')



#========== COMO O PROFESOR FEZ =================

print('GERADOR DE PA')
print('-='*20)
primeiro = int(input('PRIMEIRO TERMO'))
razao = int(input('RAZAO '))
termo = primeiro
cont = 1
while cont < 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')
