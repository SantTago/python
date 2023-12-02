
def leiadinheiro(msg):
    valido = False # ok começa como false = Falso
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha(msg): # .isalpha para verificar se e alfanumeico | caso nao seja numerico  
            print(f'\"{Entrada}\" é um preço invalido!!') # \" para forçar a chamada da chave 
        else:
            valido = True
            return float(entrada)