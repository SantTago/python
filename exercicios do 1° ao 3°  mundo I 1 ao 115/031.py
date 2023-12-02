#-------------- como eu fiz --------------------------

# Exercício Python 31: Desenvolva um programa que pergunte a distância 
# de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por 
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

h = float(input('Qual a distancia da sua viagem? '))
if h >=200:
    print('Sua viagem de {}Km/h'.format(h))
    print('Sua passagem da R$: {:.2f}'.format(h*0.45))# se a viagem for menor ou igal a  200 Km/h
else:
    print('Sua viagem de {}Km/h'.format(h))
    print('Sua passagem da R$: {:.2f}'.format(h*0.50))# se a viagem for maior que 200 Km/h
print('---BOA VIAGEM-----')

#-------------- como o professor fez  --------------------------

distancia = float(input('Qual e a distancia da sua viagem:  '))
print('Voce esta preste a começar uma viagem de {:.2f} '.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50 # se a viagem for menor ou igal a  200 Km/h
else:
    preço = distancia * 0.45  # se a viagem for maior que 200 Km/h
print('Sua preço da sua passagem sera de R$:{:.2f} '.format(preço))

preço = distamcia * 0.50 if distancia <=200 else distancia * 0.45  # outra maneira de fazer m


