#================Como eu fiz=====================

import moeda

#programa principal

preço = float(input("Digite o preço R$: "))
print(f"A metade de R$:{moeda.moeda(preço)} e R$:{moeda.moeda(moeda.metade(preço))}")
print(f"O dobro de R$:{moeda.moeda(preço)} e R$:{moeda.moeda(moeda.dobro(preço))}")
print(f"Aumentando 10%, temos R$:{moeda.moeda(moeda.aumenta(preço,10))}")


#=========Como O professor fez =====================