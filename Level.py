#choose level screen

from pygame import *

class Level():
	#initialize pygame
	init()
	def __init__(self, surface):
		"gets surface, loads images, and sets starting flags and variables"
		self.surface = surface
		self.bg = transform.scale(image.load("res/levels_bg.jpg").convert(), (surface.get_width(),surface.get_height()))
		self.button = image.load("res/level_button.png")
		self.button_hover = image.load("res/level_button_hover.png")
		self.star = image.load("res/star.png")
		self.stars = open("files/stars.txt").read().split("\n")
		self.running = False
		self.choseLevel = False
		self.selected_level = open("files/selected_level.txt", "w")
		self.unlocked_level = open("files/unlocked_levels.txt").read()
		self.lock = image.load("res/locked.png")
		self.level_font = font.Font("res/fonts/pricedown.ttf", 80)
		self.arrow_left = image.load("res/arrow_left.png")

	def render(self):
		"Renders level screen"
		self.surface.blit(self.bg, (0,0))
		# self.surface.blit(self.tar, (125,100))
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		self.surface.blit(self.arrow_left, (0,0))
		if Rect(0,0,80,80).collidepoint(mx,my) and mb[0]:
			self.running = False
		y = 184
		#3 rows of levels
		for i in range(3):
			x = 182
			#5 levels in each row
			for j in range(5):
				level = str(i*5+j+1)
				if Rect(x,y,100,100).collidepoint(mx,my):
					self.surface.blit(self.button_hover, (x,y))
					#if click start level
					if mb[0] and int(self.unlocked_level) >= int(level):
						self.running = False
						self.choseLevel = True
						self.selected_level.write(level)
						self.selected_level.close()
				else:
					self.surface.blit(self.button, (x,y))
				self.surface.blit(self.level_font.render(level, 1, (255,255,255)), (x+(100-font.Font.size(self.level_font, level)[0])//2,y-(100-font.Font.size(self.level_font,level)[1])//2))
				starx = x+4
				#blit stars for each level
				for s in range(int(self.stars[int(level)-1])):
					if s == 1:
						self.surface.blit(self.star, (starx, y-20))
					else:
						self.surface.blit(self.star, (starx, y-10))
					starx += 30
				if int(self.unlocked_level) < int(level):
					self.surface.blit(self.lock, (x,y))
				x += 140
			y += 150

	def isRunning(self):
		"Check if level screen is running"
		return self.running