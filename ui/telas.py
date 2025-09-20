import pygame
from config import *
from functions import *
from .botao import Botao
from classes.controlador import Controlador
from classes.tabuleiro import Tabuleiro

# FUNCAO APENAS PARA TESTE
def tela_vencedor(tela, vencedor):
    tela.fill(AZUL_CLARO)
    fonte = pygame.font.SysFont('Montserrat', 40)
    if vencedor == BRANCO:
        texto = 'BRANCO VENCEU!'
    elif vencedor == ROSA:
        texto = 'ROSA VENCEU!'
    else:
        texto = 'EMPATE'
    render_texto = fonte.render(texto, True, ROSA)
    tela.blit(render_texto, (TELA_LARGURA//2 - render_texto.get_width()//2, TELA_ALTURA//2 - render_texto.get_height()//2))

def tela_jogo(tela, tabuleiro):
    clock = pygame.time.Clock()
    rect = tabuleiro.get_rect(topleft=(101, 100))
    controlador = Controlador(tabuleiro)
    
    fechar_tela = False
    while not fechar_tela:
        # Voltar ao menu ou sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_tela = True
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                resultado = obtem_clique(posicao, (LARGURA, ALTURA), offset=(101, 100))
                if resultado != None:
                    linha, coluna = resultado
                    controlador.gerencia_clique(linha, coluna)
                else:
                    pass # Clique fora do tabuleiro pode ignora

        controlador.atualiza_jogo()

        # Background e Tabuleiro
        tela.blit(BG_TELA_JOGO, (0, 0))
        tela.blit(tabuleiro, rect)

        # Textos
        rosas_restantes = controlador.tabuleiro.pecas_rosas
        brancas_restantes = controlador.tabuleiro.pecas_brancas
        
        pontuacao_placar(rosas_restantes, brancas_restantes, tela)
        cor = controlador.turno
        turno(tela, cor)

        if brancas_restantes == 0 or rosas_restantes == 0:
            tela_vencedor(tela, controlador.vencedor)

        clock.tick(FPS)
        pygame.display.update()

def tela_regras(tela):
    fechar_tela = False
    while not fechar_tela:
        # Voltar ao menu ou sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_tela = True
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                fechar_tela = True

        tela.blit(BG_TELA_REGRAS, (0, 0))
        pygame.display.update()
        

def tela_inicial(tela, tabuleiro):
    rodando = True
    while rodando:
        tela.blit(BG_TELA_INICIAL, (0, 0))
        posicao_mouse_menu = pygame.mouse.get_pos()

        posicao_x = (TELA_LARGURA // 2) - 90

        # Adiciona logo na tela
        retangulo_logo = LOGO.get_rect(center=(posicao_x, 150))
        logo = tela.blit(LOGO, retangulo_logo)

        # Adiciona os botões na tela
        botao_jogar = Botao(BOTAO_JOGAR, (posicao_x, 300))
        botao_regras = Botao(BOTAO_REGRAS, (posicao_x, 392)) # 300 + 62 + 30
        botao_sair = Botao(BOTAO_SAIR, (posicao_x, 484)) # 300 + 62 + 62 + 60

        for botao in [botao_jogar, botao_regras, botao_sair]:
            botao.atualizar(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.verifica_posicao(posicao_mouse_menu):
                    tela_jogo(tela, tabuleiro) 
                if botao_regras.verifica_posicao(posicao_mouse_menu):
                    tela_regras(tela)
                if botao_sair.verifica_posicao(posicao_mouse_menu):
                    rodando = False
        pygame.display.update()
    pygame.quit()