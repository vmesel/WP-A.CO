"""
THIS IS THE FUNCTIONS FILE!
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
