# import uteis 
# para a biblioteca interia 

def fatorial(n): # from uteis import dobro, fatorial 
    f = 1
    for c in range(1, n+1): # ver pq precisa do +1
        f *= c
    return f

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
