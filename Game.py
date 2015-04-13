from pygame import *
from math import *

from Car import *
from Clock import *

class Game():
	def __init__(self,surface):
		# Setup initial surface and variables
		self.surface = surface
		self.carImg = open("files/car.txt").read()
		self.mainCar = Car(self.surface)
		self.mainCar.setCar(self.carImg)
		self.mainCar.setLocation(surface.get_width()//2,surface.get_height()//2,0)
		self.lifeCount = 5
		self.lifeImage = image.load("res/life.png")

		self.timer = Clock(surface, 120, 1, 1)

	def run(self):
		self.HUD()
		# self.timer.timer()
		pressed = key.get_pressed()
		self.mainCar.drive(pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT])
		self.mainCar.show()

	def HUD(self):
		self.header = draw.rect(self.surface, (0, 197, 247), (0,0,self.surface.get_width(),100))

		livesLocation = 800
		for i in range(self.lifeCount):
			self.surface.blit(self.lifeImage, (livesLocation, 34))
			livesLocation += 37

	def lostLife(self):
		self.liveCount -= 1