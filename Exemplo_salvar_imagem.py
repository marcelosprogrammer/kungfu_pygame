import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
white=(255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bg = (127,127,127)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      if event.type == pygame.QUIT:
         done = True
      pygame.draw.circle(screen, red, (200,150), 60,2)
      pygame.draw.circle(screen, green, (200,150), 80,2)
      pygame.draw.circle(screen, blue, (200,150), 100,2)
   pygame.display.update()
   pygame.image.save(screen, "circulos.png")