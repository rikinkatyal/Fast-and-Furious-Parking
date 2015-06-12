#gear class that blits gear image based on speed/gear

from pygame import *

class Gear() :
	def __init__(self):
		"initialize gear and image"
		self.gear = 1
		self.gearImage = image.load("res/gear_"+str(self.gear)+".png")