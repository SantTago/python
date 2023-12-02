#================Como eu fiz=====================

import moeda

#programa principal

preço = float(input("Digite o preço R$: "))
print(f"A metade de R$:{preço} e R$:{moeda.metade(preço,True)}") # True de sit=False fa função
print(f"O dobro de R$:{preço} e R$:{moeda.dobro(preço,True)}")
print(f"Aumentando 10%, temos R$:{moeda.aumenta(preço,10, True)}")
print(f"reduzindo 13%, temos R$:{moeda.diminuir(preço, 13, True)}")


#=========Como O professor fez =====================