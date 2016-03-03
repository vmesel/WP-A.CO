# WP-A.CO
##################################

WP-A stands for Web Powered Access, this actually means that the access to an application is going to be made via the web. And for getting you an easy access to your things, its going get your big urls and transform it into small urls.

WP-A.CO is an Open Source URL Shortener project that is being made with Python, SQLite, HTML and CSS.
Anyone who wants, can develop plugins and other stuff for the project to let it alive!
b
################################################
## Structure
```
wp-a/
 - __init__.py
 - system/
  -- __init__.py
  -- variables.py
 - templates/
  - home.html
  - layouts/
    -- footer.html
    -- header.html
```
################################################
## What we are working on:

- New appearence for the system

- Add HTTP:// in front of the URL

- Check if the HASH is already in use

- Get Meta Info of the Pages

## Functions that can already be used

This is a Beta version of the code, so you can find and experience some bugs, than, you can report to me or give your solution for the problem in a thread in here or send me via email: me@vmesel.com

## How to use as an API

Our URL Shortener isn't just a simple URL Shortener, you can use our own API to create your personal.

To create your own url you just need to make an HTTP Request with the URL:

```
http://yourwebsite.com/add/?url=URL TO BE SHORTEN&customshort=CUSTOM SHORT URL IF YOU WANT
```


## Available in future

url.com/login/ - This page will allow you to login and see your shortened urls.
