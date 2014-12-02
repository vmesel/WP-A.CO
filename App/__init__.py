"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE GNU/GPL 
"""
###################  IMPORT LIBRARIES  ##########################
from flask import Flask,render_template,redirect
import sys
import base64
import string
import random
import mysql.connector
import socket
from .form import URLFORM
#timeout para server defo mysql
timeout = 100
socket.setdefaulttimeout(timeout)
################################################################
app = Flask(__name__)
conexao = mysql.connector.connect(user="", password="", host='', database='')
## set landing pages on the Flask server

###################################################################
def randstring():
    caracteres='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
    return ''.join((random.choice(caracteres) for i in range(5)))

###############################################################################


@app.route("/", methods=['GET', 'POST'])
def home():
    form = URLFORM()
    return render_template("home.html",form=form)
    

@app.route("/<code>")
def encurtada(code=None):
	nintendo64 = code
	conn = conexao
	cursor = conn.cursor()
	query = 'select linkoriginal from links where linkencurtado = "' + nintendo64  + '"'
	cursor.execute(query)

	for (linkoriginal) in cursor:
		linkredirecionar = linkoriginal[0]
		return redirect(linkredirecionar, 302)	



	cursor.close()
	conn.commit()
	conn.close()

	#url = "http://" + code
	

@app.route("/u/<url>")
def gerador(url=None):
	conn = conexao
	url = "http://" + url
	cursor = conn.cursor()
	nintendo64 = randstring()
	cursor.execute("INSERT INTO links(linkoriginal, linkencurtado) VALUES ('%s','%s')" % (url, nintendo64)) 
	cursor.close()
	conn.commit()
	conn.close()
	message = "http://www.wp-a.co/%s" % nintendo64
	return message


@app.route("/u/http://<url>")
def geradorhttp(url=None):
	conn = conexao
	url = "http://" + url
	cursor = conn.cursor()
	nintendo64 = randstring()
	cursor.execute("INSERT INTO links(linkoriginal, linkencurtado) VALUES ('%s','%s')" % (url, nintendo64)) 
	cursor.close()
	conn.commit()
	conn.close()
	message = "http://www.wp-a.co/%s" % nintendo64
	return message


@app.route("/u/https://<url>")
def geradorhttps(url=None):
	conn = conexao
	url = "https://" + url
	cursor = conn.cursor()
	nintendo64 = randstring()
	cursor.execute("INSERT INTO links(linkoriginal, linkencurtado) VALUES ('%s','%s')" % (url, nintendo64)) 
	cursor.close()
	conn.commit()
	conn.close()
	message = "http://www.wp-a.co/%s" % nintendo64
	return message

######################################################


## set to run!
if __name__ == "__main__":
    app.run(debug=True, host="192.168.200.87", port=80)