from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

def realizar_pesquisa(query, num_results=5):
    resultados = search(query, num_results=num_results, lang='pt')
    return resultados

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    
    if request.method == 'POST':
        termo_de_pesquisa = request.form.get('termo')
        num_de_resultados = int(request.form.get('num_resultados'))
        resultados = realizar_pesquisa(termo_de_pesquisa, num_de_resultados)
    
    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)