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