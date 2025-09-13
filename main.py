import pygame
from config import *
from classes.controlador import Controlador

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Damas')

def main():
    relogio = pygame.time.Clock()
    controlador = Controlador(janela)
    rodando = True
    while rodando:
        relogio.tick(FPS)

        # Fecha o programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pass

        controlador.atualiza_jogo()

    pygame.quit()
    
main()