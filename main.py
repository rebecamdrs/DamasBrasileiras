import pygame
from config import *
from classes.controlador import Controlador

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Damas')

def obtem_clique(pos):
    x, y = pos
    linha = y // TAMANHO_QUADRADO
    coluna = x // TAMANHO_QUADRADO
    return linha, coluna

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
            
            # adicionar botoes aqui e as proximas linhas aparecem apenas no iniciar

            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                linha, coluna = obtem_clique(pos)
                controlador.gerencia_clique(linha, coluna)

        controlador.atualiza_jogo()
        
    pygame.quit()
    
main()
'''
funcoes que faltam:

botoes
regras
tela_vencedor

mecanicas:
capturar peca
'''