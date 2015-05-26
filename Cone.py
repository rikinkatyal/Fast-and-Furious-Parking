from pygame import *

class Cone():
	def __init__(self, surface, x, y):
		self.surface = surface
		self.x = x
		self.y = y
		self.cone = image.load("res/cone.png")

	def render(self):
		self.surface.blit(self.cone, (self.x, self.y))

	def getOuter(self):
		points = []
		for x in range(1, self.cone.get_width()-1):
			for y in range(1, self.cone.get_height()-1):
				if self.cone.get_at((x,y))[3] >= 10 and 0 in [self.cone.get_at((x-1,y-1))[3],self.cone.get_at((x,y-1))[3],self.cone.get_at((x+1,y-1))[3],self.cone.get_at((x+1,y))[3],self.cone.get_at((x+1,y+1))[3],self.cone.get_at((x,y+1))[3],self.cone.get_at((x-1,y+1))[3],self.cone.get_at((x-1,y))[3]] or ((y == 1 or y == self.cone.get_height()-2) and self.cone.get_at((x,y))[3] >= 10) or ((x == 1 or x == self.cone.get_width()-2) and self.cone.get_at((x,y))[3] >= 10):
					points.append((x+self.cone.get_width(),y+self.cone.get_height()))
		return (points)