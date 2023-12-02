

#================ COMO EU FIZ =====================

def ficha():
    
    nome = dict()
    gols = dict()
    fich = list()
    
    nome['nome'] = str(input("Nome do jogador: "))
    fich.append(nome.copy())
    
    gols['gols'] = str(input("Numeros de gols: "))
    fich.append(gols.copy())
    
    print(fich)
    
    print('='*30)
    if fich[0]['nome']:  # if funciona sem dar comparaçao apemas com um parametro
        if fich[1]['gols']:
            print(f'O jogador {fich[0]["nome"]} Fez {fich[1]["gols"]} gol(s) no capeonato')
    
    if fich[0]['nome'] == '':
        if fich[1]['gols']:
            print(f'O jogador <<Jogador desconhecido>> Fez {fich[1]["gols"]} gol(s) no capeonato')
    
    if fich[0]['nome'] == '':  # if funciona sem dar comparaçao apemas com um parametro
        if fich[1]['gols'] == '':
            print(f'O jogador <<Jogador desconhecido>> Fez 0 gol(s) no capeonato')
            
    if fich[0]['nome']:  # if funciona sem dar comparaçao apemas com um parametro
        if fich[1]['gols'] == '':
            print(f'O jogador {fich[0]["nome"]} Fez 0 gol(s) no capeonato')
            
            
#programa principal
ficha()
       
#================ COMO O PROFESOR FEZ =====================

def ficha(jog='<Desconhecido>', gol=0): # parametros caso nao tenha o jog e mostra desconhecido | se gols for vazio recebe 0 
    print(f'O jogador {jog} fez {gol} gols no capeonato')


#programa principal
nome = str(input('Nome do jogador: '))
gols = str(input('numeros de gols? '))

if gols.isnumeric(): # isnumeric() para verificar se a str e numerica 
    gols= int(gols) # se for ele passa ser int
else:
    gols = 0 # se nao tiver nada no campo gols ele vale 0
    
if nome.strip() == '': # .strip para tirar todos os espaços do campo de input | se nome for igual a vazio quando tirar os espaços
    ficha(gol=gols)
else:
    ficha(nome,gols)