from twilio.rest import Client

# Configure suas credenciais do Twilio
account_sid = 'AC0fc951b969d51573f34e3d3b93fd9c92'
auth_token = '132619e5010f76f13ebca09e092d1524'

# Inicialize o cliente Twilio
client = Client(account_sid, auth_token)

# Número de telefone de destino (deve incluir o código do país, por exemplo, +1 para os EUA)
numero_destino = '+5588993464285'  # Substitua pelo número Twilio correto

# Mensagem que você deseja enviar
mensagem = 'teste '

import time

time.sleep(3)
# Envie a mensagem
while True:
    try:
        mensagem_enviada = client.messages.create(
            to=numero_destino,
            from_='+16195928748',  # Substitua por seu número Twilio (sem o "+")
            body=mensagem
        )
        print(f'Mensagem enviada com sucesso com o SID: {mensagem_enviada.sid}')
        time.sleep(3)
    except Exception as e:
        print(f'Erro ao enviar mensagem: {str(e)}')
