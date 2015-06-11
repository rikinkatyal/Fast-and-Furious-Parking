from pygame import *
from time import time as cTime
from time import strftime, gmtime

class Clock():
	init()
	def __init__(self, surface, time, x, y, timer):
		self.surface = surface
		self.time = time
		self.timer = timer+1
		self.x, self.y = x,y
		self.timeFont = font.Font("res/fonts/pricedown.ttf", 80)
		self.timeLeft = timer
		self.timeEnded = timer

	def render(self):
		self.surface.blit(self.timeFont.render(strftime('%M:%S', gmtime(int(self.timer-(cTime()-self.time))))[1:], 1, (255,255,255)), (170,0))
		self.timeLeft = self.timer-(cTime()-self.time)

	def gameOver(self):
		return self.timeLeft < 0

	def end(self):
		self.timeEnded = self.timeLeft
		self.timeLeft = -1
		return self.timeEnded