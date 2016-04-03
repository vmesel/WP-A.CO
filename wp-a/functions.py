"""
********************************** THIS IS THE FUNCTIONS FILE! **********************************
If you aren't an experienced programmer explore with caution,
but if you want to contribute to the project, this is the right file to edit(EDIT WITH CAUTION).
"""

from flask import Flask,render_template,redirect,request
import random
import datetime
import sqlite3 as sql
from random import SystemRandom
import lib.safeurl as safeurl
from settings import *


connection = sql.connect(DBSource)
cursor = connection.cursor()
t = datetime.datetime.now()
SECRAND = SystemRandom()

class Database:
	def InsertURL(Hash, URL, Date):
		InsertQuery = "INSERT INTO URLManager(HASH, URL, DATE) VALUES('{}','{}','{}');".format(Hash, URL, Date)
		return(InsertQuery)

	def Select():
		pass


class DefaultFunctions():
	def CheckURLPrefix(urlprocessar):
		if "http://" in urlprocessar:
			return(urlprocessar)
		elif "https://" in urlprocessar:
			return(urlprocessar)
		else:
			urlprocessar = "http://" + urlprocessar
			return(urlprocessar)


	def CustomAlias(customaadd):
		if customaadd == "":
			key = SECRAND.randint(0, 66 ** 4)
			return(safeurl.num_encode(key))
		else:
			return(customaadd)

	def URLProcessing(urlprocessar, customaadd):
		connection = sql.connect(DBSource)
		cursor = connection.cursor()
		cursorNew = connection.cursor()
		CompleteURL = ""


		urlprocessar = DefaultFunctions.CheckURLPrefix(urlprocessar)
		urlFinal = DefaultFunctions.CustomAlias(customaadd)

		querySelect = "SELECT * FROM URLManager WHERE HASH = '{0}'".format(urlFinal)

		cursor.execute(querySelect)

		if len(cursor.fetchall()) == 0:
			cursorNew.execute(str(Database.InsertURL(urlFinal, urlprocessar, datetime.datetime.now())))
			connection.commit()
			return("http://{0}{1}u/{2}".format(BSUrl, BSFolder, urlFinal))

		else:
			return("Error: This hash already exists!")
			#CompleteURL = "http://{0}{1}u/{2}".format(BSUrl, BSFolder, urlFinal)

	def AccessURL(urlcode):
		connection = sql.connect(DBSource)
		cursor = connection.cursor()
		CheckQuery = "SELECT URL from URLManager where HASH = '{0}'".format(urlcode)
		cursor.execute(CheckQuery)
		connection.commit()
		return(cursor.fetchone()[0])

	def URLClickingHistory():
		#This function must get the url and add 1 click to the History table on the Database
		pass


class Security:
	def Login():
		# Add a table of users, passwords, hashes and etc
		# Define user capabilities and powers! - sysadmin has unlimited power -
		pass

	def RegisterUser():
		pass

	def RegisterURL():
		# Define if the URL is acessed only by the user, by registered users or etc
		pass

	def DoLogin():
		#Create the session and everything needed to authenticate
		pass

class Reporting:
	def ReportContent():
		pass


	def Report():
		pass

	def SendReport():
		pass
