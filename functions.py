from config import *

def obtem_clique(pos):
    x, y = pos
    linha = y // TAMANHO_QUADRADO
    coluna = x // TAMANHO_QUADRADO
    return linha, coluna

def desenha_texto(texto, fonte, cor, x, y, tela):
	img = fonte.render(texto, True, cor)
	tela.blit(img, (x, y))