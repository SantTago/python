

def aumentar(preço = 0, taxa = 0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)# is caso seja falso 
# se format nao for falso ele sera True e vai chamar a funçao moeda()
    
def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)
    
    
def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)
    
def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)

def moeda(preço = 0, moeda = "R$:"):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')  # .replac() ele troca o '.' ponto pela ',' virgula