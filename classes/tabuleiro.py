import pygame
from config import *
from .peca import Peca

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.pecas_rosas, self.pecas_brancas = 12, 12
        self.damas_rosas, self.damas_brancas = 0, 0
        self.desenha_tabuleiro()

    def desenha_quadrados(self, janela):
        janela.fill(CINZA)
        for linha in range(LINHAS):
            for coluna in range(linha % 2, COLUNAS, 2):
                pygame.draw.rect(janela, BRANCO, (linha * TAMANHO_QUADRADO, coluna * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

    def desenha_tabuleiro(self):
        for linha in range(LINHAS):
            self.tabuleiro.append([])
            for coluna in range(COLUNAS):
                # condição para que as peças sejam colocadas nas casas pretas
                if coluna % 2 == ((linha + 1) % 2):
                    if linha < 3:
                        self.tabuleiro[linha].append(Peca(linha, coluna, ROSA))
                    elif linha > 4:
                        self.tabuleiro[linha].append(Peca(linha, coluna, BRANCO))
                    else:
                        self.tabuleiro[linha].append(0)
                        
                # casas "brancas" do tabuleiro ficam vazias
                else: 
                    self.tabuleiro[linha].append(0)

    def monta_tabuleiro(self, janela):
        self.desenha_quadrados(janela)
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro[linha][coluna]
                if peca != 0:
                    peca.cria_peca(janela)

    def mover(self, peca, linha, coluna):
        self.tabuleiro[peca.linha][peca.coluna], self.tabuleiro[linha][coluna] = self.tabuleiro[linha][coluna], self.tabuleiro[peca.linha][peca.coluna]
        peca.mover(linha, coluna)

        if (linha == LINHAS - 1 and peca.cor == ROSA) or (linha == 0 and peca.cor == BRANCO):
            if not peca.eh_dama:
                peca.vira_dama()
                if peca.cor == ROSA:
                    self.damas_rosas += 1
                else:
                    self.damas_brancas += 1
    
    def obtem_peca(self, linha, coluna):
        return self.tabuleiro[linha][coluna]
    
    def remover(self, pecas):
        for peca in pecas:
            self.tabuleiro[peca.linha][peca.coluna] = 0
            if peca != 0:
                if peca.cor == BRANCO:
                    self.pecas_brancas -= 1
                else:
                    self.pecas_rosas -= 1
    
    def get_movimentos_validos(self, peca):
        movimentos = {}
        linha, coluna = peca.linha, peca.coluna

        def percorrer_diagonal(direcoes):
            for d_linha, d_coluna in direcoes:
                peca_capturada = None
                for i in range(1, LINHAS):
                    linha_atual = linha + i * d_linha
                    coluna_atual = coluna + i * d_coluna

                    if not (0 <= linha_atual < LINHAS and 0 <= coluna_atual < COLUNAS):
                        break

                    peca_no_caminho = self.tabuleiro[linha_atual][coluna_atual]

                    if peca_no_caminho == 0:
                        if peca_capturada:
                            movimentos[(linha_atual, coluna_atual)] = [peca_capturada]
                        else:
                            movimentos[(linha_atual, coluna_atual)] = []
                    elif peca_no_caminho.cor == peca.cor:
                        break
                    else:
                        if peca_capturada:
                            break
                        else:
                            peca_capturada = peca_no_caminho

                    if not peca.eh_dama:
                        break

        if peca.eh_dama:
            percorrer_diagonal([(-1, -1), (-1, 1), (1, -1), (1, 1)])
        else:
            if peca.cor == BRANCO:
                percorrer_diagonal([(-1, -1), (-1, 1)])
            else:
                percorrer_diagonal([(1, -1), (1, 1)])
        
        movimentos_com_captura = {}
        for k,v in movimentos.items():
            if v:
                movimentos_com_captura[k] = v

        if movimentos_com_captura:
            return movimentos_com_captura
        return movimentos
