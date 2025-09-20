import pygame
from config import *
from ui.telas import *

janela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Damas')

tabuleiro = pygame.Surface((LARGURA, ALTURA))

def main():
    relogio = pygame.time.Clock() 
    rodando = True
    while rodando:
        relogio.tick(FPS)
        # Fecha o programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            tela_inicial(janela, tabuleiro)
    pygame.quit()
main()