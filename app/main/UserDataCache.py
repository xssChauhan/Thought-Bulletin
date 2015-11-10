from flask import request
from datetime import datetime

class UserDataCache():
	def __init__(self):
		pass

	def writeUsertoFile(self):
		
		try: 
			with open("userData.txt","a") as f:
				f.write(str(datetime.now()) + " " + request.remote_addr + " " + request.url + " " + request.headers.get('User-Agent') + "\n")
		except IOError,e:
			print e
		return