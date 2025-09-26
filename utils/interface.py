from utils.config import *
from utils.complementos import *

def desenhar_placar(valor, posicao, superficie_tela, mostrar_capturadas=False):
    """ Desenha um valor no placar na tela. """
    # Calcula o valor que será exibido
    if mostrar_capturadas:
        valor_exibido = 12 - valor
    else:
        valor_exibido = valor

    retangulo_base = pygame.Rect(posicao[0], posicao[1], 35, 30)
    texto = LETRA_PLACAR.render(str(valor_exibido), True, BRANCO)
    retangulo_texto = texto.get_rect(center=retangulo_base.center)
    superficie_tela.blit(texto, retangulo_texto)

def pontuacao_placar(rosas_restantes, brancas_restantes, tela):
    """ Mostra as pontuações do placar na tela. """
    # PLACAR ROSA
    desenhar_placar(rosas_restantes, (792, 92), tela)           # Rosas restantes
    desenhar_placar(brancas_restantes, (792, 153), tela, True)  # Brancas capturadas

    # PLACAR BRANCO
    desenhar_placar(brancas_restantes, (792, 418), tela)        # Brancas restantes
    desenhar_placar(rosas_restantes, (792, 478), tela, True)    # Rosas capturadas

def turno(tela, cor):
    """ Mostra o turno atual na tela. """
    # Label "TURNO"
    label_turno = LETRA_GRANDE.render('TURNO', True, BRANCO)
    tela.blit(label_turno, (710, 270))
    
    # Texto do turno baseado na cor 
    turno = 'ROSA'
    if cor == BRANCO: 
        turno = 'BRANCO'
    base_turno = pygame.Rect(742, 265, 30, 100) 
    texto_turno = LETRA_GRANDE.render(turno, True, cor) 
    rect_turno = texto_turno.get_rect(center=base_turno.center) 
    tela.blit(texto_turno, rect_turno) 

def tempos(tela, pos, base1, base2, base3, base4):
    """ Mostra os botões de tempo na tela. """
    botoes = [(base1, '5 MIN'), (base2, '10 MIN'), (base3, '30 MIN'), (base4, '60 MIN')]
    for base, texto in botoes:
        if base.collidepoint(pos):
            cor = CINZA_CLARO
        else:
            cor = CINZA
        # Fundo do botão
        pygame.draw.rect(tela, cor, base, border_radius=6)
        # Texto do botão
        txt_render = LETRA_MEDIA.render(texto, True, BRANCO)
        rect_txt = txt_render.get_rect(center=base.center)
        tela.blit(txt_render, rect_txt)

def timer(tela, cor_tempo, segundos_restantes):
    """ Mostra o temporizador na tela. """
    # Formata os segundos
    tempo_formatado = formatar_tempo(segundos_restantes)

    # Coloca a base do timer
    tela.blit(TIMER, ((TELA_LARGURA-(TIMER.get_width()+381)), (70-TIMER.get_height())))

    # Coloca o tempo do timer
    temporizador = LETRA_PLACAR.render(tempo_formatado, True, cor_tempo)
    base_temporizador = pygame.Rect((TELA_LARGURA-(TIMER.get_width()-80+381)), (70-(TIMER.get_height()+33)), 28, 105)
    rect_temporizador = temporizador.get_rect(center=base_temporizador.center)
    tela.blit(temporizador, rect_temporizador)