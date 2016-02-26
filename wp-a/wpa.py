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

app = Flask(__name__)



def processaURL(urlprocessar, customaadd):
	if(customaadd is None):

		return("Sem custom " + str(customaadd))
	else:
		return("Custom:  " + str(customaadd))


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
	print(processaURL(URLadd, CustomURL))


if __name__ == "__main__":
	app.run(debug=True,port=8080)
