from pygame import *

class Menu():
	def __init__(self, surface):
		self.surface = surface
		self.bg = transform.scale(image.load("res/main_bg.jpg"), (surface.get_width(), surface.get_height()))
		self.carImage = transform.rotozoom(image.load("res/front_car.png"), 0, 0.45)
		self.carX, self.carY = 447,250
		self.width = self.carImage.get_width()
		self.height = self.carImage.get_height()
		print(self.width, self.height)

	def render(self):
		self.surface.blit(self.bg, (0,0))
		self.width += 16
		self.height += 12
		self.carY += 6
		self.carX -= 8
		self.surface.blit(transform.smoothscale(self.carImage, (self.width, self.height)), (self.carX, self.carY))
		print(self.width, self.height)