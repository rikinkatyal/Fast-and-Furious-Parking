from pygame import *
from time import time as cTime

class Loading():
	def __init__(self, surface, startTime, dur):
		self.surface = surface
		self.time1 = startTime
		self.time2 = dur
		self.speedometer = image.load("res/speedometer.png")

	def load(self):
		if cTime() - self.time1 < self.time2:
			self.surface.blit(self.speedometer, (0,0))

	def isLoading(self):
		return (cTime() - self.time1 < self.time2)