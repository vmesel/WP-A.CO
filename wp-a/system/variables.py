"""
SYSTEM VARIABLES FOR WP-A.CO
BY: VINICIUS MESEL (@VMESEL)
DISTRIBUTED UNDER THE CC SHARE ALIKE LICENSE(AVAILABLE ON THE LICENSE.md FILE)
"""



linkshortner = "http://wp-a.co"
#########################################################  DATABASE INFO  ###########################################################
dbuser = 	""	# Your DB username, like:wp-a 
dbpass = 	""	# Your DB password, like: pass123
dbserver = 	""	# Your DB server, like: 192.168.200.1
dbname =	""	# Your DB name, like: wp-a
con = 		"mysql.connector.connect(user='%s', password='%s', host='%s', database='%s')" %(dbuser,dbpass,dbserver,dbname)
timeoutformysql = 100 # integer that is equal to your timeout for MySQLDB Connection
#####################################################################################################################################






	





