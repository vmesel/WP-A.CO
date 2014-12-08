"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)
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
timeout = 100 #Timeout for MySQL Connection
socket.setdefaulttimeout(timeout)
#########################  SYSTEM VARIABLES  ###############################
app = Flask(__name__)

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
	conn = mysql.connector.connect(user="", password="", host='', database='')
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
	conn = mysql.connector.connect(user="", password="", host='', database='')
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
	conn = mysql.connector.connect(user="", password="", host='', database='')
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
	conn = mysql.connector.connect(user="", password="", host='', database='')
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
    app.run(debug=True, host="0.0.0.0", port=80)
