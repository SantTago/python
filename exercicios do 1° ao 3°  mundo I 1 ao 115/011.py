
#---------------------------como eu fiz----------------------------

#Exercício Python 11: Faça um programa que leia a 
# largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária 
# para pintá-la, sabendo que cada litro de tinta pinta 
# uma área de 2 metros quadrados.

h = float(input('Digite a largura da sua parede: '))
h1 = float(input('Digite a altura da sua parede: '))
h3 = (h*h1)/2
print('a medida da sua parede e :  {:.0f} Metros quadrados '.format(h*h1))
print('E nessesario : {:.0f} Litros de tinta'.format(h3*1))
print('A cada 2 Metros quadrados se usa 1L de tinta')


#---------------------------como o professor fez----------------------------

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede:'))
area = larg*alt
print('Sua parede tem a dimenssao de {} x {} e sua area e de {} m2'.format(larg,alt,area))
tinta = area /2
print('Para pintar essa parede, voce precisarar de {}L de tinta'.format(tinta))