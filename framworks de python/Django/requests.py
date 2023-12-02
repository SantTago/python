import requests

class GitHubUser(object):
    url = URITemplate('https://api.github.com/user{/login}')
    def __init__(self, name):
        self.api_url = url.expand(login=name)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.__dict__.update(response.json())
            
#
#Quando o módulo que contém essa classe 
# é carregado, o GitHubUser.url é avaliado 
# e, portanto, o modelo é criado uma vez. 
# Muitas vezes é difícil perceber em Python, 
# mas a criação de objetos pode consumir muito 
# tempo, assim como o módulo re do qual o 
# uritemplate depende. Construir o objeto 
# uma vez deve reduzir o tempo que seu código 
# leva para ser executado.

# pip install uritemplate