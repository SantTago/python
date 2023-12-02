
def leiaint(msg):
    while True:
        try: # tente fazer
        	n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero interito valido!!\033[m')
            continue # para voltar para o While
        else:
            return n # se tudo nao der certo e pq e um numero inteiro


def linha(tam = 42):
    return '-' * tam


def cabeçario(txt):
    print(linha())
    print(f'{txt:^42}')
    print(linha())
    
    
def menu(lista):
    cabeçario("MENU PRINCIPAL")
    c = 1 
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint("\033[32mSua opçao:\033[33m")
    return opc
    
