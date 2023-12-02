from googlesearch import search
from bs4 import BeautifulSoup
import requests
import regex as re

def search_keywords(query, num_results=10):
    search_results = search(query, num_results=num_results)
    return search_results

def extract_paragraph(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    paragraphs = soup.find_all('p')
    if paragraphs:
        return paragraphs[0].get_text()
    else:
        return "Nenhum trecho de parágrafo encontrado"

def highlight_keyword(text, keyword):
    pattern = re.compile(f'({re.escape(keyword)})', re.IGNORECASE)
    return pattern.sub(r'\033[1;31m\1\033[m', text)  # Destaca a palavra-chave

def main():
    query = input("Digite as palavras-chave para a pesquisa: ")
    search_results = search_keywords(query)

    print("Resultados da pesquisa:")
    for idx, result in enumerate(search_results, start=1):
        paragraph = extract_paragraph(result)
        highlighted_paragraph = highlight_keyword(paragraph, query)
        print(f"{idx}. {result}\n\t{highlighted_paragraph}\n")

if __name__ == "__main__":
    main()
