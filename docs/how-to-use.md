How to use WP-A.CO
=========================

Hey, first thanks for taking your precious time for reading the WP-A.CO docs. So there are three ways that you can use this URL Shortener:

- Hosting your own version (Recommended for those who want to have a bunch of custom URLs)
- Using the already usable API that is available online
- Using the WP-A.CO website as your provider (the most recommended, it's always going to be updated)

Or if you want to contribute to the project just run:
```
python wpa.py
```
With the debug options enabled in the source code!

If you choose: Hosting your own URL Shortener
===========================================================================

(This method was only tested on Ubuntu 14.x with uWSGI and nginx)To host your own URL Shortener, you will need to follow these steps:

0 - Install the requirements
You will need to install:

- Python 3.4 or later
- pip
- nginx


**1. Clone the repo**

```
git clone https://github.com/vmesel/WP-A.CO.git
```

**2. Move the "wp-a" folder to your project's folder**
```
mv wp-a/ to/your/preferenced/folder
cd to/your/preferenced/folder/

```
**3. Intall and create the Virtual Environment inside your preferenced folder**
```
pip install virtualenv
virtualenv --python=python3.4 venv/
```
**4. Activate your virtual environment and install requirements listed on the requirements.txt**
```
source venv/source/bin/activate
cd wp-a/
pip3 install -r requirements.txt
```

**5. Test the uWSGI serving**
Edit wpa.py and modify the lines 101-102 to make them similar these lines below (they are commented on the source, if you don't want to make any change, just search for "Server Environment" in wpa.py and uncomment the lines and comment the ones who are not)
```
#This must be uncommented
if __name__ == "__main__":
 app.run(port=BSPort,host="0.0.0.0")

#This must be commented
#if __name__ == "__main__":
# app.run(port=8080,debug=True)
```
After you already uncommented the necessary lines, you can try running this command below.
```
uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi
```
If you reach the WP-A page, it will be all working and you can stop testing and we will start deploying the app to the web. If you don't reach it, debug your server

**6. Create the .INI file for running your**
Create a file called: wpa.ini and add this content:
```
[uwsgi]
module = wsgi

master = true
processes = 5

socket = wpa.sock
chmod-socket = 666
vacuum = true

die-on-term = true
```
**7. Create an Upstart Script**
Create a file in /etc/init/wpa.conf (in case of Ubuntu)
```
description "uWSGI server instance for WP-A and my URL Shortener"

start on runlevel [2345]
stop on runlevel [!2345]

setuid user
setgid www-data

env PATH=/to/your/preferenced/folder/venv/bin
chdir /to/your/preferenced/folder
exec uwsgi --ini wpa.ini
```
Than, with this done, you will be able to run:
```
sudo start wpa
```
**8. Configure Nginx for Proxy Requests**

You will need to create a file with this command:
```
touch wpa.sock
sudo nano /etc/nginx/sites-available/wpa
```
And the content of the file is:
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/to/your/preferenced/folder/wpa.sock;
    }
}
```
After this run these commands to make your URL Shortener available:
```
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo service nginx restart
```
That's it! You have finally installed WP-A.CO in your server and you are up and running to process a lot of URLs.

This will serve all our application


If you choose to create an app and use our API
===========================================================================

To use the API, you will need to make an HTTP request to the page:
```
http://wp-a.co/api/?url=YOUR-URL-HERE&customshort=IF-YOU-WANT-A-CUSTOM-ALIAS-FILL-THIS-FIELD

```
If your HTTP request is all ok, our server will process your request and get you a shorten url.

Or if you just want some URLs Shortened
==================================================

That is the easiest way you can solve your trouble, troll your friends or get your URLs smaller. To start with these, you will need to access (http://wp-a.co)[WP-A.CO] and fill the homepage fields, them hit send and your url is shortened!
