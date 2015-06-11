from pygame import *

class Popup():
	init()
	def __init__(self, surface, title, text, x=True):
		self.surface = surface
		self.title = title
		self.text = text
		# for i in range(len(text)//35):
		# 	self.text.append(text[i*35:i*35+35].strip())
		# self.text.append(text[len(text)//35*35:])
		self.bg = image.load("res/popup.png")
		self.x = image.load("res/x.png")
		self.hasX = x
		self.running = False
		self.titleFont = font.Font("res/fonts/pricedown.ttf", 40)
		self.bodyFont = font.Font("res/fonts/pricedown.ttf", 27)
		self.hasImage = False
		self.imageFile = []
		self.imageLoc = []

	def render(self, stars=0):
		self.running = True
		self.surface.blit(self.bg, (self.surface.get_width()//2-self.bg.get_width()//2, self.surface.get_height()//2-self.bg.get_height()//2))
		if self.hasX:
			self.surface.blit(self.x, (self.surface.get_width()//2+self.bg.get_width()//2-self.x.get_width()*1.5, self.surface.get_height()//2-self.bg.get_height()//2))
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		if Rect(self.surface.get_width()//2+self.bg.get_width()//2-self.x.get_width()*1.5, self.surface.get_height()//2-self.bg.get_height()//2,32,32).collidepoint(mx,my) and mb[0]:
			self.running = False
		self.surface.blit(self.titleFont.render(self.title, 1, (0,0,0)), (self.surface.get_width()//2-self.titleFont.size(self.title)[0]//2, self.surface.get_height()//2-self.bg.get_height()//2+15))
		for i in range(len(self.text)):
			self.surface.blit(self.bodyFont.render(self.text[i], 1, (0,0,0)), (self.surface.get_width()//2-self.bodyFont.size(self.text[i])[0]//2, self.surface.get_height()//2-self.bg.get_height()//2+75+i*35))
		if self.hasImage:
			for img in range(len(self.imageFile)):
				self.surface.blit(self.imageFile[img], self.imageLoc[img])
		self.stars(stars)

	def isRunning(self):
		return self.running

	def images(self, imgs, locs):
		self.hasImage = True
		self.imageFile = imgs
		self.imageLoc = locs

	def setText(self, text):
		self.text = text

	def stars(self, stars):
		star = image.load("res/star_large.png")
		x, y = 422, 140
		for i in range(stars):
			if i == 1:
				self.surface.blit(star, (x,y-20))
			else:
				self.surface.blit(star, (x,y))
			x += 60