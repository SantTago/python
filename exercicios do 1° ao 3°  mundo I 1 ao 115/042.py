#=========== como eu fiz ===================

# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo 
# será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

h1 = float(input('Primeiro segmento: '))
h2 = float(input('Segudo segmento: '))
h3 = float(input('Terceiro segmento: '))
if h1 < h2 + h3 and h2 < h1 + h3 and h3 < h1 + h2:
        print('Os segmentos acima PODEM FORMAR UM  TRIANGULO', end ='')
        if h1 == h2 == h3:
            print(' EQUILATERO')
        elif h1 != h2 != h3 != h1:
            print('ESCALENO')
        else:
            print(' ISOSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')