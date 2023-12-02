#======================= COMO EU FIZ ================================

def area(msg):
    print('='* len(msg))
    print(msg)
    print('='* len(msg))
    
area('Controle de terreno')

def vezez(a, b):
    d = a * b
    print(f'A area de u mterreno {a} x {b} é {d}m²')
    
lar = float(input('Largura: '))    
comp = float(input('Comprimento: '))
vezez(lar,comp)

#======================= COMO O PROFESSOR FEZ  ================================

def area(compri, larga):
    a = compri * larga
    print(f'A area de um terreno de {compri} x {larga} e de {a}m²')
    
    
print('Controle de terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)