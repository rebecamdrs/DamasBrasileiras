import pygame
from .tabuleiro import Tabuleiro
from utils.config import *

class Controlador:
    """Classe que controla toda a mecânica do tabuleiro."""
    def __init__(self, janela):
        self._init()
        self.janela = janela

    def _init(self): # função privada
        self.peca_selecionada = None
        self.tabuleiro = Tabuleiro()
        self.turno = BRANCO
        self.movimentos_validos = {}
        self.capturas_obrigatorias = {}

        # Variáveis de estado do jogo
        self.vencedor = None
        self.empate = False

        # Variáveis para seleção inválida
        self.peca_invalida = None
        self.tempo_invalido = 0
        
        # Contador para regra de empate
        self.contador_lances_branco = 0
        self.contador_lances_rosa = 0
        self._verificar_capturas()

        # Variáveis do tempo
        self.modo = 'normal'
        self.inicio = None
        self.tempo_pausado = 0
        self.tempo_restante = None

    def verifica_fim(self):
        """Retorna o resultado da partida."""
        # Vitória por captura de todas as peças
        if self.tabuleiro.brancas_totais == 0:
            return ROSA
        elif self.tabuleiro.rosas_totais == 0:
            return BRANCO
        
        # Vitória por bloqueio
        if not self._verifica_movimentos():
            if self.turno == BRANCO:
                return ROSA
            else:
                return BRANCO
            
        # Empate pela regra dos 20 lances
        if self.contador_lances_branco >= 20 and self.contador_lances_rosa >= 20:
            return 'EMPATE'
        return None

    def atualiza_jogo(self):
        """Atualiza o jogo a cada turno."""
        self.tabuleiro.monta_tabuleiro(self.janela)
        self.desenha_selecao_invalida(self.janela)

        if self.peca_selecionada:
            self.desenha_selecao(self.janela)
            self.desenha_movimentos_validos(self.janela)
        
        if self.vencedor is None:
            self.vencedor = self.verifica_fim()
        
        pygame.display.update()

    def resetar_jogo(self, modo, tempo=None):
        """Reseta o jogo para as configurações iniciais."""
        self._init()
        self.modo = modo

        if modo == 'tempo' and tempo is not None:
            self.tempo_restante = tempo * 60
            self.inicio = pygame.time.get_ticks() // 1000
            self.tempo_pausado = 0

    def _mover(self, linha, coluna):
        """
        Tenta mover a peça selecionada para a posição (linha, coluna).
        - Move a peça no tabuleiro.
        - Remove peças capturadas, se houver.
        - Pode atualizar os movimentos válidos (em caso de múltiplas capturas).
        - Pode mudar o turno do jogador.
        - Atualiza os contadores da regra dos 20 lances.
        """
        peca_mover = self.peca_selecionada

        if peca_mover and (linha, coluna) in self.movimentos_validos:
            pecas_capturadas = self.movimentos_validos[(linha, coluna)]
            MOVE.play()
            self.tabuleiro.mover(peca_mover, linha, coluna)

            # Se houve captura, remove a peça e em seguida procura novas capturas a partir da nova posição
            if pecas_capturadas:
                self.tabuleiro.remover(pecas_capturadas)
                novos_movimentos = self.tabuleiro.movimentos_validos(peca_mover)

                novas_capturas = {}
                for posicao, lista_pecas in novos_movimentos.items():
                    if lista_pecas:
                        novas_capturas[posicao] = lista_pecas

                # Se há nova captura, o turno não muda
                if novas_capturas:
                    self.movimentos_validos = novas_capturas
                # Se não, muda o turno
                else:
                    self.mudar_turno()
            # Se foi apenas uma captura, muda o turno
            else:
                self.mudar_turno()

            # Regra dos 20 Lances
            if pecas_capturadas or not peca_mover.eh_dama:
                self.contador_lances_branco = 0
                self.contador_lances_rosa = 0
            elif peca_mover.eh_dama and not pecas_capturadas:
                if peca_mover.cor == BRANCO:
                    self.contador_lances_branco += 1
                else:
                    self.contador_lances_rosa += 1
            
            return True # O movimento foi válido
        return False # O movimento era inválido

    def _verificar_capturas(self):
        """ Verificar o tabuleito inteiro para encontrar todas as capturas obrigatórias do turno atual. """
        self.capturas_obrigatorias = {}

        # Percorre por cada casa do tabuleiro
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro.obtem_peca(linha, coluna)

                # Verifica se a peça pertence ao jogador da vez
                if peca != 0 and peca.cor == self.turno:
                    movimentos_da_peca = self.tabuleiro.movimentos_validos(peca)

                    if any(movimentos_da_peca.values()):
                        self.capturas_obrigatorias[peca] = movimentos_da_peca

    def _verifica_movimentos(self):
        """ Verifica se o jogador do turno atual tem algum movimento válido """
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                peca = self.tabuleiro.obtem_peca(linha, coluna)

                if peca != 0 and peca.cor == self.turno:
                    if self.tabuleiro.movimentos_validos(peca):
                        return True # Encontrou movimentos possíveis
        return False # Nenhuma peça tem movimentos

    def mudar_turno(self):
        """Troca o turno atual e reseta os movimentos válidos e a peça selecionada."""
        self.peca_selecionada = None
        self.movimentos_validos = {}
        if self.turno == BRANCO:
            self.turno = ROSA
        else:
            self.turno = BRANCO
        self._verificar_capturas()

    def gerencia_clique(self, linha, coluna):
        """Verifica o clique em tal casa destino"""
        # Se o clique for em um movimento válido, executa o movimento
        if (linha, coluna) in self.movimentos_validos:
            self._mover(linha, coluna)
            return
        
        peca = self.tabuleiro.obtem_peca(linha, coluna)

        # Se há captura obrigatória e o jogador clica em outra peça que seja sua
        if self.capturas_obrigatorias and peca not in self.capturas_obrigatorias:
            if peca != 0:
                INVALIDO.play()
                self._marcar_invalido(peca)
            return

        # Se o jogador clica em uma de suas peças
        if peca != 0 and peca.cor == self.turno:
            MOUSE_CLICK.play()
            movimentos_possiveis = self.tabuleiro.movimentos_validos(peca)
            if movimentos_possiveis: # Tem movimentos
                self.peca_selecionada = peca
                self.movimentos_validos = movimentos_possiveis
                self.peca_invalida = None
            else: # Não tem movimentos
                self._marcar_invalido(peca)
        else: # Se clica em uma peça do inimigo
            INVALIDO.play()
            self._marcar_invalido(peca)

    def _marcar_invalido(self, peca):
        self.peca_invalida = peca
        self.tempo_invalido = pygame.time.get_ticks()
        self.peca_selecionada = None
        self.movimentos_validos = {}
    
    def desenha_selecao(self, janela):
        """Desenha a borda na peça selecionada."""
        if self.peca_selecionada:
            linha, coluna = self.peca_selecionada.linha, self.peca_selecionada.coluna
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            raio_externo = TAMANHO_QUADRADO  // 2
            pygame.draw.circle(janela, AZUL_CLARO, (x + raio_externo, y + raio_externo), raio_externo - 3, 4)

    def desenha_selecao_invalida(self, janela):
        """ Desenha a borda na peça selecionada invalidamente."""
        if self.peca_invalida:
            duracao_ms = 500 # O círculo aparacerá por 0.5s
            agora = pygame.time.get_ticks()

            if agora - self.tempo_invalido < duracao_ms:
                linha, coluna = self.peca_invalida.linha, self.peca_invalida.coluna
                x = coluna * TAMANHO_QUADRADO
                y = linha * TAMANHO_QUADRADO
                raio_externo = TAMANHO_QUADRADO // 2
                pygame.draw.circle(janela, VERMELHO, (x + raio_externo, y + raio_externo), raio_externo - 3, 4)
            else:
                # Limpa a variável após o tempo expirar
                self.peca_invalida = None

    def desenha_movimentos_validos(self, janela):
        """Mostra no tabuleiro os movimentos válidos da peça selecionda, caso houver."""
        for movimento in self.movimentos_validos:
            linha, coluna = movimento
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            pygame.draw.rect(janela, AZUL_CLARO, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))