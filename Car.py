from pygame import *
from math import *

import Game

class Car():
	def __init__(self, surface, picture, x, y, angle):
		self.surface = surface
		self.carRect = Rect(0,0,0,0)
		self.speed = 1
		self.curSpeed = 0
		self.carImage = image.load(picture)
		self.carImageRotated = transform.rotozoom(self.carImage, angle, 1)
		self.boundingRect = self.carImageRotated.get_rect()
		self.x = x
		self.y = y
		self.angle = angle
		self.outline = self.getOuter()
		self.lastDirection = ""

	def render(self):
		if self.curSpeed < 0:
			self.curSpeed = 0
		self.carImageRotated = transform.rotozoom(self.carImage, self.angle, 1)
		self.boundingRect = self.carImageRotated.get_rect()
		self.surface.blit(self.carImageRotated, (self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2))
		self.carRect = Rect(self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2,self.boundingRect[2],self.boundingRect[3])

	def drive(self, forward=False, backward=False, right=False, left=False):
		if forward:
			if self.curSpeed < self.speed:
				self.curSpeed += 0.1
			if right:
				self.angle -= self.curSpeed/2
				self.angle += 360
			elif left:
				self.angle += self.curSpeed/2
				if self.angle > 359:
					self.angle -= 360
			self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle+90)
			self.lastDirection = "FORWARD"
		if backward:
			if self.curSpeed < self.speed:
				self.curSpeed += 0.1
			if right:
				self.angle += self.curSpeed/2
				if self.angle > 359:
					self.angle -= 360
			elif left:
				self.angle -= self.curSpeed/2
				if self.angle < 0:
					self.angle += 360
			self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle-90)
			self.lastDirection = "REVERSE"
		else:
			if self.curSpeed > 0:
				self.curSpeed -= self.speed*0.01
				if self.lastDirection == "FORWARD":
					if right:
						self.angle -= self.curSpeed/2
						self.angle += 360
					elif left:
						self.angle += self.curSpeed/2
						if self.angle > 359:
							self.angle -= 360
					self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle+90)
				elif self.lastDirection == "REVERSE":
					if right:
						self.angle += self.curSpeed/2
						if self.angle > 359:
							self.angle -= 360
					elif left:
						self.angle -= self.curSpeed/2
						if self.angle < 0:
							self.angle += 360
					self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle-90)

	def point(self,x,y,size,ang):
		dx = cos(radians(ang))
		dy = sin(radians(ang))
		return (x+dx*size,y-dy*size)

	def collision(self):
		Game.lostLife()

	def brake(self):
		if self.curSpeed > 0:
			self.curSpeed -= self.speed*0.05

	def getOuter(self):
		points = []
		for x in range(1, self.carImageRotated.get_width()-1):
			for y in range(1, self.carImageRotated.get_height()-1):
				if self.carImageRotated.get_at((x,y))[3] >= 10 and 0 in [self.carImageRotated.get_at((x-1,y-1))[3],self.carImageRotated.get_at((x,y-1))[3],self.carImageRotated.get_at((x+1,y-1))[3],self.carImageRotated.get_at((x+1,y))[3],self.carImageRotated.get_at((x+1,y+1))[3],self.carImageRotated.get_at((x,y+1))[3],self.carImageRotated.get_at((x-1,y+1))[3],self.carImageRotated.get_at((x-1,y))[3]] or ((y == 1 or y == self.carImageRotated.get_height()-2) and self.carImageRotated.get_at((x,y))[3] >= 10):
					points.append((x+int(self.x-self.boundingRect[2]/2),y+int(self.y-self.boundingRect[3]/2)))
		return (points)

	def getPt(self):
		return self.outline

	def getBoundRect(self):
		return Rect(self.x-(self.carImageRotated.get_width()//2), self.y-(self.carImageRotated.get_height()//2), self.carImageRotated.get_width(), self.carImageRotated.get_height())

	def xy2vect(x,y):
		mag = hypot(x,y)
		ang = atan2(y,x)
		return mag, ang

	def vect2xy(mag, ang):
		return cos(ang)*mag, sin(ang)*mag

	def rotatePoint(self, x, y, px, py, ang, size):
		dx, dy = px-x, py-y
		curAng, mag = self.xy2vect(dx,dy)
		curAng += ang
		dx, dy = self.vect2xy(curAng, mag)
		return x+dx*size, y+dy*size