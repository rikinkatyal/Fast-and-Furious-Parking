from pygame import *

class Cone():
	def __init__(self, surface, x, y):
		self.surface = surface
		self.x = x
		self.y = y
		self.cone = image.load("res/cone.png")

	def render(self):
		self.surface.blit(self.cone, (self.x, self.y))