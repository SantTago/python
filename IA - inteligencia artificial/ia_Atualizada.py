import requests
from bs4 import BeautifulSoup

def pesquisar(query, num_results=5):
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        
        for result in soup.find_all('div', class_='tF2Cxc'):
            link = result.a.get('href')
            title = result.h3.get_text()
            snippet = result.find('div', class_='IsZvec').get_text()
            results.append({'title': title, 'link': link, 'snippet': snippet})
        
        return results
    else:
        print("Erro ao buscar resultados")
        return []

if __name__ == "__main__":
    termo_de_pesquisa = input("Digite o termo que deseja pesquisar: ")
    num_de_resultados = int(input("Digite o número de resultados desejados: "))
    
    resultados = pesquisar(termo_de_pesquisa, num_de_resultados)
    
    for i, resultado in enumerate(resultados, start=1):
        print(f"Resultado {i}:")
        print(f"Título: {resultado['title']}")
        print(f"Link: {resultado['link']}")
        print(f"Trecho: {resultado['snippet']}\n")
