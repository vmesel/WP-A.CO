"""
WP-A VERSION 1.1.0
@vmesel on Twitter or GitHub
"""

# Import Lists
import random
import string




class URLCreator:

	def RandURL():
		return ''.join(random.SystemRandom().choice( string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10))

	def URLDefiner(url, customalias):
		urlsuffix = customalias
		if not urlsuffix:
			urlsuffix = RandURL()
