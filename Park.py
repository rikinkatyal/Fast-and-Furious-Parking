#class that has parking location

from pygame import *

class Park():
	def __init__(self, surface, x, y):
		"Set surface and position of parking spot"
		self.surface = surface
		self.x = x
		self.y = y
		self.park = image.load("res/park.png")
		self.rect = Rect(x,y,73,110)

	def render(self):
		"Blit parking spot"
		self.surface.blit(self.park, (self.x, self.y))