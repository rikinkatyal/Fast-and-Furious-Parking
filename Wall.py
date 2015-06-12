#wall class

from pygame import *

class Wall():
	def __init__(self, x, y, surface, pylon=False):
		"Initialize surface, location, and if its a cone"
		self.x = x
		self.y = y
		self.surface = surface
		self.pylon = pylon

	def render(self, wall):
		"Blit wall/cone"
		self.surface.blit(wall, (self.x, self.y))

	def getOuter(self):
		"Returns points bordering wall/cone"
		points = []
		for i in range(15):
			points.append((self.x+i, self.y))
			points.append((self.x+i, self.y+15))
			points.append((self.x, self.y+i))
			points.append((self.x+15, self.y+i))
		return points

	def getBoundRect(self):
		"Returns rect around wall"
		return Rect(self.x, self.y, 16, 16)