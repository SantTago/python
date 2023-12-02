#-------------como eu fiz-------------------------

# Exercício Python 14: Escreva um programa que converta 
# uma temperatura digitando em graus Celsius e converta 
# para graus Fahrenheit.

h = float(input('digite a temperatura ºC:'))
h1 = (h*9/5)
print('a Temporatura em {}°C'.format(h))
print('Convertido para °F da {}°F'.format(h1+32))

#-------------como o professor fez-------------------------

c = float(input('digite a temperatura °C '))
f = ((9 * c) / 5) + 32
print('A temperatura em {}°C e correspondente a {}°F'.format(c,f))


