import pygame,sys
from pygame.locals import *

'''
CORES EM RGB :
'black': (0, 0, 0, 255)
'blue': (0, 0, 255, 255),
'cyan': (0, 255, 255, 255),
'gold': (255, 215, 0, 255),
'gray': (190, 190, 190, 255),
'green': (0, 255, 0, 255),
'orange': (255, 165, 0, 255),
'purple': (160, 32, 240, 255),
'red': (255, 0, 0, 255),
'violet': (238, 130, 238, 255)
'yellow': (255, 255, 0, 255),
'white': (255, 255, 255, 255)
'''

'''
TIPOS DE EVENTOS

QUIT	None
ACTIVEEVENT	gain, state
KEYDOWN	unicode, key, mod
KEYUP	key, mod
MOUSEMOTION	pos, rel, buttons
MOUSEBUTTONUP	pos, button
MOUSEBUTTONDOWN	pos, button
JOYAXISMOTION	joy, axis, value
JOYBALLMOTION	joy, ball, rel
JOYHATMOTION	joy, hat, value
JOYBUTTONUP	joy, button
JOYBUTTONDOWN	joy, button
VIDEORESIZE	size, w, h
VIDEOEXPOSE	None
USEREVENT	Code

'''

pygame.init()
canvas=pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello")
canvas.fill((0,0,0))
while True:
   for event in pygame.event.get():
      if(event.type == QUIT):
         pygame.quit()
         sys.exit(1)