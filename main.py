import pygame
from config import *
from classes.controlador import Controlador
from ui.telas import *

janela = pygame.display.set_mode((LARGURA, ALTURA))
#janela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
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
            #tela_inicial(janela)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                linha, coluna = obtem_clique(posicao)
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