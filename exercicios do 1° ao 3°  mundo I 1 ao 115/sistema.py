def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")
    
    with open('pessoas.txt', 'a') as file:
        file.write(f"{nome},{idade}\n")
        
    print('\033[32m-'*40)
    print("Pessoa cadastrada com sucesso!")
    print('\033[32m-\033[m'*40)
    
def listar_pessoas():
    with open('pessoas.txt', 'r') as file:
        pessoas = file.readlines()
        if pessoas:
            print("Pessoas cadastradas:")
            for idx, pessoa in enumerate(pessoas, start=1):
                nome, idade = pessoa.strip().split(',')
                print(f"{idx}.Nome:{nome}, Idade:{idade}")
        else:
            print("Nenhuma pessoa cadastrada.")
            print("-"*40)

def remover_pessoa():
    listar_pessoas()
    try:
        indice = int(input("Digite o número da pessoa que deseja remover: ")) - 1
        with open('pessoas.txt', 'r') as file:
            pessoas = file.readlines()
        
        if 0 <= indice < len(pessoas):
            pessoa_removida = pessoas.pop(indice)
            with open('pessoas.txt', 'w') as file:
                file.writelines(pessoas)
            print(f"Pessoa '{pessoa_removida.strip()}' removida com sucesso.")
            print("-"*40)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")

def main():
    while True:
        print("\nOpções:")
        print("1. Cadastrar nova pessoa")
        print("2. Listar todas as pessoas cadastradas")
        print("3. Remover uma pessoa da lista")
        print("4. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        print()
        
        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            remover_pessoa()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
