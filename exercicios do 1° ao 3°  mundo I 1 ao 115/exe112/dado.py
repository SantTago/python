
def leiadinheiro(msg):
    valido = False # ok começa como false = Falso
    while not valido:
        entrada = str(input(msg)).replace(',' , ' .').strip() # replace para substituir todos os . por ,
        if entrada.isalpha() or entrada == '': # strip para tirar os espaços # .isalpha para verificar se e alfanumeico | caso nao seja numerico  
            print(f'\"{entrada}\" \033[31mé um preço invalido!!\033[m') # \" para forçar a chamada da chave 
        else:
            valido = True
            return float(entrada)