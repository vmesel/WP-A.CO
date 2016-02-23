"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)
"""
###################  IMPORT LIBRARIES  ##########################
from flask import Flask,render_template,redirect,request
from flask_wtf import Form
from wtforms import StringField, SubmitField
import sys
import string
import random
import socket

app = Flask(__name__)

def randstring():
	caracteres='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%&-+'
	return ''.join((random.choice(caracteres) for i in range(5)))


class URLForm(Form):
	url = StringField("URL")
	customshort = StringField("Custom Alias")


#Home Function
@app.route("/", methods=['GET', 'POST'])
def home():
	form = URLForm(csrf_enabled=False)
	#Render a Web Page template for the Home
	return render_template("home.html", form=form)
	#return("HELLO WORLD")

#Add URL Function - NON API FUNCTION
@app.route("/add/<urlAEncurtar>", methods=['GET', 'POST'])
def nonapiaddurl(urlAEncurtar):
	URLATrabalhar = request.form.get('url', '')
	return(URLATrabalhar)


#Add URL Function - API FUNCTION
@app.route("/add/<urlAEncurtar>", methods=['GET', 'POST'])
def addurl(urlAEncurtar):
	return(urlAEncurtar)


if __name__ == "__main__":
	app.run(debug=True)
