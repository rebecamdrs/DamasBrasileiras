import pygame
from .tabuleiro import Tabuleiro
from config import *

class Controlador:
    def __init__(self, janela):
        self._init()
        self.janela = janela

    def _init(self): # função privada
        self.peca_selecionada = None
        self.tabuleiro = Tabuleiro()
        self.turno = BRANCO
        self.movimentos_validos = {}

    def atualiza_jogo(self):
        self.tabuleiro.monta_tabuleiro(self.janela)
        if self.peca_selecionada:
            self.desenha_selecao(self.janela)
            self.desenha_movimentos_validos(self.janela)
        pygame.display.update()

    def resetar_jogo(self):
        self._init()

    def _mover(self, linha, coluna):
        peca_mover = self.peca_selecionada
        if peca_mover and (linha, coluna) in self.movimentos_validos:
            pecas_capturadas = self.movimentos_validos[(linha, coluna)]
            self.tabuleiro.mover(peca_mover, linha, coluna)
            if pecas_capturadas:
                self.tabuleiro.remover(pecas_capturadas)
            self.mudar_turno()
        else:
            return False
        return True

    def mudar_turno(self):
        self.peca_selecionada = None
        self.movimentos_validos = {}
        if self.turno == BRANCO:
            self.turno = ROSA
        else:
            self.turno = BRANCO

    def gerencia_clique(self, linha, coluna):
        if (linha, coluna) in self.movimentos_validos:
            self._mover(linha, coluna)
            return
        
        peca = self.tabuleiro.obtem_peca(linha, coluna)
        if peca != 0 and peca.cor == self.turno:
            self.peca_selecionada = peca
            self.movimentos_validos = self.tabuleiro.get_movimentos_validos(peca)
        else:
            self.peca_selecionada = None
            self.movimentos_validos = {}
    
    def desenha_selecao(self, janela):
        if self.peca_selecionada:
            linha, coluna = self.peca_selecionada.linha, self.peca_selecionada.coluna
            raio_externo = TAMANHO_QUADRADO // 2
            pygame.draw.circle(janela, AZUL_CLARO, (coluna * TAMANHO_QUADRADO + raio_externo, linha * TAMANHO_QUADRADO + raio_externo), raio_externo - 5, 4)

    def desenha_movimentos_validos(self, janela):
        for movimento in self.movimentos_validos:
            linha, coluna = movimento
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            pygame.draw.rect(janela, CINZA_CLARO, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))