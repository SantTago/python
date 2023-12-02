import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Configurações de envio de e-mail
email_de = 'mocobom09@gmail.com'  # Seu endereço de e-mail
senha = 'tiagoviana123'  # Sua senha de e-mail
servidor_smtp = 'smtp.gmail.com'  # Servidor SMTP do Gmail
porta_smtp = 587  # Porta SMTP do Gmail

# Lista de destinatários
destinatarios = ['destinatario1@example.com', 'destinatario2@example.com']

# Loop para enviar e-mails para cada destinatário
for destinatario in destinatarios:
    # Criar mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = email_de
    mensagem['To'] = destinatario
    mensagem['Subject'] = 'Assunto do E-mail'

    # Corpo do e-mail (pode ser personalizado)
    corpo_email = "teste -----------------------------------------------------------------."

    mensagem.attach(MIMEText(corpo_email, 'plain'))

    # Anexar arquivo .txt ao e-mail
    with open('arquivo.txt', 'rb') as arquivo:
        anexo = MIMEApplication(arquivo.read(), _subtype="txt")
        anexo.add_header('Content-Disposition', 'attachment', filename='arquivo.txt')
        mensagem.attach(anexo)

    # Iniciar conexão com o servidor SMTP do Gmail
    servidor = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    servidor.starttls()

    # Fazer login na conta de e-mail
    servidor.login(email_de, senha)

    # Enviar o e-mail
    servidor.sendmail(email_de, destinatario, mensagem.as_string())

    # Encerrar a conexão com o servidor SMTP
    servidor.quit()

    print(f'E-mail enviado para {destinatario}')

print('Todos os e-mails foram enviados com sucesso.')
