import pygame
pygame.font.init()

''' GERAL'''
FPS = 60
LETRA_PEQUENA = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 14)
LETRA_PLACAR = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 22)
LETRA_GRANDE = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 28)
PRINCIPAL = pygame.font.Font('assets/font/CrunchChips.ttf', 76)

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
TELA_ALTURA, TELA_LARGURA = 600, 900

''' IMAGENS '''
# Peças
PECA_ROSA = pygame.transform.scale(pygame.image.load('assets/images/peca_rosa.png'), (36, 36))
PECA_BRANCA = pygame.transform.scale(pygame.image.load('assets/images/peca_branca.png'), (36, 36))
DAMA_ROSA = pygame.transform.scale(pygame.image.load('assets/images/dama_rosa.png'), (36, 36))
DAMA_BRANCA = pygame.transform.scale(pygame.image.load('assets/images/dama_branca.png'), (36, 36))

# Logo
LOGO = pygame.transform.scale(pygame.image.load('assets/images/logo.png'), (329, 149.75))

# Estrelas
ESTRELAS = pygame.transform.scale(pygame.image.load('assets/images/estrelas.png'), (198.78, 80.25))

# Botões
BOTAO_JOGAR = pygame.transform.scale(pygame.image.load('assets/images/botao_jogar.png'), (280, 62))
BOTAO_REGRAS = pygame.transform.scale(pygame.image.load('assets/images/botao_regras.png'), (280, 62))
BOTAO_SAIR = pygame.transform.scale(pygame.image.load('assets/images/botao_sair.png'), (280, 65))

# Backgrounds 
BG_TELA_INICIAL = pygame.image.load('assets/images/bg_tela_inicial.png')
BG_TELA_REGRAS = pygame.image.load('assets/images/bg_tela_regras.png')
BG_TELA_JOGO = pygame.image.load('assets/images/bg_tela_jogo.png')