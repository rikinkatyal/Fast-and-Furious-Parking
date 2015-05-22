from pygame import *

class Store():
	init()
	def __init__(self, surface):
		self.surface = surface
		self.bg = transform.scale(image.load("res/store_bg.jpg").convert(), (surface.get_width(),surface.get_height()))
		self.arrow_left = image.load("res/arrow_left.png")
		self.arrow_right = image.load("res/arrow_right.png")
		self.cars = [image.load("res/car%s.png" % i) for i in range(1,12)]
		self.curCar = 1
		self.running = False
		self.angle = 0
		self.x, self.y = 100,100

	def render(self):
		pressed = key.get_pressed()
		self.surface.blit(self.bg, (0,0))
		self.surface.blit(self.arrow_left, (0,0))
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		if Rect(0,0,80,80).collidepoint(mx,my) and mb[0]:
			self.running = False
		if self.curCar > 0:
			self.surface.blit(self.arrow_left, (100,344))
			if Rect(100,344,80,80).collidepoint(mx,my) and mb[0]:
				self.curCar -= 1
		if self.curCar < len(self.cars):
			self.surface.blit(self.arrow_right, (844, 344))
			if Rect(844,344,80,80).collidepoint(mx,my) and mb[0] or pressed[K_RIGHT]:
				self.curCar += 1
		if self.curCar > len(self.cars):
			self.curCar = len(self.cars) - 1
		self.surface.blit(self.cars[self.curCar], (self.x, self.y))


	def isRunning(self):
		return self.running