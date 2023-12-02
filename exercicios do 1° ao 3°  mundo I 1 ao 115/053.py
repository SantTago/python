#------------------como eu fiz--------------------------

pali = input('Digite um palavra: ').upper().replace(' ','')
if pali == pali[:: -1]: # PRIMEIRO : DO PRIMEIRO / SEGUNDO : ATE A ULTIMA CASA : -1 DE TRAIS PRA FRENTE
    print('A palavra é Palindroma','\n')
    print('Palavra Invertida: {}'.format(pali),'\n')
else:
    print('A palavra não é Palindroma','\n')

print('Palavra Digitada: {} '.format(pali),'\n')

#------------------como O PROFESSOR FEZ-------------------



frase = str(input('digite uma frase')).strip() .upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) -1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print('TEMOS UM PALINDROMO! ')
else:
    print('NAO E UM PALINDROMO! ')
