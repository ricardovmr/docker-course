#Criação de um servidor Python simples que irá devolver a página index com o arquivo já criado anteriormente a partir desse servidor

import logging 
import http.server
import socketserver
import getpass     #módulo getpass para obtenção do usuário



class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s\n"% (
            self.client_address[0],
            self.log_date_time_string(),
            format%args
            ))

logging.basicConfig(
        filename='/log/http-server.log',  #caminho do arquivo que será usado para logar
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
)

logging.getLogger().addHandler(logging.StreamHandler())
logging.info('inicializando...')
PORT = 8000

httpd = socketserver.TCPServer(("", PORT), MyHTTPHandler)
logging.info('escutando a porta: %s', PORT)
logging.info('usuário: %s', getpass.getuser())
httpd.serve_forever() 



