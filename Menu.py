from pygame import *

class Menu():
	def __init__(self, surface):
		self.surface = surface
		self.bg = transform.scale(image.load("res/main_bg.jpg"), (surface.get_width(), surface.get_height()))
		self.carImage = image.load("res/front_car.png")
		self.carImageSized = transform.scale(self.carImage, (150, 100))
		self.carX, self.carY = 437,290
		self.width = self.carImageSized.get_width()
		self.height = self.carImageSized.get_height()
		self.logo = image.load("res/logo_perspective.png")
		self.running = True

	def render(self):
		self.pressed = key.get_pressed()
		self.surface.blit(self.bg, (0,0))
		self.width += 16
		self.height += 12
		self.carY += 6
		self.carX -= 8
		self.carImageSized = transform.scale(self.carImage, (self.width, self.height))
		if self.carY > 320:
			self.surface.blit(self.logo, (512-100,380))
		if self.carY < 768:
			self.surface.blit(self.carImageSized, (self.carX, self.carY))
		else:
			if self.pressed[K_SPACE]:
				self.running = False

	def isRunning(self):
		return self.running