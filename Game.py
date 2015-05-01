from pygame import *
from math import *
from time import time as cTime

from Car import *
from Clock import *
from Gear import *
import Levels
from Wall import *

mixer.init()

class Game():
	def __init__(self,surface):
		# Setup initial surface and variables
		self.surface = surface
		self.carImg = open("files/car.txt").read().strip()
		self.mainCar = Car(self.surface, self.carImg, surface.get_width()//2,surface.get_height()//2+200,0)
		mixer.music.load("res/audio/start.mp3")
		mixer.music.play(0)
		# mixer.music.load("res/audio/engine.mp3")
		# mixer.music.play(-1)
		self.lifeCount = 5
		self.lifeImage = image.load("res/life.png")

		self.logo = image.load("res/logo.png")
		self.startTime = 0
		self.timeDelay = False

		self.gameover = False
		
		self.crash = False
		self.crashImage = image.load("res/crash.png")

		self.gear = Gear()

		self.boundRect = Rect(0,100,surface.get_width(),surface.get_height()-100)

		self.walls = []
		self.grasses = []

		self.carObsctacles = [Car(self.surface, "res/car17.png", 400, 300, 86),
		Car(self.surface, "res/car15.png", 800,600, 0),
		Car(self.surface, "res/car1.png", 100, 365, 103)]

		self.grass = image.load("res/grass.png")

		self.timer = Clock(surface, cTime, 1, 1, 0)

		# Level
		for x in range(len(Levels.level1Map)):
			for y in range(len(Levels.level1Map[x])):
				if Levels.level1Map[x][y] == 1:
					self.walls.append(Wall(y*16,x*16+100,self.surface))
				elif Levels.level1Map[x][y] == 2:
					self.grasses.append((y*16,x*16+100))

		self.wall_y = image.load("res/wall_y.png")
		self.wall_b = image.load("res/wall_b.png")

	def sTime(self, time):
		self.startTime = time
		self.timer = Clock(self.surface, time, 1, 1, 120)

	def run(self):
		if self.timer.gameOver():
			self.gameover = True
			print("GAME OVER")
		if self.lifeCount == 0:
			self.gameover = True
		if cTime()-self.startTime > 2:
			self.timeDelay = True
			# mixer.music.load("res/audio/engine.mp3")
			# mixer.music.play(-1)
		self.HUD()
		pressed = key.get_pressed()
		arrows = [pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT]]
		if pressed[K_DOWN]:
			self.gear.gearImage = image.load("res/gear_r.png")
		else:
			self.gear.gearImage = image.load("res/gear_"+str(self.mainCar.speed)+".png")
		wasd = [pressed[K_w],pressed[K_s],pressed[K_d],pressed[K_a]]
		
		if not self.gameover:
			if pressed[K_e]:
				self.mainCar.brake()
				self.mainCar.drive()
			elif True in arrows and self.timeDelay:
				self.mainCar.drive(pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT])
				self.mainCar.brakeSound.stop()
			elif True in wasd and self.timeDelay:
				self.mainCar.drive(pressed[K_w],pressed[K_s],pressed[K_d],pressed[K_a])
				self.mainCar.brakeSound.stop()
			else:
				self.mainCar.drive()
				self.mainCar.brakeSound.stop()
		for car in self.carObsctacles:
			if car.getBoundRect().colliderect(self.mainCar.getBoundRect()):
				self.crash = True
				for carOut in car.outline:
					self.surface.set_at(carOut, (255,255,255))
			car.render()


		yellow = False
		for wall in self.walls:
			if yellow:
				wall.render(self.wall_y)
				yellow = False
			else:
				wall.render(self.wall_b)
				yellow = True
			if wall.getBoundRect().colliderect(self.mainCar.getBoundRect()):
				self.crash = True
		for gr in self.grasses:
			self.surface.blit(self.grass, gr)

		# for g in self.mainCar.outline:
		# 	self.surface.set_at((int(g[0]), int(g[1])), (255,255,255))
		for g in self.mainCar.outlineRotated:
			self.surface.set_at((int(g[0]), int(g[1])), (255,255,255))
		self.mainCar.render()

		# if self.crash:
		# 	self.surface.blit(self.crashImage, (self.mainCar.x,self.mainCar.y))
		if self.gameover:
			draw.rect(self.surface, (102,204,102), (0,0,1024,768))

	def HUD(self):
		self.header = draw.rect(self.surface, (0, 197, 247), (0,0,self.surface.get_width(),100))
		self.surface.blit(self.gear.gearImage, (0,0))
		livesLocation = 800
		for i in range(self.lifeCount):
			self.surface.blit(self.lifeImage, (livesLocation, 34))
			livesLocation += 37
		self.surface.blit(self.logo, (self.surface.get_width()//2-(self.logo.get_width()//2),0))
		if not self.gameover:
			self.timer.render()

	def lostLife(self):
		self.lifeCount -= 1

	def shift(self, gear=0, reverse=False):
		self.gear.gear = gear
		self.gear.reverse = reverse
		self.gear.gearImage = image.load("res/gear_"+str(gear)+".png")
		self.mainCar.speed = gear

	def getWall(self):
		return self.walls