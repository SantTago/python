# Exercício Python 4: Faça um programa que leia algo 
# pelo teclado e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele.

h = bool(input('digite um valor: '))   #verdadeiro ou falso (bool)
print (h)

h = input('dugite algo: ')
print(h .isnumeric())  # para mostrar que o campo e numeros True/False (.isnumeric)

h = input('dugite algo: ')
print(h .isalpha())  # para mostrar que o campo e letras True/False (.isalpha)

h = input('dugite algo: ')
print(h .isalnum())  # para mostrar que o campo e letras e numeros True/False (.isalnum)

h = input('dugite algo: ')
print(h .isupper())  # para mostrar que o campo e letras MAIUSCULAS True/False (.isupper)

#--------------------como eu fiz--------------------@

h =input('digite algo: ')
h1 = h .isspace()  
h2 = h .isnumeric()
h3 = h .isalpha()
h4 = h .isalnum()
h5 = h .isupper()
h6 = h .islower()
h7 = h .istitle()
print('O tipo primitivo desse valor é {}' .format(type(h)))
print('Só tem espaço? {} '.format(h1))
print('E numerico? {} '.format(h2))
print('É alfabetico? {} '.format(h3))
print('È alfanumerico ? {} '.format(h4))
print('Esta em maiusculas ? {} '.format(h5))
print('Esta em minusculas ? {} '.format(h6))
print('Esta capitalizado ? {} '.format(h7))


#-----------------------como o professor fez-----------------------@

h = input('digite algo:')
print('O tipo primitivo desse valor e: ',type(h))
print('Só tem espaço?', h.isspace())
print('E numerico?', h.isnumeric())
print('E alfabetico? ', h.isalpha())
print('E alfanumerico? ', h.isalnum())
print('esta em maiusculo? ', h.isupper())
print('esta em minuscula? ', h.islower())
print('esta capitalizado? ', h.istitle())
