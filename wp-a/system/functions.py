"""
FUNCTIONS FOR THE WP-A.CO URL SHORTENER SERVICE
VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)
"""
from flask import Flask,render_template,redirect,request
from flask_wtf import Form
from wtforms import StringField, SubmitField
import sys
import string
import random
import mysql.connector
import socket
from .variables import dbuser, dbpass, dbname, dbserver, linkshortner

conn = mysql.connector.connect(user=dbuser, password=dbpass, host=dbserver, database=dbname)





def randstring():
	caracteres='abcdefghijklmnopqrstuvwxyz123456789'
	return ''.join((random.choice(caracteres) for i in range(5)))



def tipodeurl(url,customalias):
	urlhttp = url.find("http://")
	urlhttps = url.find("https://")


	if urlhttps != -1:
		print("HTTPS")
		url = url.replace("https://", "")
		urlparaencurtar = "https://" + url

	elif urlhttp != -1:
		print("HTTP")
		url = url.replace("http://", "")
		urlparaencurtar = "http://" + url

	else:
		print("Nada")
		urlparaencurtar = "http://" + url

	if customalias != "":
		nintendo64 = customalias
	else:
		nintendo64 = randstring()

	cursor = conn.cursor()
	cursor.execute("INSERT INTO links(linkoriginal, linkencurtado) VALUES ('%s','%s')" % (urlparaencurtar, nintendo64)) 
	cursor.close()
	conn.commit()
	conn.close()
	message = "%s/%s" % (linkshortner, nintendo64)
	return message

def tipodeurladd(url):
	nintendo64 = randstring()
	urlparaencurtar = url
	return tipodeurl(urlparaencurtar,"")

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






