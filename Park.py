from pygame import *

class Park():
	def __init__(self, surface, x, y):
		self.surface = surface
		self.x = x
		self.y = y
		self.park = image.load("res/park.png")

	def render(self):
		self.surface.blit(self.park, (self.x, self.y))