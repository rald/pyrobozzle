#!/usr/bin/env python3

import pygame
import math

import canvas
import player
import star	
import palette

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init() 

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("robozzle")
programIcon = pygame.image.load('images/star.png')
pygame.display.set_icon(programIcon)


ship=player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
star=star.Star(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,12)

sprite=canvas.Canvas("sprite-00.cvs")

move_sfx = pygame.mixer.Sound("sounds/move.wav")

# Game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			elif event.key == pygame.K_UP:
				if ship.move_count==0:
					#pygame.mixer.Sound.play(move_sfx)
					ship.state = player.State.MOVE_FORWARD
			elif event.key == pygame.K_LEFT:
				if ship.move_count==0:
					#pygame.mixer.Sound.play(move_sfx)
					ship.state = player.State.TURN_LEFT
			elif event.key == pygame.K_RIGHT:
				if ship.move_count==0:
					#pygame.mixer.Sound.play(move_sfx)
					ship.state = player.State.TURN_RIGHT

	screen.fill((0,0,0))
	"""
	pygame.draw.rect(screen,(0,0,255),[SCREEN_WIDTH/2-16,SCREEN_HEIGHT/2-16,32,32])
	pygame.draw.rect(screen,(255,255,255),[SCREEN_WIDTH/2-16,SCREEN_HEIGHT/2-16,32,32],1)
		
	pygame.draw.rect(screen,palette.palette[0x02],pygame.Rect(0*32,0,32,32))
	pygame.draw.rect(screen,palette.palette[0x06],pygame.Rect(1*32,0,32,32))
	pygame.draw.rect(screen,palette.palette[0x09],pygame.Rect(2*32,0,32,32))

	for j in range(10):
		for i in range(10):
			pygame.draw.rect(screen,palette.palette[12],[i*32,j*32,32,32],1)
				
	for i in range(sprite.f):
		sprite.draw(screen,i*sprite.w*4+8,8,i,2)	
	"""
		
	star.draw(screen)

	ship.draw(screen)
	ship.update()
			
	pygame.display.update()

# Quit Pygame
pygame.quit()

