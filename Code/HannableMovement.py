import pygame, math, sys, os
from pygame.locals import *
from random import randint

screen = pygame.display.set_mode((1024, 768))
clock =  pygame.time.Clock()

class CopSprite(pygame.sprite.Sprite):
	MAX_SPEED =  10
	
	def __init__(self, image, position):
		pygame.sprite.Sprite.__init__(self)
		self.position = position
		self.src_image =  pygame.image.load(image)
		self.src_image = pygame.transform.scale(self.src_image, (75,105))
		self.speed = self.direction = 0

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - 10, self.position[1] + randint(0, 1 ))
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
		else:
			self.position = (1100,600)

rect = screen.get_rect()
cop = CopSprite('HannableCop.png', (1100, 600))
cop_group = pygame.sprite.Group(cop)

while 1:
	deltat = clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		elif event.key == K_ESCAPE:
			sys.exit(0)
	#RENDERING

	screen.fill((255,255,255))
	cop_group.update(deltat)
	cop_group.draw(screen)
	pygame.display.flip()


	

