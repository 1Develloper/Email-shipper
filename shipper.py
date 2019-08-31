import getpass
import smtplib
from email.mime.text import MIMEText
#Conexão com os servidores do GOOGLE
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

#Username ou email para logar no servidor
username = input('Digite seu email: ')
password = getpass.getpass('Digite sua senha: ')

from_addr = username
to_adrrs = [input('Digite o email alvo: ')]

#MIMEtext para enviar somente texto
message = MIMEText(input('Digite a mensagem que deseja enviar: '))
message['subject'] = input('Digite o titulo do email: ')
message['from'] = from_addr
message['to'] = ''.join(to_adrrs)

repeat = int(input('Digite quantas vezes quer enviar o MESMO email: '))
#Conexão segura com SSL 
try:
    for x in range(0, repeat):
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username,password)
        server.sendmail(from_addr, to_adrrs, message.as_string())
        server.quit()
        print(x, 'Email(s) ja enviados')
except:
    print('Algo deu errado tente novamente')
else:
    print(repeat,'Email(s) eviado com sucesso para: ', to_adrrs)

