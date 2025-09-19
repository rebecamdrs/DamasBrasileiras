import pygame
from config import *
from ui.telas import *

pygame.font.init()
janela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Damas')

def main():
    relogio = pygame.time.Clock() 
    rodando = True
    while rodando:
        relogio.tick(FPS)
        # Fecha o programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            tela_inicial(janela)
    pygame.quit()
    
main()