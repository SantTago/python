
def fatorial(n): # valor N e substituido por num
    f = 1
    for c in range(1,n,-1):
        f *= c
    return f

num = int(input("Digite um valor: "))
print(fatorial(num)) 
#print(f"O fatorial de {num} é {f}")
