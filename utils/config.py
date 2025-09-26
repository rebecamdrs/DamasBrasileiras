import pygame
pygame.font.init()
pygame.mixer.init()

''' GERAL '''
FPS = 60
LETRA_REGULAR = pygame.font.Font('assets/font/Montserrat-SemiBold.ttf', 15)
LETRA_PEQUENA = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 15)
LETRA_MEDIA = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 18)
LETRA_PLACAR = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 22)
LETRA_GRANDE = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 24)
LETRA_BIG = pygame.font.Font('assets/font/Montserrat-ExtraBold.ttf', 32)
PRINCIPAL = pygame.font.Font('assets/font/CrunchChips.ttf', 76)

''' SONS '''
MUSICA_INICIAL = pygame.mixer.Sound('assets/sounds/game-music-loop.mp3')
MUSICA_TEMPO = pygame.mixer.Sound('assets/sounds/music-loop-time.mp3')
MUSICA_NORMAL = pygame.mixer.Sound('assets/sounds/music-loop-normal.mp3')

MOUSE_CLICK = pygame.mixer.Sound('assets/sounds/click.mp3')
MOVE = pygame.mixer.Sound('assets/sounds/move.wav')
PAUSE = pygame.mixer.Sound('assets/sounds/pause.mp3')
POPUP = pygame.mixer.Sound('assets/sounds/error.mp3')
GAME_OVER_TROMBONE = pygame.mixer.Sound('assets/sounds/game-over-trombone.wav')
EMPATE = pygame.mixer.Sound('assets/sounds/empate.mp3')
INVALIDO = pygame.mixer.Sound('assets/sounds/wrong.mp3') 
HOVER = pygame.mixer.Sound('assets/sounds/hover-botao.mp3') 

# Config dos sons
MUSICA_INICIAL.set_volume(0.3)
MUSICA_TEMPO.set_volume(0.3)
MUSICA_NORMAL.set_volume(0.3)
PAUSE.set_volume(0.3)
POPUP.set_volume(0.3)
GAME_OVER_TROMBONE.set_volume(0.4)
EMPATE.set_volume(0.6)

''' CORES '''
PRETO = (8, 20, 32)
AZUL_ESCURO = (6, 27, 50)
CINZA = (39, 61, 84)
CINZA_CLARO = (87, 105, 125)
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
PAUSADO = pygame.transform.scale(pygame.image.load('assets/images/pausado.png'), (245, 112))

# Estrelas
ESTRELAS = pygame.transform.scale(pygame.image.load('assets/images/estrelas.png'), (198.78, 80.25))
TIMER = pygame.transform.scale(pygame.image.load('assets/images/timer.png'), (150, 40))

# Botões
BOTAO_JOGAR = pygame.transform.scale(pygame.image.load('assets/images/botao_jogar.png'), (280, 62))
BOTAO_REGRAS = pygame.transform.scale(pygame.image.load('assets/images/botao_regras.png'), (280, 62))
BOTAO_SAIR = pygame.transform.scale(pygame.image.load('assets/images/botao_sair.png'), (280, 65))

BOTAO_CONTINUAR = pygame.transform.scale(pygame.image.load('assets/images/bt_continuar.png'), (156, 42))
BOTAO_SAIR_2 = pygame.transform.scale(pygame.image.load('assets/images/bt_sair.png'), (156, 42))
BOTAO_REINICIAR = pygame.transform.scale(pygame.image.load('assets/images/reiniciar.png'), (156, 42))
BOTAO_REGRAS_2 = pygame.transform.scale(pygame.image.load('assets/images/regras.png'), (156, 42))
SOM_ON = pygame.transform.scale(pygame.image.load('assets/images/som_on.png'), (156, 42))
SOM_OFF = pygame.transform.scale(pygame.image.load('assets/images/som_off.png'), (156, 42))

BOTAO_NORMAL = pygame.transform.scale(pygame.image.load('assets/images/botao_normal.png'), (280, 62))
BOTAO_TEMPO = pygame.transform.scale(pygame.image.load('assets/images/botao_tempo.png'), (280, 62))

# Backgrounds 
BG_TELA_INICIAL = pygame.image.load('assets/images/bg_tela_inicial.png')
BG_TELA_REGRAS = pygame.image.load('assets/images/bg_tela_regras.png')
BG_TELA_JOGO = pygame.image.load('assets/images/bg_tela_jogo.png')