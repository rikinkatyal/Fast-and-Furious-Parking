from pygame import *

class Menu():
	init()
	def __init__(self, surface):
		self.surface = surface
		self.bg = transform.scale(image.load("res/main_bg.jpg"), (surface.get_width(), surface.get_height()))
		self.carImage = image.load("res/front_car.png")
		self.carImageSized = transform.scale(self.carImage, (150, 100))
		self.carX, self.carY = 437,290
		self.width = self.carImageSized.get_width()
		self.height = self.carImageSized.get_height()
		self.logo = image.load("res/logo_perspective.png")
		self.running = True
		self.rightMenu = image.load("res/menu_right.png")
		self.rightMenuX, self.rightMenuY = 1024, 768
		self.menuFont = font.Font("res/fonts/pricedown.ttf", 35)
		self.optionColors = [(255,255,255),(255,255,255),(255,255,255),(255,255,255)
		]
		self.optionRects = [Rect(825,465,self.menuFont.size("Start Game")[0]+10,self.menuFont.size("Start Game")[1]),Rect(825,515,self.menuFont.size("Options")[0]+10,self.menuFont.size("Options")[1]),Rect(825,565,self.menuFont.size("Help")[0]+10,self.menuFont.size("Help")[1]),Rect(825,615,self.menuFont.size("About")[0]+10,self.menuFont.size("About")[1])]
		self.options = ["Start Game", "Options", "Help", "About"]
		self.optionResults = [self.notRunning,self.notRunning,self.notRunning,self.notRunning]

		# self.notRunning()

	def render(self):
		mx, my = mouse.get_pos()
		mb = mouse.get_pressed()
		self.pressed = key.get_pressed()
		self.surface.blit(self.bg, (0,0))
		self.width += 16
		self.height += 12
		self.carY += 6
		self.carX -= 8
		self.carImageSized = transform.scale(self.carImage, (self.width, self.height))
		if self.carY > 320:
			self.surface.blit(self.logo, (512-100,380))
		if self.carY < 768:
			self.surface.blit(self.carImageSized, (self.carX, self.carY))
		else:
			if self.pressed[K_SPACE]:
				self.running = False
			self.surface.blit(self.rightMenu, (self.rightMenuX, self.rightMenuY))
			if self.rightMenuX >= 590:
				self.rightMenuX -= 30
			if self.rightMenuY >= 350:
				self.rightMenuY -= 30
			if self.rightMenuX <= 590 and self.rightMenuY <= 350:
				for r in range(len(self.optionRects)):
					# draw.rect(self.surface, (255,255,0), self.optionRects[r])
					if self.optionRects[r].collidepoint((mx,my)):
						self.optionColors[r] = (0,0,0)
						if mb[0]:
							self.optionResults[r]()
					else:
						self.optionColors[r] = (255,255,255)
					self.surface.blit(self.menuFont.render(self.options[r], 1, self.optionColors[r]), (830, 460+(r*50)))
				# self.surface.blit(self.menuFont.render("Start Game", 1, (255,255,255)), (780,370))

	def isRunning(self):
		return self.running

	def notRunning(self):
		self.running = False