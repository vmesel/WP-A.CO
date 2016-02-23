"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)

- START RECOGNIZING URLS IN /ADD/
- CREATE A CRYPTO HASH FOR EVERY URL
- WORK ON THE DB AND THE CONNECTION
"""
###################  IMPORT LIBRARIES  ##########################
from flask import Flask,render_template,redirect,request
from flask_wtf import Form
from wtforms import StringField, SubmitField
import sys
import string
import random
import socket

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
@app.route("/add/<urlAEncurtar>")
def addurl(urlAEncurtar):
	return(URLATrabalhar)



if __name__ == "__main__":
	app.run(debug=True)
