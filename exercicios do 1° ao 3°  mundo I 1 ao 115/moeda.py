#from moeda import moeda

#from moeda import aumenta, metade, moeda


#================Como eu fiz=====================

def metade(num, sit=False):
    h = num / 2
    if sit:
        s = (f'{h:.2f}')
        return s
    else:
        return h

def dobro(num, sit=False):
    h = num * 2
    if sit:
        s = (f'{h:.2f}')
        return s
    else:
        return h

def aumenta(num, meta=0, sit=False ):
    n = (num * meta) / 100
    if sit:
        s = (f'{n + num:.2f}')
        return s
    else:
        return n

    
def diminuir(num, dimi=0, sit=False):
    n = (num * dimi) / 100
    c = num - n
    if sit:
        s = (f'{c:.2f}')
        return s
    else:
        return c

def moeda(num, format=True):
    n = (f'{num:.2f}')
    return n

def resumo(num=0, au=0, re=0):
    import moeda
    print("-"*30)
    print("       Rezumo do valor")
    print("-"*30)
    dici = dict() 
    dici['Preço Analizado'] = num
    dici['Dobro do preço'] = moeda.dobro(num)
    dici['Metade do preço'] = moeda.metade(num)
    dici['80 % de aumento'] = moeda.aumenta(num,au)+num 
    dici['35 % de reduçao'] = moeda.diminuir(num,re)
    for valor,c in dici.items():
        print(f"\tR$: {valor}:",end='')
        print(f"\tR$:{moeda.moeda(c):<30}")
        
    
    
#=========Como O professor fez =====================