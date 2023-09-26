# Comentários
# Objetivos : Adicionando Oponentes

# 1 -------------------------- importando a biblioteca do pygame ---------------
import random

import pygame

# 2 ----------------- INICIALIZANDO O PYGAME
from pygame import mixer

pygame.init()

# 3 -------- CRIANDO A TELA INICIAL DO JOGO
janela = pygame.display.set_mode((800, 600))

# Sound
mixer.music.load("Juhani Junkala [Retro Game Music Pack] Level 1.wav")
mixer.music.play(-1)

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

def showmeteoro(x,y, i):
    janela.blit(meteoroImg[i], (x, y))

# 4 - CRIA A VARIAVEL executar do tipo booleana e inicializa com True.
# explicar variável boolean
executar = True


### adicionando Oponente ===========================================================
meteoroImg = []
meteoroX = []
meteoroY = []
meteoroX_alteracao = []
meteoroY_alteracao = []
quantidade = 8


for i in range(quantidade):
    meteoroImg.append(pygame.image.load('cometab.png'))
    meteoroX.append(random.randint(0, 736))
    meteoroY.append(random.randint(50, 150))
    meteoroX_alteracao.append(4)
    meteoroY_alteracao.append(40)
## ================================================================================

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

# GERANDO O MOVIMENTO ======================================================

    for i in range(quantidade):

        # Game Over
        if meteoroY[i] > 440:
            for j in range(quantidade):
                meteoroY[j] = 2000
            #game_over_text()
            break

        meteoroX[i] += meteoroX_alteracao[i]
        if meteoroX[i] <= 0:
            meteoroX_alteracao[i] = 4
            meteoroY[i] += meteoroY_alteracao[i]
        elif meteoroX[i] >= 736:
            meteoroX_alteracao[i] = -4
            meteoroY[i] += meteoroY_alteracao[i]
        showmeteoro(meteoroX[i], meteoroY[i], i)


    # adicionando o dragão ao fundo:
    janela.blit(dragaofundo, (150, 2))

    showLutador1(lutador1X, lutador1Y)
    pygame.display.update() # atualiza a geração da janela

    



