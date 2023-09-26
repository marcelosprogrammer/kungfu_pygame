filename = 'girl2.png'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Moving with mouse")
img = pygame.image.load(filename)
x = 0
y= 150
while True:
   mx,my=pygame.mouse.get_pos()
   screen.fill((255,255,255))
   screen.blit(img, (mx, my))
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
   pygame.display.update()