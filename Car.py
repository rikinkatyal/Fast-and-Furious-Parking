#car class that has driving physics, parking, and car collision

from pygame import *
from math import *

class Car():
	def __init__(self, surface, picture, x, y, angle):
		"Initialize all variables and set car image, location, and angle"
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
		self.outlineRotated = self.outline[:]
		self.lastDirection = ""
		self.brakeSound = mixer.Sound("res/audio/ebrake.ogg")

	def render(self):
		"Blits everything on surface"
		if self.curSpeed < 0:
			self.curSpeed = 0
		self.carImageRotated = transform.rotozoom(self.carImage, self.angle, 1)
		self.boundingRect = self.carImageRotated.get_rect()
		self.surface.blit(self.carImageRotated, (self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2))
		self.carRect = Rect(self.x-self.boundingRect[2]/2,self.y-self.boundingRect[3]/2,self.boundingRect[2],self.boundingRect[3])

	def drive(self, forward=False, backward=False, right=False, left=False):
		"Moves car based on arrow or WASD keys (direction)"
		if forward:
			#moves car forward
			if self.lastDirection == "REVERSE" and self.curSpeed > 0:
				self.curSpeed -= 0.25
			else:
				if self.curSpeed < self.speed:
					self.curSpeed += 0.1
				if right:
					self.angle -= self.curSpeed/2
				elif left:
					self.angle += self.curSpeed/2
				self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle+90)
				for pt in range(len(self.outline)):
					self.outline[pt] = self.point(self.outline[pt][0], self.outline[pt][1], self.curSpeed, self.angle+90)
					self.outlineRotated[pt] = self.rotatePoint(self.x, self.y, self.outline[pt][0], self.outline[pt][1], self.angle, 1)
				self.lastDirection = "FORWARD"
		elif backward:
			#moves car in reverse
			if self.lastDirection == "FORWARD" and self.curSpeed > 0:
				self.curSpeed -= 0.25
			else:
				if self.curSpeed < self.speed:
					self.curSpeed += 0.1
				if right:
					self.angle += self.curSpeed/2
				elif left:
					self.angle -= self.curSpeed/2
				self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle-90)
				for pt in range(len(self.outlineRotated)):
					self.outline[pt] = self.point(self.outline[pt][0], self.outline[pt][1], self.curSpeed, self.angle-90)
					self.outlineRotated[pt] = self.rotatePoint(self.x, self.y, self.outline[pt][0], self.outline[pt][1], self.angle, 1)
				self.lastDirection = "REVERSE"
		else:
			#brings car to slow stop
			if self.curSpeed > 0:
				self.curSpeed -= self.speed*0.025
				if self.lastDirection == "FORWARD":
					if right:
						self.angle -= self.curSpeed/2
					elif left:
						self.angle += self.curSpeed/2
					self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle+90)
					for pt in range(len(self.outline)):
						self.outline[pt] = self.point(self.outline[pt][0], self.outline[pt][1], self.curSpeed, self.angle+90)
						self.outlineRotated[pt] = self.rotatePoint(self.x, self.y, self.outline[pt][0], self.outline[pt][1], self.angle, 1)
				elif self.lastDirection == "REVERSE":
					if right:
						self.angle += self.curSpeed/2
					elif left:
						self.angle -= self.curSpeed/2
					self.x,self.y = self.point(self.x,self.y,self.curSpeed,self.angle-90)
					for pt in range(len(self.outline)):
						self.outline[pt] = self.point(self.outline[pt][0], self.outline[pt][1], self.curSpeed, self.angle-90)
						self.outlineRotated[pt] = self.rotatePoint(self.x, self.y, self.outline[pt][0], self.outline[pt][1], self.angle, 1)
	def point(self,x,y,size,ang):
		"Calculate point based on angle, starting point, and distance"
		dx = cos(radians(ang))
		dy = sin(radians(ang))
		return (x+dx*size,y-dy*size)

	def brake(self):
		"Stops the car, but not immediately"
		if self.curSpeed > 0:
			self.curSpeed -= self.speed*0.05
			self.brakeSound.play()
		else:
			self.brakeSound.stop()

	def crashed(self, carObj, pt):
		"When car crashes, it goes back in opposite direction"
		if self.lastDirection == "FORWARD":
			self.lastDirection = "REVERSE"
		elif self.lastDirection == "REVERSE":
			self.lastDirection = "FORWARD"
		if self.curSpeed > 1:
			self.curSpeed = self.curSpeed*0.5
		else:
			self.curSpeed = self.curSpeed*0.75

	def getOuter(self):
		"Gets points on car outline"
		points = []
		for x in range(1, self.carImageRotated.get_width()-1):
			for y in range(1, self.carImageRotated.get_height()-1):
				if self.carImageRotated.get_at((x,y))[3] >= 10 and 0 in [self.carImageRotated.get_at((x-1,y-1))[3],self.carImageRotated.get_at((x,y-1))[3],self.carImageRotated.get_at((x+1,y-1))[3],self.carImageRotated.get_at((x+1,y))[3],self.carImageRotated.get_at((x+1,y+1))[3],self.carImageRotated.get_at((x,y+1))[3],self.carImageRotated.get_at((x-1,y+1))[3],self.carImageRotated.get_at((x-1,y))[3]] or ((y == 1 or y == self.carImageRotated.get_height()-2) and self.carImageRotated.get_at((x,y))[3] >= 10) or ((x == 1 or x == self.carImageRotated.get_width()-2) and self.carImageRotated.get_at((x,y))[3] >= 10):
					points.append((x+int(self.x-self.boundingRect[2]/2),y+int(self.y-self.boundingRect[3]/2)))
		return (points)

	def getPt(self):
		"Returns the outline"
		return self.outline

	def getBoundRect(self):
		"Gets Rect object that surrounds car, including it rotated"
		return Rect(self.x-self.carImageRotated.get_width(), self.y-(self.carImageRotated.get_height()//2), self.carImageRotated.get_width(), self.carImageRotated.get_height())

	def xy2vect(self,x,y):
		"Converts a point to a vector with magnitude and angle"
		mag = hypot(x,y)
		ang = degrees(atan2(y,x))
		return mag, ang

	def vect2xy(self, ang, mag):
		"Converts a vector to a point using angle and magnitude"
		return cos(radians(ang))*mag, sin(radians(ang))*mag

	def rotatePoint(self, x, y, px, py, ang, size):
		"Rotates a point from an origin by converting to vector, then back to point"
		dx, dy = px-x, py-y
		mag, curAng = self.xy2vect(dx,dy)
		curAng -= ang
		dx, dy = self.vect2xy(curAng, mag)
		return int((x+dx)*size), int((y+dy)*size)

	def checkPark(self, park):
		"Checks if car is parked in parking spot by passing in Park object"
		point1 = self.rotatePoint(self.x, self.y, int(self.x), int(self.y - self.carImage.get_height()/2.5), self.angle, 1)
		point2 = self.rotatePoint(self.x, self.y, int(self.x), int(self.y + self.carImage.get_height()/2.5), self.angle, 1)
		return park.rect.collidepoint(point1) and park.rect.collidepoint(point2)