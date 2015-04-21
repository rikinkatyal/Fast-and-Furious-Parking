from pygame import *
import time

class Clock():
	def __init__(self, surface, time, x, y):
		self.surface = surface
		self.time = time
		self.x, self.y = x,y
	# def timer(self):
	# 	for t in range(self.time, -1, -1):
	# 		sf = "{:02d}:{:02d}".format(*divmod(t, 60))
	# 		time.sleep(1)