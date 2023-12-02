import moeda

p = float(input("Digite o preço R$: "))
print(f'A metade de {p} e {moeda.metade(p)}')
print(f'O drobro  de {p} e {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10)}')
