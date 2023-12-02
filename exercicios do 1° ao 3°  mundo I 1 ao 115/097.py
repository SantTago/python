#======================= COMO EU FIZ ================================
pala = str(input('Palavra: '))

def escreva(tex):
    print('=' * len(pala)) # a quantidade de letras da palavra vai definir a qunatidade de linhas
    print(f'{tex}')
    print('=' * len(pala))
    
    
escreva(pala)



#======================= COMO O PROFESSOR FEZ  ================================ 

def escreva(msg):
    tam = len(msg) + 4 # e preciso criar umavariavel para receber otamanho para que possa colocar +4 para colocar um espaço 2 para cada lado
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    
#programa principal
escreva('Gustavo Guanabara')
escreva('Curso de python no youtube')
escreva('Cev')