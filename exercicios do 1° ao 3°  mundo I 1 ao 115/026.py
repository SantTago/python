#-------------- como eu fiz --------------------------

# Exercício Python 26: Faça um programa que leia uma frase pelo 
# teclado e mostre quantas vezes aparece a letra “A”, em que posição 
# ela aparece a primeira vez e em que posição ela aparece a última vez.

h = str(input('Digite uma frase: ')).strip()
h1 = h.upper()
h2 = h1.count('A')
h3 = h1.find('A')+1
h4 = h1.rfind('A')+1
print('\nessa frase tem: {} letras A '.format(h2))
print('primeira posiçao: {} '.format(h3))
print('ultima posiçao: {}'.format(h4))


#-------------- como o professor fez  --------------------------

frase = str(input('Digite uma frase')).upper()
print('A letra A aparece {} vezes nessa frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posiçao {} '.format(frase.find('A')+1))
print('A primeira letra A apareceu na posiçao {} '.format(frase.rfind('A')+1))





