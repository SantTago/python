def linhas():
    print('-='*30)
#programa principal
linhas()
print('curso')
print('aprenda python')
print('tiago')

#=====================================================================================================================================

def mensagem(msg): #def cria um funçao mensagem e o nome que vai receber o parametros e o MSG sera o campo subistituido pelo parametro
    print('-='*30)
    print(msg)
    print('-='*30)
    
mensagem('Sistemas de alunos') # tudo que tiver entre ' ' sera substituido pala MSG
mensagem('Aprenda Python')
mensagem('Bom Domingo')
  
#=====================================================================================================================================

def soma(a, b):
    s = a + b
    print(s)

#programa principal 
soma(4, 5)
soma(8, 9)
soma(2, 1)

#=====================================================================================================================================
def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A sama A + B = {s}')

#programa principal 
soma(a=4, b=5) # dessa forma vc explicita o valor que vai para cada parametro

#=====================================================================================================================================

def contador(* num): # * quanto nao souber os taanhos dos parametros | ele vai pegar todos osvalores e colocar em num 
    for valor in num:
        print(f'{valor}', end=' ')
    print('fim')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#=====================================================================================================================================
def contador(* num): # * quanto nao souber os taanhos dos parametros | ele vai pegar todos osvalores e colocar em num 
    tama = len(num) # len para mediar o tamanho de dupla
    print(f'recebi o valor {num} e tem {tama} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#=====================================================================================================================================

def dobra(ist):
    pos = 0
    while pos < len(ist): # enquanto o valor pos for menor que o valor do meu parametro ele vai dobrar o valor 
        ist[pos]*=2  # parabre *= 2 
        pos +=1
        
        
valores = [7, 2, 5, 0, 4]
dobra(valores) 
print(valores)

#=====================================================================================================================================

def soma(*num): # * para colocar varios parametros 
    s = 0                                  # DESEMPACOTAMENTO DE CPACOTES 
    for i in num: # para cada numero em num
        s += i # aomar ele 
    print(f'Somando os valor {num} da {s}')


soma(5, 2)
soma(4, 5, 6)