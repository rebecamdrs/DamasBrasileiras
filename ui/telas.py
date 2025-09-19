import pygame
from config import *
from functions import *
from .botao import Botao
from classes.controlador import Controlador
from classes.tabuleiro import Tabuleiro

def tela_jogo(tela):
    controlador = Controlador(tela)
    clock = pygame.time.Clock()

    tabuleiro = pygame.Surface((LARGURA, ALTURA))
    tabuleiro.fill(CINZA)
    rect = tabuleiro.get_rect()
    
    fechar_tela = False
    while not fechar_tela:
        # Voltar ao menu ou sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_tela = True
                pygame.quit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                linha, coluna = obtem_clique(posicao)
                controlador.gerencia_clique(linha, coluna)

        # Background e Tabuleiro
        tela.blit(BG_TELA_JOGO, (0, 0))
        tela.blit(tabuleiro, rect)

        # Textos
        tabuleiro_objeto = Tabuleiro()
        rosas_restantes, brancas_restantes = tabuleiro_objeto.retorna_qnt_pecas()
        
        """
        rosas_restantes = controlador.tabuleiro.pecas_rosas
        brancas_restantes = controlador.tabuleiro.pecas_brancas
        """
        
        desenha_texto(str(rosas_restantes), FONTE_PLACAR, BRANCO, 798, 94, tela) # peças rosas restantes
        desenha_texto(str(12 - brancas_restantes), FONTE_PLACAR, BRANCO, 798, 155, tela) # peças brancas capturadas
        desenha_texto(str(brancas_restantes), FONTE_PLACAR, BRANCO, 798, 420, tela) # peças brancas restantes
        desenha_texto(str(12 - rosas_restantes), FONTE_PLACAR, BRANCO, 798, 480, tela) # peças rosas capturadas

        desenha_texto('TURNO', FONTE_GRANDE, BRANCO, 695, 270, tela) # turno
        turno, cor = '', ''
        if controlador.turno_atual() == (255, 255, 255):
            turno = 'BRANCO'
            cor = BRANCO
        else:
            turno = 'ROSA'
            cor = ROSA

        """
        cor = controlador.turno
        if cor == BRANCO: 
            turno = 'BRANCO'
        else:
            turno = 'ROSA'
        """

        desenha_texto(turno, FONTE_GRANDE, cor, 707, 300, tela) # cor do turno

        controlador.atualiza_jogo()
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
        

def tela_inicial(tela):
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
                    tela_jogo(tela) 
                if botao_regras.verifica_posicao(posicao_mouse_menu):
                    tela_regras(tela)
                if botao_sair.verifica_posicao(posicao_mouse_menu):
                    rodando = False
        pygame.display.update()
    pygame.quit()