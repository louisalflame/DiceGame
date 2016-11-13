# coding=UTF-8

class InterfaceSpirit:
	def __init__(self, gameManager):
		self.gm = gameManager

	def getInt(self, message=""):
		while True:
			try:
				n = int(input(message))
				if isinstance(n, int) and n>=0 and n <=5:
					break
				else:
					self.printMsg("Please enter integer from 0~5")
			except Exception as e:
				print(e)
				self.printMsg("Please enter integer")

		return n

	def printMsg(self, message=""):
		print (message)

