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
		self.timeFont = font.SysFont("arial", 50)
		self.timeLeft = timer

	def render(self):
		self.surface.blit(self.timeFont.render(strftime('%M:%S', gmtime(int(self.timer-(cTime()-self.time))))[1:], 1, (255,255,255)), (200,25))
		self.timeLeft = self.timer-(cTime()-self.time)

	def gameOver(self):
		return self.timeLeft < 0