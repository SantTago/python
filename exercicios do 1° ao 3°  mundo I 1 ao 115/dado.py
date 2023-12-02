
def leiadinheiro(msg):
    valido = False # ok começa como false = Falso
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha(msg): # .isalpha para verificar se e alfanumeico | caso nao seja numerico  
            print(f'\"{Entrada}\" é um preço invalido!!') # \" para forçar a chamada da chave 
        else:
            valido = True
            return float(entrada)
        
        
def leiaint(*msg):
    ok = False # ok começa como false = Falso
    valor = 0
    while True:
        n = str(input(msg))  # na variavel local recebe STR
        
        if n.isnumeric(): # isnumeric() para verificar se e numerico
            valor = int(n) # se for valor que começa com 0 recebe valor int de n 
            ok = True # se for numero OK vira True = Verdadeiro 
            
        else: # se N nao for numero 
            print("\033[0;31mERRO digite um numero inteiro valido!!!\033[m")
            
        if ok: # se tiver OK True ele verifica que ta tudo ok e da break
            break
    return valor # qubado o codigo acaba! ele retorna o valor de int