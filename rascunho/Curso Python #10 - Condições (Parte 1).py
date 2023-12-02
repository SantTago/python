nome = str(input('Qual seu nome ? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem')
else:
    print('Seu nome e tao normal')
print('Bom Dia, {} '.format(nome))

#-------------------exemplos da aula --------------

h = float(input('Primeira nota: '))
h1 = float(input('Segunda nota: '))
h2 = (h + h1)/2
print('Sua media foi {:.2f}'.format(h2))
if h2 >=6.0:
    print('sua media foi boa Parabéns')
else:
    print('Sua media foi ruim estude mais')

h = float(input('Primeira nota: '))
h1 = float(input('Segunda nota: '))
h2 = (h + h1)/2
print('Parabéns!' if h2 >=6 else 'Estude mais!')

