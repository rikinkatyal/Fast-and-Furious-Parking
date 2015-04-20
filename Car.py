from pygame import *
from math import *

import Game

class Car():
	speed = 1
	def __init__(self, surface):
		self.surface = surface
		self.boundRect = Rect(0,100,surface.get_width(),surface.get_height()-100)
		self.carRect = Rect(0,0,0,0)

	def setCar(self, picture):
		self.carImage = image.load(picture)
		self.carImageRotated = self.carImage

	def setLocation(self, x, y, angle):
		self.x = x
		self.y = y
		self.angle = angle

	def show(self):
		# draw.rect(self.surface,(0,0,0),self.carRect)
		self.carImageRotated = transform.rotozoom(self.carImage, self.angle, 1)
		self.boundingRect = self.carImageRotated.get_rect()
		self.surface.blit(self.carImageRotated, (self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2))
		self.carRect = Rect(self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2,self.boundingRect[2],self.boundingRect[3])

	def drive(self, forward=False, backward=False, right=False, left=False):
		if forward:
			if right:
				self.angle -= self.speed/2
				self.angle += 360
			elif left:
				self.angle += self.speed/2
				if self.angle > 359:
					self.angle -= 360
			self.x,self.y = self.point(self.x,self.y,self.speed,self.angle+90)
		elif backward:
			if right:
				self.angle += self.speed/2
				if self.angle > 359:
					self.angle -= 360
			elif left:
				self.angle -= self.speed/2
				if self.angle < 0:
					self.angle += 360
			self.x,self.y = self.point(self.x,self.y,self.speed,self.angle-90)

	def point(self,x,y,size,ang):
		dx = cos(radians(ang))
		dy = sin(radians(ang))
		return (x+dx*self.speed,y-dy*self.speed)

	def collision(self):
		Game.lostLife()