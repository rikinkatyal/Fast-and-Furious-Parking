from pygame import *
from math import *
from time import time as cTime

from Car import *
from Clock import *
from Gear import *
import Levels
from Wall import *
from Loading import *
from Cone import *

mixer.init()

class Game():
	def __init__(self,surface):
		# Setup initial surface and variables
		self.curLevel = int(open("files/selected_level.txt").read())
		LevelsMap = {
		1: Levels.level1Map
		}
		LevelsCar = {
		# 1: [Car(surface, "res/car17.png", 400, 300, 86), Car(surface, "res/car12.png", 800,600, 0), Car(surface, "res/car1.png", 100, 365, 100), Car(surface, "res/car10.png", 100, 465, 107)]
		1 : []
		}
		# LevelsCar = {1:Car(surface, "res/car17.png", 400, 300, 86)}
		self.surface = surface
		self.carImg = open("files/car.txt").read().strip()
		self.mainCar = Car(self.surface, self.carImg, surface.get_width()//2,surface.get_height()//2+200,00)
		mixer.music.load("res/audio/start.mp3")
		mixer.music.play(0)
		# mixer.music.load("res/audio/engine.mp3")
		# mixer.music.play(-1)
		self.lifeCount = 5
		self.lifeImage = image.load("res/life.png")

		self.coin_count = open("files/coins.txt").read()
		self.coin_image = image.load("res/coin_small.png")
		self.coin_font = font.Font("res/fonts/pricedown.ttf", 32)

		self.logo = image.load("res/logo_main.png")
		self.startTime = 0
		self.timeDelay = False

		self.gameover = False
		
		self.crash = False
		self.crashImage = image.load("res/crash.png")
		self.crashX, self.crashY = 0,0
		self.crashTime = 0
		self.crashObj = Game

		self.gear = Gear()

		self.boundRect = Rect(0,100,surface.get_width(),surface.get_height()-100)

		self.walls = []
		self.grasses = []
		self.cones = []

		self.carObsctacles = LevelsCar[self.curLevel]

		self.grass = image.load("res/grass.png")

		self.timer = Clock(surface, cTime, 1, 1, 0)

		self.pauseButton = image.load("res/pause.png")
		self.pauseRect = Rect(940,18,64,64)
		# self.loading = Loading(self.surface, cTime(), 5)

		# Level
		for x in range(len(LevelsMap[self.curLevel])):
			for y in range(len(LevelsMap[self.curLevel][x])):
				if LevelsMap[self.curLevel][x][y] == 1:
					self.walls.append(Wall(y*16,x*16+100,self.surface))
				elif LevelsMap[self.curLevel][x][y] == 2:
					self.grasses.append((y*16,x*16+100))
				elif LevelsMap[self.curLevel][x][y] == 3:
					self.cones.append(Cone(self.surface, y*16,x*16+100))

		self.wall_y = image.load("res/wall_y.png")
		self.wall_b = image.load("res/wall_b.png")
		self.wall = image.load("res/wall.png")

	def sTime(self, time):
		self.startTime = time
		self.timer = Clock(self.surface, time, 1, 1, 120)

	def run(self):
		# if self.loading.isLoading():
		# 	self.loading.load()
		self.mx, self.my = mouse.get_pos()
		self.mb = mouse.get_pressed()
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
		# draw.rect(self.surface, (0,255,0), (self.mainCar.x-self.mainCar.boundingRect[2]/2,self.mainCar.y-self.mainCar.boundingRect[3]/2, self.mainCar.carImageRotated.get_rect()[2], self.mainCar.carImageRotated.get_rect()[3]))
		for car in self.carObsctacles:
			# draw.rect(self.surface, (0,255,0), (car.x-car.boundingRect[2]/2,car.y-car.boundingRect[3]/2, car.boundingRect[2], car.boundingRect[3]))
			# for pt in car.outlineRotated:
			# 	self.surface.set_at((int(pt[0]),int(pt[1])), (255,255,255))
			# for pt in self.mainCar.outlineRotated:
			# 	self.surface.set_at((int(pt[0]),int(pt[1])), (255,255,255))
			if Rect((car.x-car.boundingRect[2]/2,car.y-car.boundingRect[3]/2, car.boundingRect[2], car.boundingRect[3])).colliderect(Rect(self.mainCar.x-self.mainCar.boundingRect[2]/2,self.mainCar.y-self.mainCar.boundingRect[3]/2, self.mainCar.carImageRotated.get_rect()[2], self.mainCar.carImageRotated.get_rect()[3])):
				for pt in self.mainCar.outlineRotated:
					if (int(pt[0]),int(pt[1])) in car.outlineRotated and self.timeDelay:
						self.crash = True
						self.crashX, self.crashY = int(pt[0]),int(pt[1])
						self.crashObj = car
			car.render()

		yellow = False
		for wall in self.walls:
			if yellow:
				wall.render(self.wall_y)
				yellow = False
			else:
				wall.render(self.wall_b)
				yellow = True
			# wall.render(self.wall)
			if wall.getBoundRect().colliderect((self.mainCar.x-self.mainCar.boundingRect[2]/2,self.mainCar.y-self.mainCar.boundingRect[3]/2, self.mainCar.carImageRotated.get_rect()[2], self.mainCar.carImageRotated.get_rect()[3])):
				for pt in self.mainCar.outlineRotated:
					if wall.getBoundRect().collidepoint(pt) and self.timeDelay:
						self.crash = True
						self.crashX, self.crashY = int(pt[0]),int(pt[1])
						self.crashObj = Wall
		for gr in self.grasses:
			self.surface.blit(self.grass, gr)
		for co in self.cones:
			co.render()

		self.mainCar.render()

		if self.crash:
			self.surface.blit(self.crashImage, (self.crashX-40,self.crashY-34))
			self.crash = False
			self.mainCar.crashed(self.crashObj, (self.crashX, self.crashY))
			self.lostLife()
			self.crashTime = cTime()
			self.timeDelay = False
			self.startTime = cTime()
			if self.lifeCount > 0:
				mixer.music.load("res/audio/start.mp3")
				mixer.music.play(0)
		if self.gameover:
			draw.rect(self.surface, (102,204,102), (0,0,1024,768))

	def HUD(self):
		self.header = draw.rect(self.surface, (51, 153, 255), (0,0,self.surface.get_width(),100))
		self.surface.blit(self.gear.gearImage, (0,0))
		livesLocation = 750
		for i in range(self.lifeCount):
			self.surface.blit(self.lifeImage, (livesLocation, 34))
			livesLocation += 37
		self.surface.blit(self.logo, (self.surface.get_width()//2-(self.logo.get_width()//2),13))
		if not self.gameover:
			self.timer.render()
		self.surface.blit(self.pauseButton, (940,18))
		if self.pauseRect.collidepoint((self.mx,self.my)) and self.mb[0]:
			self.pause()
		self.surface.blit(self.coin_image, (615,34))
		self.surface.blit(self.coin_font.render(self.coin_count, 1, (255,255,255)), (650,28))

	def lostLife(self):
		self.lifeCount -= 1

	def shift(self, gear=0, reverse=False):
		self.gear.gear = gear
		self.gear.reverse = reverse
		self.gear.gearImage = image.load("res/gear_"+str(gear)+".png")
		self.mainCar.speed = gear

	def getWall(self):
		return self.walls

	def pause(self):
		print("pause")