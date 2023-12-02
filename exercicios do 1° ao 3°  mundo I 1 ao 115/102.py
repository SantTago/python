
#================ COMO EU FIZ =====================
def factorial(num, show=False):
    """
    (num) recebe o numero que sera feito o fatorial
    exemplo:
    5 | 5 x 4 x 3 x 2 x 1 = 120
    Parametro tem que ta no factorial( 5 )
    """
    resultado = 1
    cont = 1
    print('='*30)
   
   
    for c in range(num, 0, -1): # valor de num ate o valor 0 de trias para frente
        if show: # se show for True 
            print(c,end='') # para cada valor em c que recebe o valor de num
            if c > 1: # se c for maior que 1 ele mostra um X
                print(' X ',end='')
            else:
                print(' = ',end='') # se ele for menor que 1 ele mostra =
        resultado *= cont
        cont += 1
    return resultado       


#programa principal

print(factorial(1000, show=True))
#print(factorial(5, show=True))
help(factorial)
#================ COMO O PROFESOR FEZ =====================


def fatorial(n, show=False): # show=True e uma parametro opcional para morar a contagem do fatorial 
    """
    -> Calcula o fatorial de um numero
    Parametro ( N ) : O numero a ser calculado  
    Parametro ( Show ) (Opcional) : Mostrar ou nao a conta 
    return : O valor e um fatorial de N
    
    """
    f = 1 # f começa com com 1 para que faça 1 x de trais para frente 
    print('=' * 30)
    for c in range(n, 0, -1): # c para cada valor em n , ele vai ate 0 de trais para frente -1
        if show: # se o show for True 
            print(c,end=' ') # para cada valor de C 
            if c > 1 :   # se C for maior que 1 mostre uma X
                print(' X ',end=' ')
            else:
                print(' = ' ,end='') # se ele for menor ele mostra = 
                
        f *= c
    return f
        
print(fatorial(5, show=True))
help(fatorial)