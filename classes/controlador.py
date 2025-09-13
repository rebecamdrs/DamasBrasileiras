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
        pygame.display.update()

    def resetar_jogo(self):
        self._init()