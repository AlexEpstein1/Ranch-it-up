import pygame, math, sys, os
from pygame.locals import *
from random import randint

screen = pygame.display.set_mode((1000, 500))
clock =  pygame.time.Clock()

class BackgroundSprite(pygame.sprite.Sprite):
	
	def __init__(self, position, flip_image=False):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.src_image =  pygame.image.load('RanchBackground.png')
		self.src_image = pygame.transform.scale(self.src_image, (1600,500))
		if flip_image: self.src_image = pygame.transform.flip(self.src_image, True, False)
		self.speed = self.direction = 0

	def update(self, deltat):
		if self.position[0]>= -1100:
			self.position = (self.position[0] - 5, self.position[1])
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
		else:
			self.position = (1600,250)

rect = screen.get_rect()
background1 = BackgroundSprite((800,250))
background2 = BackgroundSprite((2100,250), True)

background_group = pygame.sprite.Group(background1)
background_group.add(background2)

while 1:
	deltat = clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		elif event.key == K_ESCAPE:
			sys.exit(0)
	#RENDERING

	screen.fill((255,255,255))
	background_group.update(deltat)
	background_group.draw(screen)
	pygame.display.flip()
