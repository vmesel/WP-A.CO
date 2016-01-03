"""
FUNCTIONS FOR THE WP-A.CO URL SHORTENER SERVICE
VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)
"""
# NEED TO CHANGE:
# REMOVE THE MYSQL CONNECTIONS, IT WILL BECOME SQLLITE NOSQL THING
#import mysql.connector


from flask import Flask,render_template,redirect,request
from flask_wtf import Form
from wtforms import StringField, SubmitField
import sys
import string
import random

import socket
from .variables import dbuser, conn

#conn = mysql.connector.connect(user=dbuser, password=dbpass, host=dbserver, database=dbname)

def tipodeurl(url,customalias):

	if not customalias:
		RandAlias = randstring()
	else:
		NewAlias =


	#DEFINIR TIPO DE URL A PARTIR DE REGEX

	#TROCAR PARTE DE CONEXÃO COM SQLLITE
	cursor = conn.cursor()
	cursor.execute("INSERT INTO links(linkoriginal, linkencurtado) VALUES ('%s','%s')" % (urlparaencurtar, nintendo64))
	cursor.close()
	conn.commit()
	conn.close()

	message = "%s/%s" % (linkshortner, nintendo64)
	return message



def checaencurtada(code):
	cursor = conn.cursor()
	query = 'select linkoriginal from links where linkencurtado = "%s"' %(code)
	cursor.execute(query)
	for (linkoriginal) in cursor:
		linkredirecionar = linkoriginal[0]
		return redirect(linkredirecionar, 302)
	cursor.close()
	conn.commit()
	conn.close()
