from flask import Flask,render_template,redirect,request,session,url_for, flash
from functools import wraps
from hashids import Hashids
from functions import *
from git import Repo
from passlib.hash import sha256_crypt as sha256
import os
import subprocess

cypher = Hashids(salt = "WP-A.co")
app = Flask(__name__)
app.secret_key = "wp-a.co key"
git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8')
git_hash = git_hash[:6]

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            LoginError = "You must be logged in!"
            return render_template("login.html", error=LoginError)
        return f(*args, **kwargs)
    return decorated_function

def NewViewReturn(urlprocessar, customaadd):
	return(render_template("added.html",FullURL = DefaultFunctions.URLProcessing(urlprocessar, customaadd), git_hash = git_hash))

@app.route("/home-test/", methods=['GET', 'POST'])
def homeNew():
	return render_template("index2.html", git_hash = git_hash, jumbotroner = False)

@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("index.html", git_hash = git_hash)

@app.route("/new/", methods=['GET', 'POST'])
def newurl():
	return render_template("new.html", git_hash = git_hash)

@app.route("/about/", methods=['GET', 'POST'])
def about():
	return render_template("about.html", git_hash = git_hash)

@app.route("/add/", methods=['GET', 'POST'])
def addRouting():
	global URLadd, CustomURL
	URLadd = request.args.get('url')
	CustomURL = request.args.get('customshort')
	return(NewViewReturn(URLadd, CustomURL))

@app.route("/api/", methods=['GET', 'POST'])
def apiURL():
	#Get API working with usernames
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

@app.route("/register/", methods=['GET', 'POST'])
def register():
	return render_template("register.html")

# Closed to Users Only


@app.route("/login/", methods=['GET', 'POST'])
def loginPage():
	LoginError = None
	if request.method == 'POST':
		userform = request.form['username']
		connection = sql.connect(DBSource)
		c = connection.cursor()
		sqllogin = "SELECT PASSWORD,USERTYPE FROM Users WHERE USERNAME = '{}'".format(str(userform))
		value = c.execute(sqllogin)
		value = c.fetchone()
		try:
			if sha256.verify(str(request.form['password']),str(value[0])) == True:
				session["logged_in"] = True
				session["username"] = userform
				session["usertype"] = str(value[1])
				return render_template("render-url.html",RedirectTo = "/restrict/", git_hash = git_hash)
			else:
				LoginError = "Invalid credentials!"
				return render_template("login.html", error=LoginError, git_hash = git_hash)
		except Exception:
			LoginError = "Invalid credentials!"
			return render_template("login.html", error=LoginError, git_hash = git_hash)


	return(render_template("login.html",error = LoginError, git_hash = git_hash))


@app.route("/logout/", methods=['GET', 'POST'])
@login_required
def logout():
	session.clear()
	return render_template("render-url.html",RedirectTo = "/")

@app.route("/restrict/", methods=['GET', 'POST'])
@login_required
def RestrictedArea():
	return render_template("restrict.html", git_hash = git_hash)


if __name__ == "__main__":
       app.run(port=BSPort, debug=DBGState, host=BSHost)
