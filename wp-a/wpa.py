"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)

- WORK ON THE DB AND THE CONNECTION
"""
###################  IMPORT LIBRARIES  ##########################
from flask import Flask,render_template,redirect,request
import random
import datetime
from hashids import Hashids
import sqlite3 as sql
from variables import *
from random import SystemRandom
import lib.safeurl as safeurl

cypher = Hashids(salt = "WP-A.co")
app = Flask(__name__)
t = datetime.datetime.now()
SECRAND = SystemRandom()

def processaURL(urlprocessar, customaadd):
	if customaadd == "":
		key = SECRAND.randint(0, 66 ** 4)
		urlFinal = safeurl.num_encode(key)
	else:
		urlFinal = customaadd

	connection = sql.connect(DBSource)
	cursor = connection.cursor()
	querySelect = "SELECT * FROM URLManager WHERE HASH='{0}'".format(urlFinal)

	cursor.execute(querySelect)
	if len(cursor.fetchall()) < 1:
		query = "INSERT INTO URLManager(HASH, URL, DATE) VALUES('{0}','{1}','{2}')".format(urlFinal, urlprocessar, datetime.datetime.now())
		cursor.execute(query)
		connection.commit()
		CompleteURL = "http://{0}{1}u/{2}".format(BSUrl, BSFolder, urlFinal)
	else:
		CompleteURL = "http://{0}{1}u/{2}".format(BSUrl, BSFolder, urlFinal)

	return render_template("newurl.html",FullURL = CompleteURL)


	#If not, insert it into the database

	#CompleteURL = "Your url is: http://{0}{1}{2}".format(BSUrl, BSFolder, urlFinal)
	#return(CompleteURL)



#Home Function
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("home.html")


@app.route("/add/", methods=['GET', 'POST'])
def addURL():
	global URLadd, CustomURL
	URLadd = request.args.get('url')
	CustomURL = request.args.get('customshort')

	return(processaURL(URLadd, CustomURL))



@app.route("/u/<urlcode>", methods=['GET', 'POST'])
def CheckURL(urlcode):
	# SELECT URL from URLManager where HASH = urlcode
	connection = sql.connect(DBSource)
	cursor = connection.cursor()
	CheckQuery = "SELECT URL from URLManager where HASH = '{0}'".format(urlcode)
	cursor.execute(CheckQuery)
	connection.commit()
	RedirectTo = cursor.fetchone()[0]
	return render_template("render-url.html",RedirectTo = RedirectTo)


if __name__ == "__main__":
	app.run(port=80,debug=True)
