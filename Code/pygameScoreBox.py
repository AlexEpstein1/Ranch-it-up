import pygame, sys
from pygame.locals import *


class Score(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 15)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((255,255,255))
        pygame.display.update()

    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (0,0,0), (445, 0, 598, 45), 2)
        pygame.display.update()

    def update_text(self):
        self.screen.blit(self.font.render('Ranch Collected: <NUM_RANCH>', True, (255,0,0)), (450, 22))
        pygame.display.update()

score = Score()
score.addRect()
score.update_text()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();


