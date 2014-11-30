from flask import Flask,render_template,request,redirect
#from flask.ext.wtf import Form
app = Flask(__name__)


## set landing pages on the Flask server

titulosite = "GITT.ME"

@app.route("/")
def home():
	Title = titulosite + " | Home"
	pagetype = "home"
	return render_template("home.html",title = Title,pagina=pagetype)









@app.route("/insert")
def insert(url = None):
	return "Insert" 











@app.route("/<code>")
def redirectpage(code=None):
	codigopagina = code
	Title = titulosite + codigopagina
	pagetype = "urlshortned"
	redirectscript  = "http://" + codigopagina


	return redirect(redirectscript, code=302)



	# verify if the url for inputting will be getting the same value






@app.route("/u/<url>")
def paginainsert(url = None):
	tamanho = len(url)


	link = url
	Title = titulosite + " | URL ENCURTADA:" + url
	pagetype = "inserturl"
	
	return render_template("home.html", title = Title, pagina = pagetype, url = url, tamanho = tamanho)





@app.route("/u/http://<url>")
def paginainserthttp(url = None):

	tamanho = len(url)


	link = url
	Title = titulosite + " | URL ENCURTADA:" + url
	pagetype = "inserturl"
	
	return render_template("home.html", title = Title, pagina = pagetype, url = url, tamanho = tamanho)






@app.route("/u/https://<url>")
def paginainserthttps(url = None):

	tamanho = len(url)


	link = url
	Title = titulosite + " | URL ENCURTADA:" + url
	pagetype = "inserturl"
	
	return render_template("home.html", title = Title, pagina = pagetype, url = url, tamanho = tamanho)






@app.route("/about")
def aboutpage():
	Title = titulosite + " | About"
	pagetype = "about"
	return render_template("home.html", title = Title, pagina = pagetype)




























## set to run!
if __name__ == "__main__":
    app.run(debug=True,port=80)