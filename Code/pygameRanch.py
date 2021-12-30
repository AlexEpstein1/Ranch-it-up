import pygame, math, sys, os
from pygame.locals import *
from random import randint

screen = pygame.display.set_mode((1000, 500))
clock =  pygame.time.Clock()

class RanchSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.position = 1000, 300
		self.ranch_images = ['Ranch.png', 'SirachaRanch.png']
		self.src_image =  pygame.image.load(self.ranch_images[randint(0, 1)])
		self.src_image = pygame.transform.scale(self.src_image, (45,75))
		self.speed = self.direction = 0

	def update(self, deltat):
		if self.position[0] >=0:
			self.position = (self.position[0] - 10, self.position[1] - randint(-3,3))
			self.image = pygame.transform.rotate(self.src_image, self.direction)
			self.rect = self.image.get_rect()
			self.rect.center = self.position
			self.position = (1200,300)
		else:
			self.src_image =  pygame.image.load(self.ranch_images[randint(0, 1)])
			self.src_image = pygame.transform.scale(self.src_image, (45,75))

rect = screen.get_rect()
ranch = RanchSprite()
ranch_group = pygame.sprite.Group(ranch)

while 1:
	deltat = clock.tick(30)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		elif event.key == K_ESCAPE:
			sys.exit(0)
	#RENDERING

	screen.fill((255,255,255))
	ranch_group.update(deltat)
	ranch_group.draw(screen)
	pygame.display.flip()