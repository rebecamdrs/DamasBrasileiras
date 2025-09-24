import pygame
pygame.font.init()

''' GERAL'''
FPS = 60
LETRA_REGULAR = pygame.font.Font('assets/font/Montserrat-Regular.ttf', 15)
LETRA_PEQUENA = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 15)
LETRA_MEDIA = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 18)
LETRA_PLACAR = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 22)
LETRA_GRANDE = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 24)
LETRA_BIG = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 32)
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
VERMELHO = (255, 0, 0)

''' DIMENSÕES '''
# Tabuleiro
LARGURA_TABULEIRO, ALTURA_TABULEIRO = 400, 400
LINHAS, COLUNAS = 8, 8
TAMANHO_QUADRADO = LARGURA_TABULEIRO // COLUNAS

# Telas
TELA_ALTURA, TELA_LARGURA = 600, 900

''' IMAGENS '''
# Peças
PECA_ROSA = pygame.transform.scale(pygame.image.load('assets/images/peca_rosa.png'), (36, 36))
PECA_BRANCA = pygame.transform.scale(pygame.image.load('assets/images/peca_branca.png'), (36, 36))
DAMA_ROSA = pygame.transform.scale(pygame.image.load('assets/images/dama_rosa.png'), (36, 36))
DAMA_BRANCA = pygame.transform.scale(pygame.image.load('assets/images/dama_branca.png'), (36, 36))

# Textos
LOGO = pygame.transform.scale(pygame.image.load('assets/images/logo.png'), (329, 149.75))
ATENCAO = pygame.transform.scale(pygame.image.load('assets/images/atencao.png'), (238, 86.32))

# Estrelas
ESTRELAS = pygame.transform.scale(pygame.image.load('assets/images/estrelas.png'), (198.78, 80.25))
TIMER = pygame.transform.scale(pygame.image.load('assets/images/timer.png'), (150, 40))

# Botões
BOTAO_JOGAR = pygame.transform.scale(pygame.image.load('assets/images/botao_jogar.png'), (280, 62))
BOTAO_REGRAS = pygame.transform.scale(pygame.image.load('assets/images/botao_regras.png'), (280, 62))
BOTAO_SAIR = pygame.transform.scale(pygame.image.load('assets/images/botao_sair.png'), (280, 65))
BOTAO_CONTINUAR = pygame.transform.scale(pygame.image.load('assets/images/bt_continuar.png'), (156, 42))
BOTAO_SAIR_2 = pygame.transform.scale(pygame.image.load('assets/images/bt_sair.png'), (156, 42))
BOTAO_NORMAL = pygame.transform.scale(pygame.image.load('assets/images/botao_normal.png'), (280, 62))
BOTAO_TEMPO = pygame.transform.scale(pygame.image.load('assets/images/botao_tempo.png'), (280, 62))

# Backgrounds 
BG_TELA_INICIAL = pygame.image.load('assets/images/bg_tela_inicial.png')
BG_TELA_REGRAS = pygame.image.load('assets/images/bg_tela_regras.png')
BG_TELA_JOGO = pygame.image.load('assets/images/bg_tela_jogo.png')