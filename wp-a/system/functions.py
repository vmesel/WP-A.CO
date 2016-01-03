"""
FUNCTIONS FOR THE WP-A.CO URL SHORTENER SERVICE
VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)
"""
# NEED TO CHANGE:
# REMOVE THE MYSQL CONNECTIONS, IT WILL BECOME SQLLITE NOSQL THING
#import mysql.connector


from flask import Flask,render_template,redirect,request
from flask_wtf import Form
from wtforms import StringField, SubmitField
import sys
import string
import random

import socket
from .variables import dbuser, conn


def checaencurtada(code):
	cursor = conn.cursor()
	query = 'select linkoriginal from links where linkencurtado = "%s"' %(code)
	cursor.execute(query)
	for (linkoriginal) in cursor:
		linkredirecionar = linkoriginal[0]
		return redirect(linkredirecionar, 302)
	cursor.close()
	conn.commit()
	conn.close()
