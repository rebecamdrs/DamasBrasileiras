from config import *
    
def obtem_clique(posicao, limites_tabuleiro, offset=(0, 0)):
    largura, altura = limites_tabuleiro
    x, y = posicao
    offset_x, offset_y = offset

    x_relativo = x - offset_x
    y_relativo = y - offset_y
    
    if 0 <= x_relativo < largura and 0 <= y_relativo < altura:
        linha = y_relativo // TAMANHO_QUADRADO
        coluna = x_relativo // TAMANHO_QUADRADO
        return linha, coluna
    return None

def pontuacao_placar(rosas_restantes, brancas_restantes, tela):
    '''------------------------- PLACAR ROSA -------------------------'''
    # PEÇAS ROSAS RESTANTES
    base_r_restantes = pygame.Rect(792, 92, 35, 30)
    texto_r_restantes = LETRA_PLACAR.render(str(rosas_restantes), True, BRANCO)
    rect_r_restantes = texto_r_restantes.get_rect(center=base_r_restantes.center)
    tela.blit(texto_r_restantes, rect_r_restantes) 

    # PEÇAS BRANCAS CAPTURADAS
    base_b_capturadas = pygame.Rect(792, 153, 35, 30)
    texto_b_capturadas = LETRA_PLACAR.render(f'{12 - brancas_restantes}', True, BRANCO)
    rect_b_capturadas = texto_b_capturadas.get_rect(center=base_b_capturadas.center)
    tela.blit(texto_b_capturadas, rect_b_capturadas) 

    '''------------------------ PLACAR BRANCO ------------------------'''
    # PEÇAS BRANCAS RESTANTES
    base_b_restantes = pygame.Rect(792, 418, 35, 30)
    texto_b_restantes = LETRA_PLACAR.render(str(brancas_restantes), True, BRANCO)
    rect_b_restantes = texto_b_restantes.get_rect(center=base_b_restantes.center)
    tela.blit(texto_b_restantes, rect_b_restantes) 

    # PEÇAS ROSAS CAPTURADAS
    base_r_capturadas = pygame.Rect(792, 478, 35, 30)
    texto_r_capturadas = LETRA_PLACAR.render(f'{12 - rosas_restantes}', True, BRANCO)
    rect_r_capturadas = texto_r_capturadas.get_rect(center=base_r_capturadas.center)
    tela.blit(texto_r_capturadas, rect_r_capturadas)

def turno(tela, cor):
    label_turno = LETRA_GRANDE.render('TURNO', True, BRANCO)
    if cor == BRANCO: 
        turno = 'BRANCO'
    else:
        turno = 'ROSA'
    base_turno = pygame.Rect(740, 265, 30, 100) # base para centralizar
    texto_turno = LETRA_GRANDE.render(turno, True, cor) # texto
    rect_turno = texto_turno.get_rect(center=base_turno.center) # base para movimentar o texto e centralizar na base
    tela.blit(label_turno, (700, 270)) 
    tela.blit(texto_turno, rect_turno) 