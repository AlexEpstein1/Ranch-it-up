import pygame, math, sys
from pygame.locals import *

surface = pygame.Surface((100, 100))
image = pygame.image.load("nicholas.jpg")
screen = pygame.display.set_mode((400, 300))

while True:
	screen.blit(image, (0, 0))
	pygame.display.flip()