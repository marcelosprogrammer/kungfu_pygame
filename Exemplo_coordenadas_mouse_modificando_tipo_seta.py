import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))

'''
pygame.SYSTEM_CURSOR_ARROW	arrow
pygame.SYSTEM_CURSOR_IBEAM	i-beam
pygame.SYSTEM_CURSOR_WAIT	wait
pygame.SYSTEM_CURSOR_CROSSHAIR	crosshair
pygame.SYSTEM_CURSOR_SIZENWSE	double arrow pointing northwest and southeast
pygame.SYSTEM_CURSOR_SIZENESW	double arrow pointing northeast and southwest
pygame.SYSTEM_CURSOR_SIZEWE	double arrow pointing west and east
pygame.SYSTEM_CURSOR_SIZENS	double arrow pointing north and south
pygame.SYSTEM_CURSOR_SIZEALL	four pointed arrow
pygame.SYSTEM_CURSOR_NO	slashed circle or crossbones
pygame.SYSTEM_CURSOR_HAND	hand
'''

pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
pygame.display.set_caption("Coordenadas do Mouse e tipo do mouse")
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos=pygame.mouse.get_pos()
         btn=pygame.mouse
         print ("x = {}, y = {}".format(pos[0], pos[1]))