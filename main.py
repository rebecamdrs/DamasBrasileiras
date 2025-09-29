import pygame
from utils.config import *
from ui.telas import *

janela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Damas Brasileiras')
pygame.display.set_icon(DAMA_ROSA)
tabuleiro = pygame.Surface((LARGURA_TABULEIRO, ALTURA_TABULEIRO))

def main():
    relogio = pygame.time.Clock() 
    rodando = True
    while rodando:
        relogio.tick(FPS)
        rodando = tela_inicial(janela, tabuleiro)
    pygame.quit()

if __name__ == '__main__':
    main()