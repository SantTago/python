#-------------- como eu fiz --------------------------

# Exercício Python 24: Crie um programa que leia o nome 
# de uma cidade diga se ela começa ou não com o nome “SANTO”.

h = str(input('digite o nome da sua cidade: '))
h1 = h.upper()
print('ASNTO' in h1)



#-------------- como o professor fez  --------------------------

cid = str(input('Qual o nome da cidade que vc nasceu ?')).strip()
print(cid[:5].upper() == 'SANTO')