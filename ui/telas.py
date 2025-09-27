import pygame
from utils.config import *
from utils.complementos import *
from utils.interface import *
from .botao import Botao
from classes.controlador import Controlador

def tela_pause(tela, frame, som_ligado, controlador, modo, tempo):
    """### Tira um print da tela e mostra que o jogo foi pausado."""
    PAUSE.play()
    clock = pygame.time.Clock()
    if som_ligado:
        img_som = SOM_ON
    else:
        img_som = SOM_OFF
    parar_musica(modo)

    while True:
        clock.tick(FPS)
        tela.blit(frame, (0, 0))
        
        # Sobreposição
        sobreposicao = pygame.Surface((TELA_LARGURA, TELA_ALTURA), pygame.SRCALPHA)
        sobreposicao.fill((0, 0, 0, 160))
        tela.blit(sobreposicao, (0, 0))

        # Desenha o pop-up
        pygame.draw.rect(tela, BRANCO, (((TELA_LARGURA-500)//2), ((TELA_ALTURA-380)//2), 500, 380), 0, 10)
        pygame.draw.rect(tela, AZUL_CLARO, (((TELA_LARGURA-480)//2), ((TELA_ALTURA-360)//2), 480, 360), 3, 10)
        tela.blit(PAUSADO, (((TELA_LARGURA-PAUSADO.get_width())//2), (TELA_ALTURA-280)//2))

        # Botões
        bt_reiniciar = tela.blit(BOTAO_REINICIAR, (((TELA_LARGURA-25-(BOTAO_REINICIAR.get_width()+BOTAO_REGRAS_2.get_width()))//2), ((TELA_ALTURA-15)//2)))
        bt_regras = tela.blit(BOTAO_REGRAS_2, (((TELA_LARGURA+25-(BOTAO_REINICIAR.get_width()-BOTAO_REGRAS_2.get_width()))//2), ((TELA_ALTURA-15)//2)))

        bt_som = tela.blit(img_som, (((TELA_LARGURA-25-(BOTAO_REINICIAR.get_width()+BOTAO_REGRAS_2.get_width()))//2), ((TELA_ALTURA-15+82+50)//2)))
        bt_sair = tela.blit(BOTAO_SAIR_2, (((TELA_LARGURA+25-(BOTAO_REINICIAR.get_width()-BOTAO_REGRAS_2.get_width()))//2), ((TELA_ALTURA-15+82+50)//2)))

        # Texto voltar ao jogo
        texto_sair = LETRA_PEQUENA.render('CLIQUE NA TECLA "P" PARA VOLTAR AO JOGO', True, AZUL_ESCURO)
        tela.blit(texto_sair, ((TELA_LARGURA - texto_sair.get_width())//2, (TELA_ALTURA - 160) - texto_sair.get_height()//2))

        rosas_restantes = controlador.tabuleiro.rosas_totais
        brancas_restantes = controlador.tabuleiro.brancas_totais

        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if bt_reiniciar.collidepoint(pos):
                    # Contagem regressiva
                    if modo == 'tempo':
                        if contagem_regressiva(tela):
                            return  
                    MOUSE_CLICK.play()
                    controlador.resetar_jogo(modo, tempo)
                    return 'reiniciar', som_ligado
                if bt_som.collidepoint(pos):
                    MOUSE_CLICK.play()
                    if som_ligado:
                        parar_musica(modo)
                        img_som = SOM_OFF 
                        som_ligado = False
                    else:
                        img_som = SOM_ON
                        som_ligado = True
                elif bt_regras.collidepoint(pos):
                    MOUSE_CLICK.play()
                    if not tela_regras(tela):
                        return 'fechar', som_ligado
                elif bt_sair.collidepoint(pos):
                    MOUSE_CLICK.play()
                    return 'sair_menu', som_ligado
                    
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                PAUSE.play()
                return 'continuar', som_ligado
            if evento.type == pygame.QUIT:
                escolha = tela_pop_up(tela, frame, rosas_restantes, brancas_restantes)
                if escolha == "sair":
                    return 'fechar', som_ligado

        pygame.display.update()

def tela_pop_up(tela, frame, rosas_restantes, brancas_restantes):
    """ ### Pop-up mostrado para confirmar a desistencia."""
    POPUP.play()
    clock = pygame.time.Clock()
    mostrar = True
    escolha = None

    while mostrar:
        clock.tick(FPS)
        tela.blit(frame, (0, 0))

        # Sobreposição
        sobreposicao = pygame.Surface((TELA_LARGURA, TELA_ALTURA), pygame.SRCALPHA)
        sobreposicao.fill((0, 0, 0, 160))
        tela.blit(sobreposicao, (0, 0))

        # Desenha o pop-up
        pygame.draw.rect(tela, BRANCO, (((TELA_LARGURA-500)//2), ((TELA_ALTURA-380)//2), 500, 380), 0, 10)
        pygame.draw.rect(tela, AZUL_ESCURO, (((TELA_LARGURA-480)//2), ((TELA_ALTURA-360)//2), 480, 360), 3, 10)
        tela.blit(ATENCAO, (((TELA_LARGURA-ATENCAO.get_width())//2), (TELA_ALTURA-300)//2))

        # Textos
        texto1 = LETRA_PEQUENA.render('TEM CERTEZA QUE QUER DESISTIR DO JOGO?', True, AZUL_ESCURO)
        texto2 = LETRA_PEQUENA.render('VOCÊ PERDERÁ TODO O SEU PROGRESSO.', True, AZUL_ESCURO)
        texto3 = LETRA_REGULAR.render('PLACAR ATUAL', True, AZUL_ESCURO)
        texto4 = LETRA_REGULAR.render(f'ROSA: {rosas_restantes}    BRANCO: {brancas_restantes}', True, AZUL_ESCURO)
        tela.blit(texto1, (((TELA_LARGURA-texto1.get_width())//2), ((TELA_ALTURA-100)//2)))
        tela.blit(texto2, (((TELA_LARGURA-texto2.get_width())//2), ((TELA_ALTURA-60)//2)))
        tela.blit(texto3, (((TELA_LARGURA-texto3.get_width())//2), ((TELA_ALTURA+20)//2)))
        tela.blit(texto4, (((TELA_LARGURA-texto4.get_width())//2), ((TELA_ALTURA+60)//2)))

        # Botões
        bt_continuar = tela.blit(BOTAO_CONTINUAR, (((TELA_LARGURA-50-(BOTAO_CONTINUAR.get_width()+BOTAO_SAIR_2.get_width()))//2), ((TELA_ALTURA+180)//2)))
        bt_sair = tela.blit(BOTAO_SAIR_2, (((TELA_LARGURA+50-(BOTAO_CONTINUAR.get_width()-BOTAO_SAIR_2.get_width()))//2), ((TELA_ALTURA+180)//2)))

        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bt_continuar.collidepoint(pos):
                    MOUSE_CLICK.play()
                    mostrar = False
                    escolha = "continuar"
                if bt_sair.collidepoint(pos):
                    MOUSE_CLICK.play()
                    mostrar = False
                    escolha = "sair"

        pygame.display.update()
    return escolha

def tela_fim(tela, vencedor):
    """Mostra o resultado final da partida."""
    clock = pygame.time.Clock()
    fechar_tela = False

    # Música 
    if vencedor == 'nenhum':
        GAME_OVER_TROMBONE.play()
    else:
        EMPATE.play()

    while not fechar_tela:
        clock.tick(FPS)
        if vencedor == BRANCO:
            texto, cor_tela = 'BRANCO VENCEU!', BRANCO
        elif vencedor == ROSA:
            texto, cor_tela = 'ROSA VENCEU!', ROSA
        elif vencedor == 'nenhum':
            texto, cor_tela = 'TEMPO ESGOTADO!', VERMELHO
        else:
            texto, cor_tela = 'EMPATE', AZUL_CLARO
            
        tela.fill(cor_tela)
        render_texto = PRINCIPAL.render(texto, True, BRANCO)

        # Mensagem para voltar ao menu
        instrucao = LETRA_PEQUENA.render('CLIQUE NA TECLA "M" PARA VOLTAR AO MENU', True, BRANCO)

        # Retângulo azul escuro 
        pygame.draw.rect(tela, AZUL_ESCURO, (0, (TELA_ALTURA - 350) // 2, TELA_LARGURA, 350))

        centro_x, centro_y = TELA_LARGURA//2, TELA_ALTURA//2
        if vencedor in (ROSA, BRANCO):
            tela.blit(ESTRELAS, (centro_x - ESTRELAS.get_width() // 2, centro_y - 60 - ESTRELAS.get_height() // 2))
            tela.blit(render_texto, (centro_x - render_texto.get_width() // 2, centro_y + 25 - render_texto.get_height() // 2))
            tela.blit(instrucao, (centro_x - instrucao.get_width() // 2, centro_y + 85 - instrucao.get_height() // 2))
        else:
            tela.blit(render_texto,(centro_x - render_texto.get_width() // 2,centro_y - render_texto.get_height() // 2))
            tela.blit(instrucao, (centro_x - instrucao.get_width() // 2, centro_y + 50 - instrucao.get_height() // 2))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_tela = True
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_m:
                fechar_tela = True

        pygame.display.update()

def tela_jogo(tela, tabuleiro, modo, tempo=None):
    """### Mostra a tela de jogo baseada no modo escolhido."""
    clock = pygame.time.Clock()
    rect = tabuleiro.get_rect(topleft=(101, 100))

    # Contagem regressiva
    if modo == 'tempo':
        if contagem_regressiva(tela):
            return  
    
    controlador = Controlador(tabuleiro)
    controlador.resetar_jogo(modo, tempo)
    som_ligado = True
    tocar_musica(modo, som_ligado)

    try:
        fechar_tela = False
        while not fechar_tela:
            clock.tick(FPS)

            # BACKGROUND E TABULEIRO
            tela.blit(BG_TELA_JOGO, (0, 0))
            tela.blit(tabuleiro, rect)

            rosas_restantes = controlador.tabuleiro.rosas_totais
            brancas_restantes = controlador.tabuleiro.brancas_totais

            # TEXTOS PLACAR
            pontuacao_placar(rosas_restantes, brancas_restantes, tela)
            cor = controlador.turno
            turno(tela, cor)

            # Texto para pausar
            texto_sair = LETRA_PEQUENA.render('CLIQUE NA TECLA "P" PARA PAUSAR O JOGO', True, BRANCO)
            tela.blit(texto_sair, ((TELA_LARGURA - texto_sair.get_width() - TELA_ALTURA//2)//2, (TELA_ALTURA - 30) - texto_sair.get_height()//2))

            # Verifica se o jogo terminou: se sim, retorna o vencedor
            if controlador.vencedor is not None:
                parar_musica(modo)
                tela_fim(tela, controlador.vencedor)
                return
            
            if controlador.modo == 'tempo':
                agora = pygame.time.get_ticks() // 1000
                segundos_passados = (agora - controlador.inicio) - controlador.tempo_pausado
                segundos_restantes = controlador.tempo_restante - segundos_passados

                if segundos_restantes < 0:
                    segundos_restantes = 0

                # Se acabar o tempo, fim de jogo (nenhum vencedor)
                if segundos_restantes <= 0:
                    parar_musica(modo)
                    tela_fim(tela, 'nenhum')
                    return
                
                # Define a cor do tempo: quando atingir 1min, ele fica rosa
                cor_tempo = AZUL_ESCURO
                if segundos_restantes <= 60:
                    cor_tempo = ROSA
                timer(tela, cor_tempo, segundos_restantes)

            for evento in pygame.event.get():
                # Gerenciamento do tabuleiro
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicao = pygame.mouse.get_pos()
                    resultado = obtem_clique(posicao, (LARGURA_TABULEIRO, ALTURA_TABULEIRO), offset=(101, 100))
                    if resultado is not None:
                        linha, coluna = resultado
                        controlador.gerencia_clique(linha, coluna)

                if evento.type == pygame.QUIT:
                    # Se o usuário quiser sair, mostra a tela de pop-up
                    POPUP.play()
                    parar_musica(modo)
                    print_pop_up = tela.copy()
                    if modo =='tempo':
                        tempo_inicio_pausa = pygame.time.get_ticks() // 1000
                        escolha = tela_pop_up(tela, print_pop_up, rosas_restantes, brancas_restantes)
                        tempo_fim_pausa = pygame.time.get_ticks() // 1000
                        controlador.tempo_pausado += (tempo_fim_pausa - tempo_inicio_pausa)
                    else:
                        escolha = tela_pop_up(tela, print_pop_up, rosas_restantes, brancas_restantes)
                    tocar_musica(modo, som_ligado)
                    if escolha == "sair":
                        fechar_tela = True

                # Gerenciamento do pause
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                    PAUSE.play()
                    parar_musica(modo)
                    if modo == 'tempo':
                        tempo_inicio_pausa = pygame.time.get_ticks() // 1000

                    print_pausa = tela.copy()
                    acao_retorno, som_ligado = tela_pause(tela, print_pausa, som_ligado, controlador, modo, tempo) # Pausa o jogo

                    # Se o modo for "tempo", calcula pausa
                    if modo == 'tempo' and acao_retorno == 'continuar':
                        tempo_fim_pausa = pygame.time.get_ticks() // 1000
                        controlador.tempo_pausado += (tempo_fim_pausa - tempo_inicio_pausa)

                    if acao_retorno in ('sair_menu', 'fechar'):
                        fechar_tela = True
                    elif som_ligado:
                        tocar_musica(modo, som_ligado)
                    
            controlador.atualiza_jogo()
            pygame.display.update()
    finally:
        parar_musica(modo)

def tela_modo_jogo(tela):
    """### Dispõe ao usuário dois modos de jogo.
    -'normal' ou 'tempo'"""
    clock = pygame.time.Clock()
    modo = None 
    tempo = None
    ultimo_hover = None

    fechar_tela = False
    while not fechar_tela:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()

        # BACKGROUND E TEXTO
        tela.blit(BG_MODO_JOGO, (0, 0))
        tela.blit(MODO_JOGO, ((TELA_LARGURA-MODO_JOGO.get_width())//2, (TELA_ALTURA-MODO_JOGO.get_width()-80)//2))

        # BOTOES
        botao_normal = tela.blit(BOTAO_NORMAL, (((TELA_LARGURA-BOTAO_NORMAL.get_width()) // 2), ((TELA_ALTURA-50)//2)))
        botao_tempo = tela.blit(BOTAO_TEMPO, (((TELA_LARGURA-BOTAO_TEMPO.get_width()) // 2), ((TELA_ALTURA+130)//2)))

        # TEMPOS
        # Posições
        x1 = (TELA_LARGURA - 260 - (BOTAO_NORMAL.get_width() - BOTAO_TEMPO.get_width())) // 2
        x2 = (TELA_LARGURA + 20 - (BOTAO_NORMAL.get_width() - BOTAO_TEMPO.get_width())) // 2
        y1 = (TELA_ALTURA + BOTAO_TEMPO.get_height() + 230) // 2
        y2 = (TELA_ALTURA + BOTAO_TEMPO.get_height() + 365) // 2

        # Bases
        base_min3 = pygame.Rect(x1, y1, 120, 45)
        base_min5 = pygame.Rect(x2, y1, 120, 45)
        base_min10 = pygame.Rect(x1, y2, 120, 45)
        base_min15 = pygame.Rect(x2, y2, 120, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_tela = True
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_normal.collidepoint(pos): 
                    MOUSE_CLICK.play()
                    fechar_tela = True
                    modo = 'normal'
                elif botao_tempo.collidepoint(pos):
                    MOUSE_CLICK.play()
                    modo = 'tempo'
                elif modo == 'tempo':
                    tempos_botoes = [(3, base_min3), (5, base_min5), (10, base_min10), (15, base_min15)]
                    for minutos, base in tempos_botoes:
                        if base.collidepoint(evento.pos):
                            tempo = minutos
                            fechar_tela = True
                            break

        # Somente se o modo de tempo for selecionado, aparecem as opções de tempo
        if modo == 'tempo':
            ultimo_hover = tempos(tela, pos, base_min3, base_min5, base_min10, base_min15, ultimo_hover)
        pygame.display.update()
        
    if modo == 'tempo' and tempo is None:
        return None, None
    return modo, tempo

def tela_regras(tela):
    """###Mostra a tela de regras do jogo."""
    while True:
        tela.blit(BG_TELA_REGRAS, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                return True
        
        pygame.display.update()

def tela_inicial(tela, tabuleiro):
    """### Mostra a tela inicial do jogo."""
    MUSICA_INICIAL.play(-1)

    rodando = True
    while rodando:
        tela.blit(BG_TELA_INICIAL, (0, 0))
        posicao_mouse_menu = pygame.mouse.get_pos()
        posicao_x = (TELA_LARGURA // 2) - 90

        # Adiciona logo na tela
        retangulo_logo = LOGO.get_rect(center=(posicao_x, 150))
        tela.blit(LOGO, retangulo_logo)

        # Adiciona os botões na tela
        botao_jogar = Botao(BOTAO_JOGAR, (posicao_x, 300))
        botao_regras = Botao(BOTAO_REGRAS, (posicao_x, 392))
        botao_sair = Botao(BOTAO_SAIR, (posicao_x, 484))
        for botao in [botao_jogar, botao_regras, botao_sair]:
            botao.atualizar(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Tela de jogo
                if botao_jogar.verifica_posicao(posicao_mouse_menu):
                    MOUSE_CLICK.play()
                    MUSICA_INICIAL.fadeout(500)
                    modo, tempo = tela_modo_jogo(tela)
                    if modo == 'normal':
                        tela_jogo(tela, tabuleiro, modo)
                    elif modo == 'tempo':
                        tela_jogo(tela, tabuleiro, modo, tempo)
                    MUSICA_INICIAL.play(-1)

                # Tela de Regras
                elif botao_regras.verifica_posicao(posicao_mouse_menu):
                    MOUSE_CLICK.play()
                    if not tela_regras(tela):
                        return False
                # Sair 
                elif botao_sair.verifica_posicao(posicao_mouse_menu):
                    MOUSE_CLICK.play()
                    rodando = False
        pygame.display.update()