
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

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'* 30) 
    print(f'resumo do valor'.center(30))  # .center para centralizar o str
    print('-'* 30 )
    print(f'Preço Analizando: \t {moeda(preço)}') # \t para criar uma tabulaçao das informaçoes  caso uma nao seja suficiente tem que por duas \t\t
    print(f'Dobro do preço: \t {dobro(preço, True)}')
    print(f'Metade do preço: \t {metade(preço, True)}')
    print(f'{taxaa}% tanto de aumento: \t {aumentar(preço, taxaa, True)}')
    print(f'{taxar}% tanto de rezução: \t {diminuir(preço, taxar, True)}')
    
    print('-'* 30 )
    
    
def leiadinheiro(msg):
    valido = False # ok começa como false = Falso
    while not valido:
        entrada = str(input(msg)).replace(',' , ' .') # replace para substituir todos os . por ,
        if entrada.isalpha(msg) or entrada.strip() == ' ': # strip para tirar os espaços # .isalpha para verificar se e alfanumeico | caso nao seja numerico  
            print(f'\"{Entrada}\" é um preço invalido!!') # \" para forçar a chamada da chave 
        else:
            valido = True
            return float(entrada)