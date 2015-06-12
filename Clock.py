#game timer to count down level

from pygame import *
from time import time as cTime
from time import strftime, gmtime

class Clock():
	#initialize pygame
	init()
	def __init__(self, surface, time, x, y, timer):
		"Set game timer and clock position"
		self.surface = surface
		self.clockTime = time
		self.clockTimer = timer+1
		self.x, self.y = x,y
		self.timeFont = font.Font("res/fonts/pricedown.ttf", 80)
		self.timeLeft = timer
		self.timeEnded = timer

	def render(self):
		"Blit clock to surface"
		self.surface.blit(self.timeFont.render(strftime('%M:%S', gmtime(int(self.clockTimer-(cTime()-self.clockTime))))[1:], 1, (255,255,255)), (170,0))
		self.timeLeft = self.clockTimer-(cTime()-self.clockTime)

	def gameOver(self):
		"Check if time ran out"
		return self.timeLeft < 0

	def end(self):
		"End the clock and return time completed in"
		self.timeEnded = self.timeLeft
		self.timeLeft = -1
		return self.timeEnded