"""
WP-A.CO CODE
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)

- CREATE A CRYPTO HASH FOR EVERY URL
- WORK ON THE DB AND THE CONNECTION
"""
###################  IMPORT LIBRARIES  ##########################
from flask import Flask,render_template,redirect,request
import random
import datetime
from hashids import Hashids

cypher = Hashids(salt = "WP-A.co")

app = Flask(__name__)

t = datetime.datetime.now()

def processaURL(urlprocessar, customaadd):

	#This is going to need an improvement for grapping in the database and seeing if any url can be reused

	pi = 3.14159
	if(customaadd != ""):
		return("Custom:  " + str(customaadd))
	else:
		generator = len(urlprocessar) / pi
		untilNow = (t - datetime.datetime(1970,1,1)).total_seconds()
		# To generate the Final Hash
		urlFinal = cypher.encode(int(generator),int(untilNow))
		return("Sem custom " + str(urlFinal))

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
	app.run(debug=True,port=8080)
