image_filename = 'girl1.png'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Movendo imagem com o teclado númerico")
img = pygame.image.load(image_filename)
x = 0
y= 150
while True:
   screen.fill((255,255,255))
   screen.blit(img, (x, y))
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == KEYDOWN:
         if event.key == K_KP6:
            x= x+5
         if event.key == K_KP4:
            x=x-5
         if event.key == K_KP8:
            y=y-5
         if event.key == K_KP2:
            y=y+5
         if event.key == K_KP7:
            x=x-5
            y=y-5
         if event.key == K_KP9:
            x=x+5
            y=y-5
         if event.key == K_KP3:
            x=x+5
            y=y+5
         if event.key == K_KP1:
            x=x-5
            y=y+5
   pygame.display.update()