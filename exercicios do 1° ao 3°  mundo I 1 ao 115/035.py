#-------------- como eu fiz --------------------------

# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('ANALIZADOR DE TRIANGULO')
print('-='*20)
h1 = float(input('Primeiro segmento: '))
h2 = float(input('Segudo segmento: '))
h3 = float(input('Terceiro segmento: '))
if h1 < h2 + h3 and h2 < h1 + h3 and h3 < h1 + h2:  #medir as retas de um triangulo
        print('Os segmentos acima PODEM FORMAR UM  TRIANGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')
print('-='*20)
#-------------- como o professor fez  --------------------------

print('-='*20)
print('ANALIZADOR DE TRIANGULO')
print('-='*20)
h1 = float(input('Primeiro segmento: '))
h2 = float(input('Segudo segmento: '))
h3 = float(input('Terceiro segmento: '))
if h1 < h2 + h3 and h2 < h1 + h3 and h3 < h1 + h2:  #medir as retas de um triangulo
        print('Os segmentos acima PODEM FORMAR UM  TRIANGULO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')
