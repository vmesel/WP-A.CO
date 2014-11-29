
#		APPLICAITON THAT RUNS THE SERVER ON UBUNTU SERVER STARTUP
#		REQUIRES PIP, EAZY INSTALL, FLASK
#		CREATED BY: m3s3l
#		DESCRIPTION: WEBSERVER APP THAT STARTS UP ON SERVER		

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
if __name__ == "__main__":
    app.run(port=80)
    #app.run(host="201.87.124.142")
