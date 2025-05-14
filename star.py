import pygame
import math

import palette

class Star:
	def __init__(self,center_x,center_y,radius):
		self.center_x = center_x
		self.center_y = center_y
		self.radius = radius
		self.points = []
		# Number of star points (outer + inner)
		self.num_points = 10
		# Inner radius is about 3/8 of outer radius for nice star shape
		self.inner_radius = self.radius * 3 / 8
		self.angle = math.pi / 2  # Start at top (90 degrees)

		for i in range(self.num_points):
		    r = self.radius if i % 2 == 0 else self.inner_radius
		    x = self.center_x + r * math.cos(self.angle)
		    y = self.center_y - r * math.sin(self.angle)  # Pygame y-axis goes down, so subtract
		    self.points.append((x, y))
		    self.angle += math.pi / 5  # 36 degrees per point step (360/10)
                 
	def draw(self,screen):
		pygame.draw.polygon(screen,palette.sweetie[0x05],self.points)
		pygame.draw.polygon(screen,palette.sweetie[0x0C],self.points,1)

