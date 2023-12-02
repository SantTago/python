print(input.__doc__) # para ver as funçoes de input
help(input) #para ver os parametros de inpout

#==================================================================================

def contador(i, f, p):
    c = 0
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')

help(contador)

#==================================================================================

def contador(i, f, p):
    """ # tris aspas e clicar no enter  para criar um manual da fnçao criana 
    Faz uma contagem na tema 

    contador(i, f, p):
        i : Inicio
        f : Fim
        p : Passos
    criado por Tiago Viana Da Cruz
    """
    c = 0
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')

help(contador)

#==================================================================================

def soma(a, b, c=0): # caso nao o C nao receba valr ele sera ignorado com c=0

    s = a+b+c   
    print(f'A soma vale {s}')

soma(3, 2, 5)
soma(9, 5)

#==================================================================================

def soma(a=0, b=0, c=0): # tambem pode ser feito em todos para preencher todas as posibilidades 

    s = a+b+c   
    print(f'A soma vale {s}')

soma(3, 2, 5)
soma(9, 5)
soma()

#==================================================================================


def soma(a=0, b=0, c=0): # caso nao o C nao receba valr ele sera ignorado com c=0
    
    s = a+b+c   
    print(f'A soma vale {s}',end='\n') # end com \n dentro quebra a linha 

soma(a=3, c=2) # pode atribuir os valore dessa forma 

#==================================================================================


def test():
    x = 8  # o valor de X so vale dentro do def  | Variavel Local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#programa principal 

n = 2 # O N ja vai fuincionar em todo contigo | Variavel Global 
print(f'No programa pricipal, n vale {n}')
test()

#==================================================================================

def teste(b):
    a = 8 # Variavel local
    b += 4  # b RECEBE O VALOR DE A QUE E 5 
    c = 2  # VALOR LOCAL
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 # variavel global
teste(a)
print(f'A Fora vale {a}')

#==================================================================================

def funçao():
    n1 = 4 # valor local so vale dentro do def
    print(f'h1 Local vale {n1}')

n1 = 2 # valor global funciona dentro da cuinçao 
funçao()
print(f'h1 Global vale {n1}')

#==================================================================================


def teste(b):
    global a # quando coloca Global o valor 5 e substituido por 8 que o novo valor passado
    a = 8 # Variavel local
    b += 4  # b RECEBE O VALOR DE A QUE E 5 
    c = 2  # VALOR LOCAL
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 # variavel global
teste(a)
print(f'A Fora vale {a}') 

#==================================================================================


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # A variavel S vai para o valor de dentro do print

print(somar(3, 2, 5))  # valor de return s

#==================================================================================

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # A variavel S vai para o valor de dentro do print

n1 = somar(3, 2, 5) # dando o valor da funçao prar uma variavel para que possa ter vsarios formados de prints 
n2 = somar(2, 2)
n3 = somar(6)
print(f'Meus calculos deral {n1}, {n2}. {n3}')

#==================================================================================


def factorial(num=1): # se num for igual a 0 recebe 1
    t = 1
    for c in range(num, 0, -1):
        t *= c
    return t 

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()

print(f'Os resultados são {f1}, {f2}, {f3}')

#==================================================================================

def par(n=0):
    if n % 2 == 0:
        return True # se for par ele retorna True
    else:
        return False # se nao for ele da false

num = int(input('Digite um numero: '))
print(par(num)) # par e a funçao 
if par(num):
    print('E par ')
else:
    print('Nao e par ')