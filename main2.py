# Comentários
# Objetivos : Alterar o Título, O logotipo de Janela e a Cor de Fundo da Janela

# 1 -------------------------- importando a biblioteca do pygame ---------------
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
    janela.fill((255,134,0))
    pygame.display.update() # atualiza a geração da janela





