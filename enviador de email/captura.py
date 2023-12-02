import requests
import re

# URL do site que você deseja raspar
url = 'https://www.isabelaflores.com'

# Enviar uma solicitação GET para a página
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Extrair e-mails da página usando expressões regulares
    emails = re.findall(r'\S+@\S+', response.text)

    # Nome do arquivo onde você deseja armazenar os e-mails
    nome_arquivo = 'email_cap.txt'

    # Escrever os e-mails em um arquivo de texto
    with open(nome_arquivo, 'w') as file:
        for email in emails:
            file.write(email + '\n')

    print(f'E-mails encontrados e salvos em {nome_arquivo}')
else:
    print(f'Erro ao acessar a página: {response.status_code}')
