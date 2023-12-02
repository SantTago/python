import moeda

p = float(input("Digite o preço R$: "))
print(f'A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')#moeda -> pacote \ moeda -> modulo
print(f'O drobro  de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}')#moeda -> pacote \ moeda -> modulo
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(p, 10))}') #moeda -> pacote \ moeda -> modulo
 