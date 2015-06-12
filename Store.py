#store class to buy other cars

from pygame import *
from time import time as cTime

class Store():
	#initialize pygame
	init()
	def __init__(self, surface):
		"load images, fonts, and set starting variables and flags."
		self.surface = surface
		self.bg = transform.scale(image.load("res/store_bg.jpg").convert(), (surface.get_width(),surface.get_height()))
		self.arrow_left = image.load("res/arrow_left.png")
		self.arrow_right = image.load("res/arrow_right.png")
		self.cars = [transform.rotozoom(image.load("res/car%s.png" % i), 1, 2) for i in range(1,19)]
		self.unlocked = open("files/cars_unlocked.txt").read().split("\n")
		self.smallFont = font.Font("res/fonts/pricedown.ttf", 40)
		self.mediumFont = font.Font("res/fonts/pricedown.ttf", 50)
		self.buy = image.load("res/buy.png")
		self.use = image.load("res/use.png")
		self.already = image.load("res/already.png")
		self.prices = open("files/cars_price.txt").read().split("\n")
		self.coins = open("files/coins.txt").read()
		self.coin = image.load("res/coin_medium.png")
		self.coinSmall = image.load("res/coin_small.png")
		self.curCar = 0
		self.running = False
		self.angle = 0
		self.x, self.y = 350,350
		self.errorTime = 0

	def render(self, down):
		"Render store screen"
		self.surface.blit(self.bg, (0,0))
		self.surface.blit(self.arrow_left, (0,0))
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		#back button
		if Rect(0,0,80,80).collidepoint(mx,my) and mb[0]:
			self.running = False
		#move car carousel left
		if self.curCar > 0:
			self.surface.blit(self.arrow_left, (100,344))
			if Rect(100,344,80,80).collidepoint(mx,my) and down:
				self.curCar -= 1
		#move car carousel right
		if self.curCar < len(self.cars)-1:
			self.surface.blit(self.arrow_right, (844, 344))
			if Rect(844,344,80,80).collidepoint(mx,my) and down:
				self.curCar += 1
		#limit exceeding carousel cars
		if self.curCar >= len(self.cars):
			self.curCar = len(self.cars) - 1
		#move car angle for rotation
		self.angle += 1
		self.carImageRotated = transform.rotozoom(self.cars[self.curCar], self.angle, 1)
		self.boundingRect = self.carImageRotated.get_rect()
		self.surface.blit(self.carImageRotated, (self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2))
		#blit rotated car, and if car is unlocked, active, or available for purchase
		if str(self.curCar + 1) in self.unlocked:
			self.surface.blit(self.smallFont.render("Unlocked", 1, (255,255,255)), (550,200))
			if open("files/car.txt").read() == "res/car%s.png" % str(self.curCar + 1):
				self.surface.blit(self.already, (570, 275))
			else:
				self.surface.blit(self.use, (570, 275))
				if Rect(570,275,126,48).collidepoint(mx,my) and down:
					f = open("files/car.txt", "w").write("res/car%s.png" % str(self.curCar + 1))
		else:
			self.surface.blit(self.buy, (570, 275))
			self.surface.blit(self.smallFont.render("Cost: ", 1, (255,255,255)), (550, 350))
			self.surface.blit(self.coinSmall, (660, 360))
			self.surface.blit(self.smallFont.render(self.prices[self.curCar], 1, (255,255,255)), (700, 350))
			if Rect(570,275,126,48).collidepoint(mx,my) and down:
				if int(self.coins) - int(self.prices[self.curCar]) < 0:
					self.errorTime = cTime()
				else:
					self.coins = str(int(self.coins)-int(self.prices[self.curCar]))
					f = open("files/cars_unlocked.txt", "a").write("\n%s" % str(self.curCar+1))
					f = open("files/coins.txt", "w").write(self.coins)
					self.unlocked = open("files/cars_unlocked.txt").read().split("\n")
				
		self.surface.blit(self.coin, (550, 50))
		self.surface.blit(self.mediumFont.render(self.coins, 1, (255,255,255)), (630, 45))

		#error message for not enough coins
		if cTime() - self.errorTime <= 3:
			self.surface.blit(self.smallFont.render("Not Enough Coins!", 1, (255,0,0)), (self.surface.get_width()//2-(font.Font.size(self.smallFont, "Not Enough Coins!")[0])//2, 600))

	def isRunning(self):
		"Check if store is running"
		return self.running