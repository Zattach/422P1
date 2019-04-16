'''
April 7
Author: Nicholas Bonat
'''

class Student:
	def __init__(self, firstName, lastName, uoID, email, pSpelling, reveal):
		self.fname = firstName
		self.lname = lastName
		self.id = uoID
		self.email = email
		self.pspell = pSpelling
		self.reveal = reveal
		self.correctQ = 0
		self.calledOnCount = 0

	def getFName(self):
		return self.fname

	def getLName(self):
		return self.lname

	def getID(self):
		return self.id

	def getEmail(self):
		return self.email

	def getReveal(self):
		return self.reveal

	def getCorrectQ(self):
		return self.correctQ

	def setCorrectQ(self, correct):
		self.correctQ = correct

	def getCalledOnCount(self):
		return self.calledOnCount

	def setCalledOnCount(self, called):
		self.calledOnCount = called