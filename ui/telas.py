import pygame
from config import *
from functions import *
from .botao import Botao
from classes.controlador import Controlador

def tela_vencedor(tela, vencedor):
    fechar_tela = False
    while not fechar_tela:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                fechar_tela = True

        # Definir cor da tela com base no resultado
        if vencedor == ROSA:
            cor_tela = ROSA
        elif vencedor == BRANCO:
            cor_tela = BRANCO
        else:
            cor_tela = AZUL_CLARO
        tela.fill(cor_tela)

        # Retangulo azul escuro
        pygame.draw.rect(tela, AZUL_ESCURO, (0, ((TELA_ALTURA-350)//2), TELA_LARGURA, 350))

        # Texto de vencedor
        if vencedor == BRANCO:
            texto = 'BRANCO VENCEU!'
        elif vencedor == ROSA:
            texto = 'ROSA VENCEU!'
        else:
            texto = 'EMPATE'
        render_texto = PRINCIPAL.render(texto, True, BRANCO)

        if vencedor == ROSA or vencedor == BRANCO:
            tela.blit(render_texto, (TELA_LARGURA//2 - render_texto.get_width()//2, (TELA_ALTURA//2 + 25) - render_texto.get_height()//2))
            # Estrelas
            tela.blit(ESTRELAS, (TELA_LARGURA//2 - ESTRELAS.get_width()//2, (TELA_ALTURA//2 - 60) - ESTRELAS.get_height()//2))
            # Texto sair
            texto_sair = LETRA_PEQUENA.render('CLIQUE EM QUALQUER TECLA PARA VOLTAR AO MENU.', True, BRANCO)
            tela.blit(texto_sair, (TELA_LARGURA//2 - texto_sair.get_width()//2, (TELA_ALTURA//2 + 85) - texto_sair.get_height()//2))
        else:
            tela.blit(render_texto, (TELA_LARGURA//2 - render_texto.get_width()//2, TELA_ALTURA//2 - render_texto.get_height()//2))
            # Texto sair
            texto_sair = LETRA_PEQUENA.render('CLIQUE EM QUALQUER TECLA PARA VOLTAR AO MENU.', True, BRANCO)
            tela.blit(texto_sair, (TELA_LARGURA//2 - texto_sair.get_width()//2, (TELA_ALTURA//2 + 50) - texto_sair.get_height()//2))
                
        pygame.display.update()

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


        # Background e Tabuleiro
        tela.blit(BG_TELA_JOGO, (0, 0))
        tela.blit(tabuleiro, rect)

        # Textos
        rosas_restantes = controlador.tabuleiro.pecas_rosas
        brancas_restantes = controlador.tabuleiro.pecas_brancas
        
        pontuacao_placar(rosas_restantes, brancas_restantes, tela)
        cor = controlador.turno
        turno(tela, cor)

        # Verifica se o jogo terminou
        if controlador.vencedor is not None:
            tela_vencedor(tela, controlador.vencedor)
            return

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