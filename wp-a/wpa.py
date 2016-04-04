from flask import Flask,render_template,redirect,request,session,url_for
from hashids import Hashids
from functions import *
from git import Repo
import os
import subprocess

cypher = Hashids(salt = "WP-A.co")
app = Flask(__name__)
app.secret_key = "wp-a.co key"
#repo = Repo(os.getcwd())
#master = repo.head.reference
#git_hash = master.commit.hexsha
git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')
git_hash = git_hash[:6] 

def NewViewReturn(urlprocessar, customaadd):
	return(render_template("added.html",FullURL = DefaultFunctions.URLProcessing(urlprocessar, customaadd, git_hash = git_hash)))

@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("index.html", git_hash = git_hash)

@app.route("/new/", methods=['GET', 'POST'])
def newurl():
	return render_template("new.html", git_hash = git_hash)

@app.route("/about/", methods=['GET', 'POST'])
def about():
	return render_template("about.html", git_hash = git_hash)

@app.route("/login/", methods=['GET', 'POST'])
def loginPage():
	LoginError = None
	if request.method == "POST":
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			LoginError = "Invalid credentials!"
		else:
			session['logged_in'] = True
			return render_template("render-url.html",RedirectTo = "/about/")
	return(render_template("login.html",error = LoginError))

@app.route("/restrict/", methods=['GET', 'POST'])
def RestrictedArea():
	if session['logged_in'] == True:
		return render_template("restrict.html", git_hash = git_hash)
	else:
		return render_template("render-url.html",RedirectTo = "/about/")

@app.route("/add/", methods=['GET', 'POST'])
def addRouting():
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
		return("Error: No Method Defined!")

@app.route("/u/<urlcode>", methods=['GET', 'POST'])
def CheckURL(urlcode):
	RedirectTo = DefaultFunctions.AccessURL(urlcode)
	return render_template("render-url.html",RedirectTo = RedirectTo)

if __name__ == "__main__":
       app.run(port=BSPort, debug=DBGState, host=BSHost)
