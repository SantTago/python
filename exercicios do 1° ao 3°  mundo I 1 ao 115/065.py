#-------------------    COMO  EU FIZ ---------------

n = 1
cont = 0
media = maior = menor = 0
while n != 0:
    n = int(input('[ 0 ] PARA PARAR | DIGITE UM NUMERO:'))
    cont += 1
    media += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('VOCE  DIGITOU {} NUMEROS E A MEDIA FOI {}'.format(cont-1, (media/(cont-1))))
print('O MAIOR VALOR FOI  {} E O MENOR VALOR FOI {}'.format(maior, menor))


#-------------------    COMO O PROFESSOR FEZ ---------------

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('DIFITE UM NUMERO: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
            menor = num
    resp = str(input('QUER CONTINUAR ? [ S | N]')).upper().strip()[0]
media = soma / quant
print('VOCE DIFITOU {} NUMEROS E A MEDIA ENTRE ELES E {}'.format(quant, media))
print('o maior valor e {} e o menor valor foi {} '.format(maior, menor))








