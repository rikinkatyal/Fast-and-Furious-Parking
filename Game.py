from pygame import *
from math import *

from Car import *

class Game():
	def __init__(self,screen):
		# Setup initial screen and variables
		self.screen = screen
		self.carImg = open("files/car.txt").read()
		self.mainCar = Car(self.screen)
		self.mainCar.setCar(self.carImg)
		self.mainCar.setLocation(screen.get_width()//2,screen.get_height()//2,0)

	def run(self):
		pressed = key.get_pressed()
		self.mainCar.drive(pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT])
		self.mainCar.show()