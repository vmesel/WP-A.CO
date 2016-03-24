"""
HERE WE ARE GOING TO SET THE VARIABLES FOR THE WEBSITE
"""

# Defines the DEFAULT VARIABLES WITH LIBRARIES
import random
import datetime
from hashids import Hashids
from random import SystemRandom
cypher = Hashids(salt = "WP-A.co")

t = datetime.datetime.now()
SECRAND = SystemRandom()

# USER DEFINED VARIABLES
WebsiteName = "My Custom URL Shortener" # Name of the website
BSUrl = "localhost:8080" # Base url for the whole website
BSFolder = "/" # Base folder for the application
BSHost = "0.0.0.0"
DBSource = "database.db" # database name
BSPort = 8080
