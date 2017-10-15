from dbco import db
import random

class Form(object):

	def __init__(self, q1, q2, q3, q4, q5):
		self.q1 = str(q1)
		self.q2 = str(q2)
		self.q3 = str(q3)
		self.q4 = str(q4)
		self.q5 = str(q5)
		

	def to_json(self): 
		myform = dict()
		myform["q1"] = self.q1
		myform["q2"] = self.q2
		myform["q3"] = self.q3
		myform["q4"] = self.q4
		myform["q5"] = self.q5
	
		return myform

	@classmethod
	def from_json(constructor, myform):
		q1 = myform.get("q1")
		q2 = myform.get("q2")
		q3 = myform.get("q3")
		q4 = myform.get("q4")
		q5 = myform.get("q5")
		
		return constructor(q1, q2, q3, q4, q5)