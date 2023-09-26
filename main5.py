# Comentários
# Objetivos : Movimentando a Imagem

# 1 -------------------------- importando a biblioteca do pygame ---------------
import random

import pygame

# 2 ----------------- INICIALIZANDO O PYGAME
pygame.init()

# 3 -------- CRIANDO A TELA INICIAL DO JOGO
janela = pygame.display.set_mode((800, 600))

# 3.1 - Configurando o Titulo
# 3.2 - Modificando o Icone
pygame.display.set_caption('Criando jogos com PyGame')
micone = pygame.image.load('robo.png')
pygame.display.set_icon(micone)

# 3.3 adicionando o lutador --------------------------------------------------------
dragaofundo = pygame.image.load('dragaochines.png')
lutador1 = pygame.image.load('girl1.png')
lutador1X = 200
lutador1Y = 300

# criando o método para o lutador 1
# explicar o que são os parametros da função - brevemente
def showLutador1(x,y):
    janela.blit(lutador1, (x, y))


meteoro = pygame.image.load('meteoro.png')
meteorox = random.randint(0, 500)
meteoroy = random.randint(0,500)
meteoro_alteracaox = 0

def showmeteoro(x,y):
    janela.blit(meteoro, (x,y))

# 4 - CRIA A VARIAVEL executar do tipo booleana e inicializa com True.
# explicar variável boolean
executar = True

# 5 - CRIA O LOOP PARA EXECUTAR A LOGICA DO JOGO
# 6 - ENQUANTO EXECUTAR FOR VERDADEIRO A JANELA FICARÁ ABERTA E O JOGO EM EXECUÇÃO.
while executar:
    # 7 - CAPTURA O EVENTO E VERIFICA SE O EVENTO (AÇÃO) GERADO É DE FECHAR A JANELA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executar = False
    # ALTERANDO A COR DA JANELA
    # A cor da janela é em RGB
    janela.fill((255,255,255))

    # 7.1 ADICIONANDO O LUTADOR 1 A EXECUÇÃO
    # modificado para gerar o movimento
    lutador1X += 0.1 # faz crescer o valor em 0.1 a cada passada do  loop
    if lutador1X > 450:
        lutador1X = 200

# 8.0 - Controlando movimento pleo teclado..
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            lutador1 = pygame.image.load('girl1.png')

        if event.key == pygame.K_RIGHT:
            lutador1 = pygame.image.load('girl2.png')

        if event.key == pygame.K_DOWN:
            lutador1 = pygame.image.load('girl3.png')

        if event.key == pygame.K_UP:
            lutador1 = pygame.image.load('girl4.png')

    meteorox += 0.4
    if meteorox <=0:
        meteorox = 0
    elif meteorox >= 450:
        meteorox = 450



    # adicionando o dragão ao fundo:
    janela.blit(dragaofundo, (150, 2))

    showmeteoro(meteorox,200)
    showLutador1(lutador1X, lutador1Y)
    pygame.display.update() # atualiza a geração da janela

    



