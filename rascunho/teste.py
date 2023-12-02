import random

A, B, C, D = [], [], [], []

for k in range(12):

    nome = input('Digite seu nome: ')
    numero = int(input('Um numero: '))
    outro = int(input('Outro numero: '))

    lista = random.choice([A, B, C, D])
    lista.append(nome + " " + str(numero) +" " + str(outro))