#------------------como eu fiz--------------------------
print('''
====================================
        10 TERMOS DE UMA PA         
====================================
''')
h1 = int(input('PRIMEIRO TERMO: '))
h2 = int(input('RAZAO: '))
for h in range(h1, 21 - h2, h2):
    print(h, end=' -> ')
print('ACABOU')



#------------------como O PROFESSOR FEZ-------------------

primeiro = int(input("PRIMEIRO TERMO: "))
razao = int(input('RAZAO: '))
decimo = primeiro + (10 -1) * razao #PARA MOSTRAR ATE A 10 CASA
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')