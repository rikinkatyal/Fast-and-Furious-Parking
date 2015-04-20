from pygame import *

class Gear() :
	def __init__(self):
		self.reverse = False
		self.gear = 1
		self.gearImage = image.load("res/gear_"+str(self.gear)+".png")

	def shift(self):
		if self.reverse:
			pass
		else:
			pass