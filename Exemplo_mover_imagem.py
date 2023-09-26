image_filename = 'boxe.png'
image_filename2 = 'chuteshaolim.png'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mover Imagem")
img = pygame.image.load(image_filename)
img = pygame.transform.scale(img, (300,300))
img2 = pygame.image.load(image_filename2)
img2 = pygame.transform.scale(img2, (300,300))

x = 300
h = -600
while True:
   screen.fill((255,255,255))
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
   screen.blit(img, (x, 100))
   screen.blit(img2, (-h, 100))
   x= x+0.1
   h+= 0.1

   if x > 200:
      x = x-200

   if h > 300:
      h = h-100
   pygame.display.update()