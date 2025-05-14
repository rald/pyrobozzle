import pygame
import math

import palette

from enum import Enum



class State(Enum):
	IDLE         = 0
	MOVE_FORWARD = 1,
	TURN_LEFT    = 2,
	TURN_RIGHT   = 3

class Direction(Enum):
	UP    = 0,
	DOWN  = 1,
	LEFT  = 2,
	RIGHT = 3
	
class Player:

	D2R = math.pi / 180.0

	SPEED = 2
	
	SHIP_SIZE = 7
	
	ship=[
		[ 0, 0],
		[ 1, 1],
		[ 0,-2],
		[-1, 1],
		[ 0, 0]
	]

	move_count = 0

	state=State.IDLE
	
	direction=Direction.UP
	
	angle = 0
	
	speed = 1

	def __init__(self,x,y):
		self.x=x
		self.y=y

	def draw(self,screen):
		ship=[]

		for i in range(len(self.ship)):
			ship.append([self.ship[i][0]*Player.SHIP_SIZE+self.x,self.ship[i][1]*Player.SHIP_SIZE+self.y])

		for i in range(len(ship)):
			ship[i]=Player.rotate((self.x,self.y),ship[i],self.angle)
			
		pygame.draw.polygon(screen,palette.sweetie[0x02],ship)
		pygame.draw.polygon(screen,palette.sweetie[0x0C],ship,1)		

	def update(self):
		if self.state==State.IDLE:
			pass
		elif self.state==State.MOVE_FORWARD:
			if self.move_count==0:
				self.move_count=32/self.speed
			else:
				self.move_forward()
		elif self.state==State.TURN_LEFT:
			if self.move_count==0:
				self.move_count=90/self.speed
			else:
				self.turn_left()
		elif self.state==State.TURN_RIGHT:
			if self.move_count==0:
				self.move_count=90/self.speed
			else:
				self.turn_right()
		
	@staticmethod
	def rotate(origin, point, angle):
		ox, oy = origin
		px, py = point
		qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
		qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
		return qx, qy

	def move_forward(self):
		if self.direction==Direction.UP:
			self.y-=self.speed
		elif self.direction==Direction.DOWN:
			self.y+=self.speed
		elif self.direction==Direction.LEFT:
			self.x-=self.speed
		elif self.direction==Direction.RIGHT:
			self.x+=self.speed
			
		self.move_count -= 1
		if self.move_count <= 0:
			self.move_count = 0
			self.state=State.IDLE
		
	def turn_left(self):
		self.angle-=self.speed*Player.D2R
	
		self.move_count -= 1
		if self.move_count <= 0:
			self.move_count = 0
			if self.direction==Direction.UP:
				self.direction=Direction.LEFT
			elif self.direction==Direction.DOWN:
				self.direction=Direction.RIGHT
			elif self.direction==Direction.LEFT:
				self.direction=Direction.DOWN
			elif self.direction==Direction.RIGHT:
				self.direction=Direction.UP
			self.state=State.IDLE
			
	def turn_right(self):
		self.angle+=self.speed*Player.D2R
	
		self.move_count -= 1
		if self.move_count <= 0:
			self.move_count = 0
			if self.direction==Direction.UP:
				self.direction=Direction.RIGHT
			elif self.direction==Direction.DOWN:
				self.direction=Direction.LEFT
			elif self.direction==Direction.LEFT:
				self.direction=Direction.UP
			elif self.direction==Direction.RIGHT:
				self.direction=Direction.DOWN
			self.state=State.IDLE

