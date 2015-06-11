from time import time as cTime

from Car import *
from Clock import *
from Gear import *
import Levels
from Wall import *
from Loading import *
from Cone import *
from Park import *
from Popup import *

mixer.init()

class Game():
	def __init__(self,surface):
		# Setup initial surface and variables
		self.curLevel = int(open("files/selected_level.txt").read())
		LevelsMap = {
		1 : Levels.level1Map,
		2 : Levels.level2Map,
		3 : Levels.level3Map,
		4 : Levels.level4Map
		}
		LevelsCar = {
		1 : [],
		2 : [],
		3 : [Car(surface, "res/car4.png", 430, 450, 20), Car(surface, "res/car13.png", 550, 460, 17)],
		4 : [Car(surface, "res/car9.png", 490, 450, -45), Car(surface, "res/car5.png", 700, 330, -45)]
		}
		ParkLoc = {
		1 : Park(surface, 475, 324),
		2 : Park(surface, 240, 260),
		3 : Park(surface, 459, 230),
		4 : Park(surface, 710, 130)
		}
		Times = {
		1 : 30,
		2 : 60,
		3 : 60,
		4 : 75
		}
		self.carImg = open("files/car.txt").read().strip()
		MainCar = {
		1 : Car(surface, self.carImg, surface.get_width()//2,surface.get_height()//2+200,0),
		2 : Car(surface, self.carImg, surface.get_width()//2-50,surface.get_height()//2+300,0),
		3 : Car(surface, self.carImg, 496,surface.get_height()//2+250,0),
		4 : Car(surface, self.carImg, surface.get_width()//2-100,surface.get_height()//2+250,0)
		}
		self.parkSpot = ParkLoc[self.curLevel]
		self.levelTime = Times[self.curLevel]
		self.surface = surface
		self.mainCar = MainCar[self.curLevel]
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

		self.isPause = False
		self.levelComplete = False

		# Level
		for x in range(len(LevelsMap[self.curLevel])):
			for y in range(len(LevelsMap[self.curLevel][x])):
				if LevelsMap[self.curLevel][x][y] == 1:
					self.walls.append(Wall(y*16,x*16+100,self.surface))
				elif LevelsMap[self.curLevel][x][y] == 2:
					self.grasses.append((y*16,x*16+100))
				elif LevelsMap[self.curLevel][x][y] == 3:
					self.cones.append(Wall(y*16,x*16+100,self.surface, True))

		self.wall_y = image.load("res/wall_y.png")
		self.wall_b = image.load("res/wall_b.png")
		self.wall = image.load("res/wall.png")
		self.coneImage = image.load("res/cone.png")

		self.complete = Popup(surface, "Level Complete", ["You completed the level"], False)
		self.fail = Popup(surface, "Level Failed", ["Please try again"], False)

		# settings = open("files/settings.txt").read().split()
		# if settings[0] == "1":
		# 	mixer.music.load("res/audio/background.mp3")
		# 	mixer.music.play(-1)

		self.completedIn = 0
		self.justEnded = False

		self.stars = 0

	def sTime(self, time):
		self.startTime = time
		self.timer = Clock(self.surface, time, 1, 1, self.levelTime)

	def run(self):
		# if self.loading.isLoading():
		# 	self.loading.load()
		self.mx, self.my = mouse.get_pos()
		self.mb = mouse.get_pressed()
		if self.timer.gameOver():
			self.gameover = True
		if self.lifeCount == 0:
			self.gameover = True
		if cTime()-self.startTime > 2:
			self.timeDelay = True
			# mixer.music.load("res/audio/engine.mp3")
			# mixer.music.play(-1)
		self.HUD()
		pressed = key.get_pressed()
		arrows = [pressed[K_UP], pressed[K_DOWN], pressed[K_RIGHT], pressed[K_LEFT]]
		if pressed[K_DOWN] and not self.gameover:
			self.gear.gearImage = image.load("res/gear_r.png")
		elif not self.gameover:
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
			if wall.getBoundRect().colliderect((self.mainCar.x-self.mainCar.boundingRect[2]/2,self.mainCar.y-self.mainCar.boundingRect[3]/2, self.mainCar.carImageRotated.get_rect()[2], self.mainCar.carImageRotated.get_rect()[3])):
				for pt in self.mainCar.outlineRotated:
					if wall.getBoundRect().collidepoint(pt) and self.timeDelay:
						self.crash = True
						self.crashX, self.crashY = int(pt[0]),int(pt[1])
						self.crashObj = wall
		for gr in self.grasses:
			self.surface.blit(self.grass, gr)
		for cone in self.cones:
			cone.render(self.coneImage)
			if cone.getBoundRect().colliderect((self.mainCar.x-self.mainCar.boundingRect[2]/2,self.mainCar.y-self.mainCar.boundingRect[3]/2, self.mainCar.carImageRotated.get_rect()[2], self.mainCar.carImageRotated.get_rect()[3])):
				for pt in self.mainCar.outlineRotated:
					if cone.getBoundRect().collidepoint(pt) and self.timeDelay:
						self.crash = True
						self.crashX, self.crashY = int(pt[0]),int(pt[1])
						self.crashObj = wall

		self.parkSpot.render()
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
			if self.levelComplete:
				self.complete.setText(["Level completed in %s seconds" % str(self.timeLeft)])
				self.complete.render(self.stars)
				if self.curLevel < 15:
					newUnlock = open("files/unlocked_levels.txt").read()
					if int(newUnlock) == self.curLevel:
						newUnlock = str(int(newUnlock)+1)
					f = open("files/unlocked_levels.txt", "w")
					f.write(newUnlock)
					f.close()			
			else:
				self.fail.render(0)

		if self.mainCar.checkPark(self.parkSpot):
			if not self.justEnded:
				self.justEnded = True
				self.timeLeft = int(ceil(self.levelTime - self.timer.end()))
				if self.timeLeft < (self.levelTime/4)*3:
					self.stars = 3
				elif self.timeLeft < self.levelTime/2:
					self.stars = 2
				else:
					self.stars = 1
				coins = int(open("files/coins.txt").read()) + self.stars
				open("files/coins.txt", "w").write(str(coins))
			self.levelComplete = True

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
		# self.surface.blit(self.pauseButton, (940,18))
		# if self.pauseRect.collidepoint((self.mx,self.my)) and self.mb[0]:
		# 	self.pause()
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
		self.isPaused = True