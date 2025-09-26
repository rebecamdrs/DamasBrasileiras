import pygame
from utils.config import *
from .peca import Peca

class Tabuleiro:
    """Classe que cria o tabuleiro e guarda seus dados atuais."""
    def __init__(self):
        self.tabuleiro = []
        self.pecas_rosas, self.pecas_brancas = 12, 12
        self.damas_rosas, self.damas_brancas = 0, 0
        self.direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.atualiza_contagem_total()
        self.desenha_tabuleiro()

    def desenha_quadrados(self, janela):
        """Desenha as casas brancas do tabuleiro."""
        janela.fill(CINZA)
        for linha in range(LINHAS):
            for coluna in range(linha % 2, COLUNAS, 2):
                pygame.draw.rect(janela, BRANCO, (linha * TAMANHO_QUADRADO, coluna * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

    def desenha_tabuleiro(self):
        """Cria a estrutura do tabuleiro."""
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
        """Mostra o tabuleiro na tela: casas e peças."""
        self.desenha_quadrados(janela)
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro[linha][coluna]
                if peca != 0:
                    peca.cria_peca(janela)
    
    def atualiza_contagem_total(self):
        """Atualiza a contagem total de peças do tabuleiro após cada turno.
        - Peças normais + damas"""
        self.rosas_totais = self.pecas_rosas + self.damas_rosas
        self.brancas_totais = self.pecas_brancas + self.damas_brancas

    def mover(self, peca, linha, coluna):
        """Move uma peça para a casa destino selecionada. Caso a peça seja movida para a primeira/última linha, é analisado a condição de virar dama."""
        self.tabuleiro[peca.linha][peca.coluna], self.tabuleiro[linha][coluna] = self.tabuleiro[linha][coluna], self.tabuleiro[peca.linha][peca.coluna]
        peca.mover(linha, coluna)
        if (linha == LINHAS - 1 and peca.cor == ROSA) or (linha == 0 and peca.cor == BRANCO):
            if not peca.eh_dama:
                peca.vira_dama()
                if peca.cor == ROSA:
                    self.damas_rosas += 1
                    self.pecas_rosas -= 1
                else:
                    self.damas_brancas += 1
                    self.pecas_brancas -= 1
                self.atualiza_contagem_total()
    
    def obtem_peca(self, linha, coluna):
        """Retorna a peça do tabuleiro que está na posição dada."""
        return self.tabuleiro[linha][coluna]

    def remover(self, pecas):
        """Remove a(s) peça(s) fornecidas do tabuleiro."""
        for peca in pecas:
            self.tabuleiro[peca.linha][peca.coluna] = 0
            if peca != 0:
                if peca.eh_dama:
                    if peca.cor == BRANCO:
                        self.damas_brancas -= 1
                    else:
                        self.damas_rosas -= 1
                else:
                    if peca.cor == BRANCO:
                        self.pecas_brancas -= 1
                    else:
                        self.pecas_rosas -= 1
        self.atualiza_contagem_total()
    
    def movimentos_validos(self, peca):
        """Gerencia a obtenção de movimentos válidos."""
        movimentos = {}
        if peca.eh_dama:
            movimentos = self._movimentos_dama(peca)
        else:
            movimentos = self._movimentos_peca(peca)

        movimentos_captura = {}
        for posicao, peca_capturada in movimentos.items():
            if peca_capturada:
                movimentos_captura[posicao] = peca_capturada
        
        if movimentos_captura:
            return movimentos_captura
        return movimentos

    def _movimentos_peca(self, peca):
        """ Calcula os movimentos de uma peça que não é Dama """
        movimentos = {}
        
        # Percorre todas as direções diagonais possíveis
        for direcao_linha, direcao_coluna in self.direcoes:
            # Calcula a coordenada da casa de destino
            linha_alvo = peca.linha + direcao_linha
            coluna_alvo = peca.coluna + direcao_coluna

            # Verifica se a casa está no tabuleiro
            if 0 <= linha_alvo < LINHAS and 0 <= coluna_alvo < COLUNAS:
                peca_caminho = self.tabuleiro[linha_alvo][coluna_alvo]

                # A casa está vazia
                if peca_caminho == 0:
                    movimento_valido = False
                    
                    # Peças brancas só podem se mover para linhas com íncide menor 
                    if peca.cor == BRANCO and direcao_linha == -1:
                        movimento_valido = True

                    # Peças rosas só podem se mover para linhas com íncide maior 
                    elif peca.cor == ROSA and direcao_linha == 1:
                        movimento_valido = True
                    
                    # Se o movimento é válido, adiciona a posição no dicionário de movimentos
                    if movimento_valido:
                        movimentos[(linha_alvo, coluna_alvo)] = []

                # A casa tem uma peça inimiga, potencial captura
                elif peca_caminho.cor != peca.cor: 
                    # Calcula a posição de pouso do salto
                    linha_salto = peca.linha + 2 * direcao_linha
                    coluna_salto = peca.coluna + 2 * direcao_coluna
                    # Verifica se a casa de pouso está dentro do tabuleiro e vazia
                    if 0 <= linha_salto < LINHAS and 0 <= coluna_salto < COLUNAS and self.tabuleiro[linha_salto][coluna_salto] == 0:
                        movimentos[(linha_salto, coluna_salto)] = [peca_caminho]
        return movimentos

    def _movimentos_dama(self, peca):
        """ Calcula os movimentos para uma Dama """
        movimentos = {}
        for d_linha, d_coluna in self.direcoes:
            movimentos.update(self._verifica_diagonal(peca, d_linha, d_coluna))
        return movimentos

    def _verifica_diagonal(self, peca, d_linha, d_coluna):
        """ Caminha por uma diagonal, encontrando os movimentos válidos para a Dama """
        movimentos_diagonal = {}
        peca_capturada = None # Peça inimiga que pode ser capturada no caminho

        # Itera pelas casas na diagonal, começando a 1 passo da Dama
        for i in range(1, LINHAS):
            linha_atual = peca.linha + i * d_linha
            coluna_atual = peca.coluna + i * d_coluna
            if not(0 <= linha_atual < LINHAS and 0 <= coluna_atual < COLUNAS):
                break
            peca_caminho = self.tabuleiro[linha_atual][coluna_atual]

            # Encontrou uma casa vazia
            if peca_caminho == 0:
                if peca_capturada:
                    movimentos_diagonal[(linha_atual, coluna_atual)] = [peca_capturada]
                else:
                    movimentos_diagonal[(linha_atual, coluna_atual)] = []
            
            # Encontrou uma peça amiga
            elif peca_caminho.cor == peca.cor:
                break

            # Encontrou uma peça inimiga
            else:
                if peca_capturada:
                    break # AJUSTAR PARA CAPTURAR MAIS DE UMA PEÇA
                else:
                    peca_capturada = peca_caminho
        return movimentos_diagonal