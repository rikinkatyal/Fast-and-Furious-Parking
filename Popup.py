from pygame import *

class Popup():
	init()
	def __init__(self, surface, title, text):
		self.surface = surface
		self.title = title
		self.text = []
		for i in range(len(text)//25):
			self.text.append(text[i*25:i*25+25].strip())
		self.text.append(text[len(text)//25*25:])
		self.bg = image.load("res/popup.png")
		self.x = image.load("res/x.png")
		self.running = False
		self.titleFont = font.Font("res/fonts/pricedown.ttf", 50)
		self.bodyFont = font.Font("res/fonts/pricedown.ttf", 35)

	def render(self):
		self.running = True
		self.surface.blit(self.bg, (self.surface.get_width()//2-self.bg.get_width()//2, self.surface.get_height()//2-self.bg.get_height()//2))
		self.surface.blit(self.x, (self.surface.get_width()//2+self.bg.get_width()//2-self.x.get_width()*1.5, self.surface.get_height()//2-self.bg.get_height()//2))
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		if Rect(self.surface.get_width()//2+self.bg.get_width()//2-self.x.get_width()*1.5, self.surface.get_height()//2-self.bg.get_height()//2,32,32).collidepoint(mx,my) and mb[0]:
			self.running = False
		self.surface.blit(self.titleFont.render(self.title, 1, (0,0,0)), (self.surface.get_width()//2-self.titleFont.size(self.title)[0]//2, self.surface.get_height()//2-self.bg.get_height()//2+15))
		for i in range(len(self.text)):
			self.surface.blit(self.bodyFont.render(self.text[i], 1, (0,0,0)), (self.surface.get_width()//2-self.bodyFont.size(self.text[i])[0]//2, self.surface.get_height()//2-self.bg.get_height()//2+100+i*50))

	def isRunning(self):
		return self.running