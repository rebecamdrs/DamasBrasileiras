import pygame

''' GERAL'''
FPS = 60

''' CORES '''
PRETO = (8, 20, 32)
AZUL_ESCURO = (6, 27, 50)
CINZA = (39, 61, 84)
CINZA_CLARO = (170, 170, 170)
BRANCO = (255, 255, 255)
BRANCO_OFF = (242, 242, 242)
ROSA = (240, 72, 164)
AZUL_CLARO = (130, 229, 223)

''' DIMENSÕES '''
# Tabuleiro
LARGURA, ALTURA = 400, 400
LINHAS, COLUNAS = 8, 8
TAMANHO_QUADRADO = LARGURA // COLUNAS

# Telas
TELA_ALTURA, TELA_LARGURA = 600, 1000

''' IMAGENS '''
# Peças
PECA_ROSA = pygame.transform.scale(pygame.image.load('assets/images/peca_rosa.png'), (36, 36))
PECA_BRANCA = pygame.transform.scale(pygame.image.load('assets/images/peca_branca.png'), (36, 36))
DAMA_ROSA = pygame.transform.scale(pygame.image.load('assets/images/dama_rosa.png'), (36, 36))
DAMA_BRANCA = pygame.transform.scale(pygame.image.load('assets/images/dama_branca.png'), (36, 36))

# Botões
BOTAO_JOGAR = pygame.image.load('assets/images/botao_jogar.png')
BOTAO_REGRAS = pygame.image.load('assets/images/botao_regras.png')
BOTAO_SAIR = pygame.image.load('assets/images/botao_sair.png')

class Peca:
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
        print(f'Peças brancas: {self.pecas_brancas}; Peças rosas: {self.pecas_rosas}; Damas brancas: {self.damas_brancas}; Damas rosas: {self.damas_rosas}\n')
        
    def movimentos_validos(self, peca):
        """ Gerencia a obtenção de movimentos válidos.  """
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
        # Define a direção do movimento com base na cor da peça
        if peca.cor == BRANCO:
            direcao_linha = -1
        else:
            direcao_linha = 1
        
        # Verifica as diagonais
        for direcao_coluna in [-1, 1]:
            linha_alvo = peca.linha + direcao_linha
            coluna_alvo = peca.coluna + direcao_coluna

            # Verifica se a casa está no tabuleiro
            if 0 <= linha_alvo < LINHAS and 0 <= coluna_alvo < COLUNAS:
                peca_caminho = self.tabuleiro[linha_alvo][coluna_alvo]

                # A casa está vazia, movimento permitido
                if peca_caminho == 0:
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
        direcoes = [(-1, -1), (-1, 1), (1, -1), (1,1)]

        for d_linha, d_coluna in direcoes:
            movimentos.update(self._verifica_diagonal(peca, d_linha, d_coluna))
        return movimentos

    def _verifica_diagonal(self, peca, d_linha, d_coluna):
        """ Caminha por uma diagonal, encontrando os movimentos válidos para a Dama """
        movimentos_diagonal = {}
        # Armazena a peça inimiga que pode ser capturada no caminho
        peca_capturada = None

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

class Controlador:
    def __init__(self, janela):
        self._init()
        self.janela = janela
        self.vencedor = None

    def _init(self): # função privada
        self.peca_selecionada = None
        self.tabuleiro = Tabuleiro()
        self.turno = BRANCO
        self.movimentos_validos = {}

    def verifica_vitoria(self):
        if self.tabuleiro.pecas_brancas == 0 and self.tabuleiro.damas_brancas == 0:
            return ROSA
        elif self.tabuleiro.pecas_rosas == 0 and self.tabuleiro.damas_rosas == 0:
            return BRANCO
        # opcao para sem saida?
        return None

    def atualiza_jogo(self):
        self.tabuleiro.monta_tabuleiro(self.janela)
        if self.peca_selecionada:
                self.desenha_selecao(self.janela)
                self.desenha_movimentos_validos(self.janela)
                
        if self.vencedor is not None:
            self.tela_vencedor(self.vencedor)
        else:
            self.vencedor = self.verifica_vitoria()
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
            self.movimentos_validos = self.tabuleiro.movimentos_validos(peca)
        else:
            self.peca_selecionada = None
            self.movimentos_validos = {}
    
    def desenha_selecao(self, janela):
        if self.peca_selecionada:
            linha, coluna = self.peca_selecionada.linha, self.peca_selecionada.coluna
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            raio_externo = TAMANHO_QUADRADO  // 2
            pygame.draw.circle(janela, AZUL_CLARO, (x + raio_externo, y + raio_externo), raio_externo - 3, 4)

    def desenha_movimentos_validos(self, janela):
        for movimento in self.movimentos_validos:
            linha, coluna = movimento
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            pygame.draw.rect(janela, AZUL_CLARO, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    
    # FUNCAO APENAS PARA TESTE
    def tela_vencedor(self, vencedor):
        self.janela.fill(AZUL_CLARO)
        fonte = pygame.font.SysFont('Montserrat', 40)
        if vencedor == BRANCO:
            texto = 'BRANCO VENCEU!'
        else:
            texto = 'ROSA VENCEU!'
        render_texto = fonte.render(texto, True, vencedor)
        self.janela.blit(render_texto, (LARGURA//2 - render_texto.get_width()//2, ALTURA//2 - render_texto.get_height()//2))

def obtem_clique(pos):
    x, y = pos
    linha = y // TAMANHO_QUADRADO
    coluna = x // TAMANHO_QUADRADO
    return linha, coluna

def main():
    pygame.init()
    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Damas')
    relogio = pygame.time.Clock()
    controlador = Controlador(janela)
    rodando = True
    while rodando:
        relogio.tick(FPS)

        # Fecha o programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            #tela_inicial(janela)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                linha, coluna = obtem_clique(posicao)
                controlador.gerencia_clique(linha, coluna)
        controlador.atualiza_jogo()
        
    pygame.quit()
    
main()