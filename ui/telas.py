import pygame
from config import *
from .botao import Botao

#tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Damas Brasileiras')

# Backgrounds
bg_tela_incial = pygame.image.load('assets/images/bg_tela_inicial.png')
bg_tela_regras = pygame.image.load('assets/images/bg_tela_regras.png')
bg_tela_jogo = pygame.image.load('assets/images/bg_tela_jogo.png')

def tela_jogo(tela):
    rodando = True
    while rodando:
        tela.tela.blit(bg_tela_jogo, (0, 0))

        # Sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False


def tela_regras(tela):
    rodando = True
    while rodando:
        tela.tela.blit(bg_tela_regras, (0, 0))

        # Voltar ao menu ou sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento == pygame.KEYDOWN:
                tela_inicial()

        pygame.display.update()
        

def tela_inicial(tela):
    rodando = True
    while rodando:
        tela.blit(bg_tela_incial, (0, 0))
        posicao_mouse_menu = pygame.mouse.get_pos()

        botao_jogar = Botao(BOTAO_JOGAR, (TELA_LARGURA // 2, 150))
        botao_regras = Botao(BOTAO_REGRAS, (TELA_LARGURA // 2, 300))
        botao_sair = Botao(BOTAO_SAIR, (TELA_LARGURA // 2, 450))

        for botao in [botao_jogar, botao_regras, botao_sair]:
            botao.atualizar(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.verifica_posicao(posicao_mouse_menu):
                    tela_jogo() 
                if botao_regras.verifica_posicao(posicao_mouse_menu):
                    tela_regras()
                if botao_sair.verifica_posicao(posicao_mouse_menu):
                    rodando = False

        pygame.display.update()