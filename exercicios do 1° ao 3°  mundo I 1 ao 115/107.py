#================Como eu fiz=====================

import moeda

#programa principal

preço = float(input("Digite o preço R$: "))
print(f"A metade de R$:{preço:.2f} e R$:{moeda.metade(preço):.2f}")
print(f"O dobro de R$:{preço:.2f} e R$:{moeda.dobro(preço):.2f}")
print(f"Aumentando 10%, temos R$:{moeda.aumenta(preço,10):.2f}")
print(f"reduzindo 13%, temos R$:{moeda.diminuir(preço, 13):.2f}")

#=========Como O professor fez =====================