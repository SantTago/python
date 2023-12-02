import moeda

p = float(input("Digite o preço R$: "))
print(f'A metade de {(p)} e {moeda.metade(p, True)}')#moeda -> pacote \ moeda -> modulo
print(f'O drobro  de {(p)} e {moeda.dobro(p,True)}')#moeda -> pacote \ moeda -> modulo
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, True)}') #moeda -> pacote \ moeda -> modulo
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')