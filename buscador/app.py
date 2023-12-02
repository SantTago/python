from flask import Flask, render_template, request
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import regex as re

app = Flask(__name__)

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
    return pattern.sub(r'<span style="color:red">\1</span>', text)  # Destaca a palavra-chave

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        search_results = search_keywords(query)
        
        highlighted_results = []
        for idx, result in enumerate(search_results, start=1):
            paragraph = extract_paragraph(result)
            highlighted_paragraph = highlight_keyword(paragraph, query)
            highlighted_results.append((result, highlighted_paragraph))
        
        return render_template('index.html', query=query, results=highlighted_results)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
