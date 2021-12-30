import pygame, math, sys
from pygame.locals import *

screen = pygame.display.set_mode((1000, 500))

class EricSprite(pygame.sprite.Sprite):
	MOVEMENT_SPEED = 5
	MAX_HEIGHT = 20

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.pos_x = 10
		self.pos_y = 300
		self.position = self.pos_x, self.pos_y
		self.src_image = pygame.image.load("../Sprites/EricHorse–Standing.png")
		self.src_image = pygame.transform.scale(self.src_image, (100, 105))
		self.speed = self.MOVEMENT_SPEED

	def move_left(self):
		self.pos_x -= self.MOVEMENT_SPEED
		self.position = self.pos_x, self.pos_y

	def move_right(self):
		self.pos_x += self.MOVEMENT_SPEED
		self.position = self.pos_x, self.pos_y

pygame.display.set_caption('Ranch It UP')
eric = EricSprite()
screen.fill((255, 255, 255))
screen.blit(eric.src_image, eric.position)
pygame.display.flip()

while 1:
	for event in pygame.event.get():
	# # 	print(event)
		if not hasattr(event, 'key'): continue
	# 	if event.key == K_RIGHT:
	# 		eric.move_right()
	# 	elif event.key == K_LEFT:
	# 		eric.move_left()
	# 	elif event.key == K_ESCAPE:
	# 		sys.exit()

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		eric.move_left()
	elif key[pygame.K_RIGHT]:
		eric.move_right()
	elif key[pygame.K_ESCAPE]:
		sys.exit()

	print(eric.pos_x)
	#RENDERING
	screen.fill((255, 255, 255))
	screen.blit(eric.src_image, eric.position)
	pygame.display.flip()

