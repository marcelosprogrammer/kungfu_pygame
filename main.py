# Comentários
# Objetivos:
# 1.0 - importar a biblioteca
# 2.0 - iniciar a bibliteca
# 3.0 - configurar tamanho da janela e rodar o código

# 1 -------------------------- importando a biblioteca do pygame ---------------
import pygame

# 2 ----------------- INICIALIZANDO O PYGAME
pygame.init()

# 3 -------- CRIANDO A TELA INICIAL DO JOGO
janela = pygame.display.set_mode((800, 600))

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





