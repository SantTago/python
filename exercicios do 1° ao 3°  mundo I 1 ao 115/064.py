#-------------------    COMO  EU FIZ ---------------
num = 0
cont = 1
soma = 1
while num != 999:
    num = int(input('digite um numero de 1 ao 999: '))
    cont += 1
    soma += num
print('VC DIGITOU {} VEZES E A SOMA DOS NUMEROS DA {}'.format(cont-2, soma-1000))
print('FIIM')




#-------------------    COMO O PROFESSOR FEZ ---------------

num = cont = soma = 0
num = int(input('DIGITE UM VALOR [999 STOP]')) #num  fora para  eliminar o flag para parar  da contagem da  soma
while num != 999:
    cont += 1
    soma += num
    num = int(input('DIGITE UM VALOR [999 STOP]'))#num  a soma so vai funcionar se tiver certo se o imput tiver n ultima linha do whilw
print('VOCE DIGITOU {} NUMEROS E A SOMA ENTRE ELES E {}'.format(cont, soma))
print('fim')









