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

cypher = Hashids(salt = "WP-A.co")
app = Flask(__name__)
t = datetime.datetime.now()

def URLGenerate(customaadd, urlprocessar):
	#This is going to need an improvement for grapping in the database and seeing if any url can be reused
	pi = 3.14159
	if(customaadd != ""):
		return("0")
	else:
		return("1")

def processaURL(urlprocessar, customaadd):
	checker = URLGenerate(urlprocessar, customaadd)
	if checker == 0:
		generator = len(urlprocessar) / pi
		untilNow = (t - datetime.datetime(1970,1,1)).total_seconds()
		# To generate the Final Hash
		urlFinal = cypher.encode(int(generator),int(untilNow))

	else:
		urlFinal = customaadd

	# TABLE ORDER: HASH, URL, DATE
	#insertContent = "'"urlFinal"','" urlprocessar"','" datetime.datetime.now()
	#insertContent = ("('" + urlFinal "','" + urlprocessar + "'," + datetime.now() ")")
	connection = sql.connect(DBSource)
	cursor = connection.cursor()
	query = "INSERT INTO URLStorage VALUES('{0}','{1}','{2}')".format(urlFinal, urlprocessar, datetime.datetime.now())
	#return(query)
	cursor.execute(query)
	CompleteURL = "Your url is: http://{0}{1}{2}".format(BSUrl, BSFolder, urlFinal)
	return(CompleteURL)


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


if __name__ == "__main__":
	app.run(port=8080,debug=True)
