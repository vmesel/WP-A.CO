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
	connection = sql.connect(DBSource)
	cursor = connection.cursor()
	CompleteURL = ""

	# Check if there is the HTTP:// in the string
	if "http://" in urlprocessar:
		urlprocessar = urlprocessar
	elif "https://" in urlprocessar:
		urlprocessar = urlprocessar
	else:
		urlprocessar = "http://" + urlprocessar

	if customaadd == "":
		key = SECRAND.randint(0, 66 ** 4)
		urlFinal = safeurl.num_encode(key)
	else:
		urlFinal = customaadd


	querySelect = "SELECT * FROM URLManager WHERE URL = '{0}'".format(urlprocessar)

	cursor.execute(querySelect)
	if len(cursor.fetchall()) < 1:
		query = "SELECT case HASH when HASH IS NULL THEN '0' else '1' end from URLManager where HASH = '{0}'".format(urlFinal)
		cursorNew = connection.cursor()
		cursorNew.execute(query)
		sqlquery = str(cursorNew.fetchone()).replace("[", "").replace("]", "")
		if sqlquery == "None":
			query2 = "INSERT INTO URLManager(HASH, URL, DATE) VALUES('{0}','{1}','{2}')".format(urlFinal, urlprocessar, datetime.datetime.now())
			cursorNew.execute(query2)
		else:
			return("Error: This hash already exists!")
			CompleteURL = "http://{0}{1}u/{2}".format(BSUrl, BSFolder, urlFinal)
	else:
		querySelectHASH = "SELECT HASH FROM URLManager WHERE URL = '{0}'".format(urlprocessar)
		cursor.execute(querySelectHASH)
		cursorURL = cursor.fetchone()[0]
		CompleteURL = "http://{0}{1}u/{2}".format(BSUrl, BSFolder, cursorURL)

	connection.commit()
	return(CompleteURL)

def NewViewReturn(urlprocessar, customaadd):
	return(render_template("added.html",FullURL = processaURL(urlprocessar, customaadd)))


#Home Function
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("index.html")

@app.route("/new/", methods=['GET', 'POST'])
def newurl():
	return render_template("new.html")

@app.route("/about/", methods=['GET', 'POST'])
def about():
	return render_template("about.html")


@app.route("/add/", methods=['GET', 'POST'])
def addURL():
	global URLadd, CustomURL
	URLadd = request.args.get('url')
	CustomURL = request.args.get('customshort')
	return(NewViewReturn(URLadd, CustomURL))

@app.route("/api/", methods=['GET', 'POST'])
def apiURL():
	global URLadd, CustomURL
	URLadd = request.args.get('url')
	CustomURL = request.args.get('customshort')
	ReturnMethod = request.args.get('method')
	try:
		if ReturnMethod == "json":
			ExitingString = "{ 'url' : " + processaURL(URLadd, CustomURL) + "}"
			return(ExitingString)
		elif ReturnMethod == "http":
			return(processaURL(URLadd, CustomURL))
		elif ReturnMethod == "":
			return("Error: No Method Defined!")
	except ValueError:
		return(ValueError)

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

# Server Environment
#if __name__ == "__main__":
#app.run(port=BSPort,debug=True,host="0.0.0.0")

if __name__ == "__main__":
       app.run(port=8080, debug=True)
