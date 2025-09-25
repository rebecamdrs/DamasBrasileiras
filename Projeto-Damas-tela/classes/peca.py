from utils.config import *

class Peca:
    """Classe para criação das peças do tabuleiro."""
    def __init__(self, linha, coluna, cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        self.eh_dama = False
        self.x, self.y = 0, 0
        self.calcula_posicao()

    def calcula_posicao(self):
        self.x = TAMANHO_QUADRADO * self.coluna + TAMANHO_QUADRADO // 2
        self.y = TAMANHO_QUADRADO * self.linha + TAMANHO_QUADRADO // 2

    def cria_peca(self, janela):
        if not self.eh_dama:
            if self.cor == ROSA:
                janela.blit(PECA_ROSA, (self.x - PECA_ROSA.get_width() // 2, self.y - PECA_ROSA.get_height() // 2))
            elif self.cor == BRANCO:
                janela.blit(PECA_BRANCA, (self.x - PECA_BRANCA.get_width() // 2, self.y - PECA_BRANCA.get_height() // 2))
        else:
            if self.cor == ROSA:
                janela.blit(DAMA_ROSA, (self.x - DAMA_ROSA.get_width() // 2, self.y - DAMA_ROSA.get_height() // 2))
            elif self.cor == BRANCO:
                janela.blit(DAMA_BRANCA, (self.x - DAMA_BRANCA.get_width() // 2, self.y - DAMA_BRANCA.get_height() // 2))

    def vira_dama(self):
        self.eh_dama = True

    def mover(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.calcula_posicao()

    def __repr__(self):
        return str(self.cor)