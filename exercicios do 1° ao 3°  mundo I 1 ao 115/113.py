#================Como eu fiz=====================


while True:
    try:
        inter = int(input('Digite um numero inteiro: '))
        break
    except ValueError:
        print('Erro! Por favor digite um numero inteiro!!')
    except KeyboardInterrupt: # caso algum campo esteja vazio
        print("O usuario preferil nao informar nenhum dado!")
    
        
while True:
    try:
        real = float(input('Digite um numero real: '))
        break
    except ValueError:
        print('Erro! Por favor digite um numero real!!')
    except KeyboardInterrupt: # caso algum campo esteja vazio
        print("O usuario preferil nao informar nenhum dado!")
    
    
print(f"O numero inteiro foi {inter} e o real foi {real}")

#================ Como o professor fez =====================

def leiaint(msg):
    while True:
        try: # tente fazer
        	n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero interito valido!!\033[m')
            continue # para voltar para o While
        else:
            return n # se tudo nao der certo e pq e um numero inteiro
        
def leiafloat(msg):
    while True:
        try: # tente fazer
        	n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero interito valido!!\033[m')
            continue # para voltar para o While
        else:
            return n # se tudo nao der certo e pq e um numero inteiro
    

num = leiaint("digite um numero:")
nu = leiafloat("Digite um numero Real: ")
print(f'o numero inteiro digitado foi {num} e o real foi {nu}')
	 