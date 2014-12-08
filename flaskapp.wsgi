import sys
import logging
from extras.variables import logpath



logging.basicConfig(stream=sys.stderr) #configura o log para ver somente o os erros padrões
sys.path.insert(0, logpath)#preencher entre aspas o caminho para o arquivo no server

#from App import app as application
#application.secret_key = "" # here you can set your secret key for the application
