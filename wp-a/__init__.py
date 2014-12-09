"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE
"""
###################  IMPORT LIBRARIES  ##########################
from flask import Flask,render_template,redirect,request
from flask_wtf import Form
from wtforms import StringField, SubmitField
import sys
import string
import random
import mysql.connector
import socket
from system.variables import timeoutformysql
from system.functions import tipodeurl, tipodeurladd, checaencurtada



socket.setdefaulttimeout(timeoutformysql)


app = Flask(__name__)

def randstring():
	caracteres='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
	return ''.join((random.choice(caracteres) for i in range(5)))

class URLForm(Form):
	url = StringField("URL")
	customshort = StringField("Custom Alias")


@app.route("/", methods=['GET', 'POST'])
def home():
	form = URLForm(csrf_enabled=False)
	return render_template("home.html", form=form)


@app.route("/add/", methods=['GET', 'POST'])
def addurl():
	return tipodeurl(request.args.get("url"),request.args.get("customshort"))




@app.route("/<code>")
def encurtada(code):
	return checaencurtada(code)



@app.route("/u/")
def erroquatrocentosequatro():
	return redirect("/", 302)


@app.route("/u/<url>")
def gerador(url=None):
	return tipodeurladd(url)


@app.route("/u/http://<url>")
def geradorhttp(url=None):
	return tipodeurladd(url)

@app.route("/u/https://<url>")
def geradorhttps(url=None):
	return tipodeurladd(url)

if __name__ == "__main__":
	app.run(debug=True)
