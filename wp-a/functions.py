"""
********************************** THIS IS THE FUNCTIONS FILE! **********************************
If you aren't an experienced programmer explore with caution,
but if you want to contribute to the project, this is the right file to edit(EDIT WITH CAUTION).
"""

from flask import Flask,render_template,redirect,request,session,url_for, flash
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
	def InsertURL(Hash, URL, Date, Private, Creator):
		InsertQuery = "INSERT INTO URLManager(HASH, URL, DATE, PRIVATE, CREATOR) VALUES('{}','{}','{}','{}','{}');".format(Hash, URL, Date, Private, Creator)
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

	def URLProcessing(urlprocessar, customaadd, privateurl,CreatorID):
		connection = sql.connect(DBSource)
		cursor = connection.cursor()
		cursorNew = connection.cursor()
		CompleteURL = ""
		urlprocessar = DefaultFunctions.CheckURLPrefix(urlprocessar)
		urlFinal = DefaultFunctions.CustomAlias(customaadd)
		# Get URL Facebook and twitter stuff
		querySelect = "SELECT * FROM URLManager WHERE HASH = '{0}'".format(urlFinal)
		cursor.execute(querySelect)
		urlprefix = "u/"
		if privateurl == "on":
			Private = 1
			urlprefix = "p/"
		else:
			Private = 0


		if len(cursor.fetchall()) == 0:
			cursorNew.execute(str(Database.InsertURL(urlFinal, urlprocessar, datetime.datetime.now(), Private, CreatorID)))
			connection.commit()
			return("http://{0}{1}{2}{3}".format(BSUrl,BSFolder,urlprefix, urlFinal))

		else:
			return("Error: This hash already exists!")
			#CompleteURL = "http://{0}{1}u/{2}".format(BSUrl, BSFolder, urlFinal)

	def AccessURL(urlcode):
		connection = sql.connect(DBSource)
		cursor = connection.cursor()
		CheckQuery = "SELECT PRIVATE from URLManager where HASH = '{0}'".format(urlcode)
		cursor.execute(CheckQuery)
		connection.commit()
		if cursor.fetchone()[0] == 0:
			cursortwo = connection.cursor()
			SecondQuery = "SELECT URL from URLManager where HASH = '{0}'".format(urlcode)
			cursortwo.execute(SecondQuery)
			connection.commit()
			return(cursortwo.fetchone()[0])
		return("http://" + BSUrl + BSFolder + "privateurl/")

	def AccessPrivateURL(urlcode):
		connection = sql.connect(DBSource)
		cursor = connection.cursor()
		cursortwo = connection.cursor()
		FirstQuery = "SELECT CREATOR from URLManager where HASH = '{0}'".format(urlcode)
		cursor.execute(FirstQuery)
		connection.commit()
		try:
			if cursor.fetchone()[0] == session["userid"]:
				SecondQuery = "SELECT URL from URLManager where HASH = '{0}'".format(urlcode)
				cursortwo.execute(SecondQuery)
				connection.commit()
				return(cursortwo.fetchone()[0])
			else:
				return("http://" + BSUrl + BSFolder + "privateurl/")
		except Exception:
			return("http://" + BSUrl + BSFolder + "privateurl/")
