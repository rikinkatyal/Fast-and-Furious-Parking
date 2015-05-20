from pygame import *

class Level():
	def __init__(self, surface):
		self.surface = surface
		self.bg = transform.scale(image.load("res/levels_bg.jpg"), (surface.get_width(),surface.get_height()))
		self.button = image.load("res/level_button.png")
		self.button_hover = image.load("res/level_button_hover.png")
		self.star = image.load("res/star.png")
		self.stars = open("files/stars.txt").read().split("\n")
		self.running = True
		self.selected_level = open("files/selected_level.txt", "w")

	def render(self):
		self.surface.blit(self.bg, (0,0))
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		y = 184
		for i in range(3):
			x = 182
			for j in range(5):
				level = str(i*5+j+1)
				if Rect(x,y,100,100).collidepoint(mx,my):
					self.surface.blit(self.button_hover, (x,y))
					if mb[0]:
						self.running = False
						self.selected_level.write(level)
						self.selected_level.close()
				else:
					self.surface.blit(self.button, (x,y))
				starx = x+4
				for s in range(int(self.stars[int(level)-1])):
					if s == 1:
						self.surface.blit(self.star, (starx, y-20))
					else:
						self.surface.blit(self.star, (starx, y-10))
					starx += 30
				x += 140
			y += 150

	def isRunning(self):
		return self.running