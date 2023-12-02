from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

# Chave de API
API_KEY = 'AIzaSyBN4YwzR5NICUhcqZe5Lj_jD8uMEVZyQ78'

# Criação de um serviço para a API do Google Search
service = build('customsearch', 'v1', developerKey=API_KEY)

# Função para fazer uma busca
def search(query, num_results=10):
    total_results = []
    num_per_request = 10  # Número de resultados por solicitação

    for start in range(1, num_results + 1, num_per_request):
        result = service.cse().list(
            q=query,
            cx='63e73428c5279432c',  # ID do mecanismo de pesquisa personalizado
            num=num_per_request,
            start=start
        ).execute()
        total_results.extend(result.get('items', []))

    return total_results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        results = search(user_input, num_results=100)  # Alterado para 100 resultados
        return render_template('index.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
