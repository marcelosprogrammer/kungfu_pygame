import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
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
      font = pygame.font.SysFont("Arial", 36)
   txtsurf = font.render("Apresentando Textos na Janela", True, white)
   screen.blit(txtsurf,(230 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
   pygame.display.update()