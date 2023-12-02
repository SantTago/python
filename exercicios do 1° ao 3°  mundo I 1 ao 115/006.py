
#-------------------------------como eu fiz------------------------------------#

# Exercício Python 006: Crie um algoritmo 
# que leia um número e mostre o seu dobro, 
# triplo e raiz quadrada.

h = int(input('difite um numero: '))
h1 = (h) + (h)
h2 = (h) + (h) + (h)
h3 = (h) ** (h)    #nao consegui resolver
print('O dobro de {} e {} ' .format(h , h1))
print('O triblo de {} e {} ' .format(h , h2))
print('A raiz quadrada de {} e {}'.format(h , h3))


#-------------------------------como o professor fez ------------------------------------#

h = int(input('digite um numero: '))
h1 = h *2
h2 = h *3
h3 = h**(1/2)
print('O dobro de {} vale {} '. format(h , h1))
print ('O trilho de {} vale {}. A raiz quadrada de {} e igual {:.2f} '.format(h, h2 , h ,h3))

#-------------------------------outrp jeito de fazer ------------------------------------#

h = int(input('digite um numero: '))
print('O dobro de {} vale {} '. format(h ,(h*2)))
print ('O trilho de {} vale {}. \nA raiz quadrada de {} e igual {:.2f} '.format(h, (h*3) , h, (h**(1/2))))


