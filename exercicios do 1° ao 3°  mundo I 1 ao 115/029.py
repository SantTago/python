#-------------- como eu fiz --------------------------

# Exercício Python 29: Escreva um programa que leia a velocidade 
# de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

h = float(input('Qual foi a sua velocidade? '))
h1 = (h-80)*7
if h >=80:
    print('------VOCE FOI MULTADO---------')
    print('Valor da sua multa e R$:{:.2f}'.format(h1))

else:
    print("Parabéns por respeitar o limite de velocidade")

#-------------- como O PROFESSOR FEZ --------------------------


velocidade = float(input('Qual a velocidade doseu carro atual:'))
if velocidade > 80:
    print('MULTADO!! VOCE EXEDEU O LIMITE PERMITIDO NA VIA QUE E DE 80KM/H')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma MULTA de R$: {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado')
