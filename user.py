from dbco import db
import random

class User(object):

	def __init__(self, username, password, typeOfUser):
		
		if not all([username, password, typeOfUser]):
			raise ValueError

		self.username = str(username)
		self.password = str(password)
		self.typeOfUser = str(typeOfUser)
		

	def to_json(self): 
		myuser = dict()
		myuser["username"] = self.username
		myuser["password"] = self.password
		myuser["typeOfUser"] = self.typeOfUser
		

		return myuser

	@classmethod
	def from_json(constructor, myuser):
		username = myuser.get("username")
		password = myuser.get("password")
		typeOfUser = myuser.get("typeOfUser")
		
		return constructor(username, password, typeOfUser)

	def update_time(self):
		self.date_modified = dt.now()