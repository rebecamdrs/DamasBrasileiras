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
VERMELHO = (255, 0, 0)

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
        self.direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.atualiza_contagem_total()
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

    def atualiza_contagem_total(self):
        self.rosas_totais = self.pecas_rosas + self.damas_rosas
        self.brancas_totais = self.pecas_brancas + self.damas_brancas

    def mover(self, peca, linha, coluna):
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
        self.atualiza_contagem_total()
        
        print(f'Peças brancas: {self.pecas_brancas}; Peças rosas: {self.pecas_rosas}; Damas brancas: {self.damas_brancas}; Damas rosas: {self.damas_rosas}')
        print(f'BRANCAS TOTAIS: {self.brancas_totais}; ROSAS TOTAIS:{self.rosas_totais}\n')
        
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
        
        for direcao_linha, direcao_coluna in self.direcoes:
            linha_alvo = peca.linha + direcao_linha
            coluna_alvo = peca.coluna + direcao_coluna

            # Verifica se a casa está no tabuleiro
            if 0 <= linha_alvo < LINHAS and 0 <= coluna_alvo < COLUNAS:
                peca_caminho = self.tabuleiro[linha_alvo][coluna_alvo]

                if peca_caminho == 0:
                    movimento_valido = False

                    if peca.cor == BRANCO and direcao_linha == -1:
                        movimento_valido = True
                    elif peca.cor == ROSA and direcao_linha == 1:
                        movimento_valido = True
                    
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
                    break 
                else:
                    peca_capturada = peca_caminho
        return movimentos_diagonal

class Controlador:
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

    def verifica_vitoria(self):
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
                
        return None
    
    def verifica_empate(self):
        # Regra do 20 Lances
        if self.contador_lances_branco >= 20 and self.contador_lances_rosa >= 20:
            return True
        return False
    
    def atualiza_jogo(self):
        self.tabuleiro.monta_tabuleiro(self.janela)
        self.desenha_selecao_invalida(self.janela)

        if self.peca_selecionada:
                self.desenha_selecao(self.janela)
                self.desenha_movimentos_validos(self.janela)
                
        if self.vencedor is None and not self.empate:
            vencedor_encontrado = self.verifica_vitoria()
            if vencedor_encontrado:
                self.vencedor = vencedor_encontrado
            elif self.verifica_empate():
                self.empate = True

        if self.vencedor is not None:
            self.tela_vencedor(self.vencedor)
        elif self.empate:
            self.tela_empate()
                
        pygame.display.update()

    def resetar_jogo(self):
        self._init()

    def _mover(self, linha, coluna):
        peca_mover = self.peca_selecionada

        if peca_mover and (linha, coluna) in self.movimentos_validos:
            pecas_capturadas = self.movimentos_validos[(linha, coluna)]
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
            # Se foi apenas uma captura muda o turno
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
        """ Verifica o tabuleiro inteiro para encontrar todas as capturas obrigatórias do turno atual """
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
        self.peca_selecionada = None
        self.movimentos_validos = {}

        if self.turno == BRANCO:
            self.turno = ROSA
        else:
            self.turno = BRANCO
        self._verificar_capturas()

    def gerencia_clique(self, linha, coluna):
        # Se o clique for em um movimento válido, executa o movimento
        if (linha, coluna) in self.movimentos_validos:
            self._mover(linha, coluna)
            return
        
        peca = self.tabuleiro.obtem_peca(linha, coluna)

        # Se há captura obrigatória e o jogador clica em outra peça que seja sua
        if self.capturas_obrigatorias and peca not in self.capturas_obrigatorias:
            if peca != 0:
                self._marcar_invalido(peca)
            return

        # Se o jogador clica em uma de suas peças
        if peca != 0 and peca.cor == self.turno:
            movimentos_possiveis = self.tabuleiro.movimentos_validos(peca)
            
            if movimentos_possiveis: # Tem movimentos
                self.peca_selecionada = peca
                self.movimentos_validos = movimentos_possiveis
                self.peca_invalida = None
            else: # Não tem movimentos
                self._marcar_invalido(peca)
        else: # Se clica em uma peça do inimigo
            self._marcar_invalido(peca)
    
    def _marcar_invalido(self, peca):
        self.peca_invalida = peca
        self.tempo_invalido = pygame.time.get_ticks()
        self.peca_selecionada = None
        self.movimentos_validos = {}

    def desenha_selecao(self, janela):
        if self.peca_selecionada:
            linha, coluna = self.peca_selecionada.linha, self.peca_selecionada.coluna
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            raio_externo = TAMANHO_QUADRADO  // 2
            pygame.draw.circle(janela, AZUL_CLARO, (x + raio_externo, y + raio_externo), raio_externo - 3, 4)

    def desenha_selecao_invalida(self, janela):
        """ Desenha um círculo vermelho ao redor de uma peça selecionada invalidamente """
        if self.peca_invalida:
            duracao_ms = 500  # O círculo aparecerá por 0.5 segundos
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
        for movimento in self.movimentos_validos:
            linha, coluna = movimento
            x = coluna * TAMANHO_QUADRADO 
            y = linha * TAMANHO_QUADRADO
            pygame.draw.rect(janela, AZUL_CLARO, (x, y, TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    
    # FUNCOES APENAS PARA TESTE
    def tela_vencedor(self, vencedor):
        self.janela.fill(AZUL_CLARO)
        fonte = pygame.font.SysFont('Montserrat', 40)
        if vencedor == BRANCO:
            texto = 'BRANCO VENCEU!'
        else:
            texto = 'ROSA VENCEU!'
        render_texto = fonte.render(texto, True, vencedor)
        self.janela.blit(render_texto, (LARGURA//2 - render_texto.get_width()//2, ALTURA//2 - render_texto.get_height()//2))

    def tela_empate(self):
        self.janela.fill(AZUL_CLARO)
        fonte = pygame.font.SysFont('Montserrat', 40)
        texto = 'EMPATE'
        render_texto = fonte.render(texto, True, CINZA_CLARO)
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

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                linha, coluna = obtem_clique(posicao)
                controlador.gerencia_clique(linha, coluna)
        controlador.atualiza_jogo()
        
    pygame.quit()
    
main()