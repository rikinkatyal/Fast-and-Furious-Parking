from pygame import *

class Wall():
	def __init__(self, x, y, surface):
		self.x = x
		self.y = y
		self.surface = surface

	def render(self, wall):
		self.surface.blit(wall, (self.x, self.y))

	def getOuter(self):
		points = []
		for i in range(15):
			points.append((self.x+i, self.y))
			points.append((self.x+i, self.y+15))
			points.append((self.x, self.y+i))
			points.append((self.x+15, self.y+i))
		return points

	def getBoundRect(self):
		return Rect(self.x, self.y, 16, 16)