from uteis import numeros # dessa forma ele pega todas as funçoes de dentro de numeros 
num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} e {numeros.dobro(num)}')
#print(f'O dobro de {num} e {uteis.triplo(num)}')