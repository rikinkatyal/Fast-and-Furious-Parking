from pygame import *
from math import *

from Car import *
from Clock import *
from Gear import *
import Levels

mixer.init()

class Game():
	def __init__(self,surface):
		# Setup initial surface and variables
		self.surface = surface
		self.carImg = open("files/car.txt").read().strip()
		self.mainCar = Car(self.surface, self.carImg, surface.get_width()//2,surface.get_height()//2,0)
		mixer.music.load("res/audio/start.mp3")
		mixer.music.play(0)
		# mixer.music.load("res/audio/engine.mp3")
		# mixer.music.play(-1)
		self.lifeCount = 5
		self.lifeImage = image.load("res/life.png")

		self.gear = Gear()

		self.boundRect = Rect(0,100,surface.get_width(),surface.get_height()-100)

		self.timer = Clock(surface, 120, 1, 1)

		self.wallLoc = []

		self.carObsctacles = [Car(self.surface, "res/Police.png", 400, 300, 86),
		Car(self.surface, "res/truck.png", 800,600, 0),
		Car(self.surface, "res/car1.png", 100, 365, 103)]

	def run(self):
		self.HUD()
		pressed = key.get_pressed()
		arrows = [pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT]]
		if pressed[K_DOWN]:
			self.gear.gearImage = image.load("res/gear_r.png")
		else:
			self.gear.gearImage = image.load("res/gear_"+str(self.mainCar.speed)+".png")
		wasd = [pressed[K_w],pressed[K_s],pressed[K_d],pressed[K_a]]
		if True in arrows:
			self.mainCar.drive(pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT])
		elif True in wasd:
			self.mainCar.drive(pressed[K_w],pressed[K_s],pressed[K_d],pressed[K_a])
		self.mainCar.show()

		for i in self.carObsctacles:
			i.show()

		# Level
		for x in range(len(Levels.level1)):
			for y in range(len(Levels.level1[x])):
				if Levels.level1[x][y] == 1:
					draw.rect(self.surface, (0,0,255), (y*16,x*16+100,16,16))
					self.wallLoc.append(Rect(y*16,x*16,16,16))

	def HUD(self):
		self.header = draw.rect(self.surface, (0, 197, 247), (0,0,self.surface.get_width(),100))
		self.surface.blit(self.gear.gearImage, (0,0))
		livesLocation = 800
		for i in range(self.lifeCount):
			self.surface.blit(self.lifeImage, (livesLocation, 34))
			livesLocation += 37


	def lostLife(self):
		self.lifeCount -= 1

	def shift(self, gear=0, reverse=False):
		self.gear.gear = gear
		self.gear.reverse = reverse
		self.gear.gearImage = image.load("res/gear_"+str(gear)+".png")
		self.mainCar.speed = gear

	def getWall(self):
		return self.wallLoc