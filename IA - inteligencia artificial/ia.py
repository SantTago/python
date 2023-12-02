# pip install googlesearch-python
# pip install openai

from googlesearch import search #  googlesearch-python. Esta biblioteca permite que você execute pesquisas no Google

def realizar_pesquisa(query, num_results=5): # funçao realizar_pesquisa 
    resultados = search(query, num_results=num_results, lang='pt')
    
    for i, resultado in enumerate(resultados, start=1):
        print(f"Resultado {i}: {resultado}")

if __name__ == "__main__":
    termo_de_pesquisa = input("Digite o termo que deseja pesquisar: ")
    num_de_resultados = int(input("Digite o número de resultados desejados: "))
    
    realizar_pesquisa(termo_de_pesquisa, num_de_resultados)# realizar_pesquisa -> nome da funçao

