import pygame
from utils.config import *
from utils.complementos import *
from utils.interface import *
from .botao import Botao
from classes.controlador import Controlador

def pop_up(tela, frame, rosas_restantes, brancas_restantes):
    """ ### Pop-up mostrado para confirmar a desistencia. """
    clock = pygame.time.Clock()
    mostrar = True
    escolha = None  # "continuar" ou "sair"

    while mostrar:
        clock.tick(FPS)
        tela.blit(frame, (0, 0)) # Tela de fundo(jogo)

        # Sobreposição
        sobreposicao = pygame.Surface((TELA_LARGURA, TELA_ALTURA), pygame.SRCALPHA)
        sobreposicao.fill((0, 0, 0, 200))
        tela.blit(sobreposicao, (0 , 0))

        # Desenha o pop-up
        pygame.draw.rect(tela, BRANCO, (((TELA_LARGURA-500)//2), ((TELA_ALTURA-380)//2), 500, 380), 0, 10)
        pygame.draw.rect(tela, AZUL_ESCURO, (((TELA_LARGURA-490)//2), ((TELA_ALTURA-370)//2), 490, 370), 3, 10)
        tela.blit(ATENCAO, (((TELA_LARGURA-240)//2), (TELA_ALTURA-300)//2))

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
        rect_continuar = tela.blit(BOTAO_CONTINUAR, (((TELA_LARGURA+50-(BOTAO_CONTINUAR.get_width()-BOTAO_SAIR_2.get_width()))//2), ((TELA_ALTURA+160)//2)))
        rect_sair = tela.blit(BOTAO_SAIR_2, (((TELA_LARGURA-50-(BOTAO_CONTINUAR.get_width()+BOTAO_SAIR_2.get_width()))//2), ((TELA_ALTURA+160)//2)))

        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_continuar.collidepoint(pos):
                    mostrar = False
                    escolha = "continuar"
                if rect_sair.collidepoint(pos):
                    mostrar = False
                    escolha = "sair"

        pygame.display.update()
    return escolha

def tela_fim(tela, vencedor):
    """ ### Mostra o resultado final da partida. """
    clock = pygame.time.Clock()
    fechar_tela = False

    while not fechar_tela:
        clock.tick(FPS)

        # Definir cor da tela e o texto com base no resultado
        if vencedor == BRANCO:
            cor_tela = BRANCO
            texto = 'BRANCO VENCEU!'
        elif vencedor == ROSA:
            cor_tela = ROSA
            texto = 'ROSA VENCEU!'
        elif vencedor == 'nenhum':
            cor_tela = VERMELHO
            texto = 'TEMPO ESGOTADO!'
        else:
            cor_tela = AZUL_CLARO
            texto = 'EMPATE'
        tela.fill(cor_tela)
        render_texto = PRINCIPAL.render(texto, True, BRANCO)

        # Retangulo azul escuro
        pygame.draw.rect(tela, AZUL_ESCURO, (0, ((TELA_ALTURA-350)//2), TELA_LARGURA, 350))

        if vencedor == ROSA or vencedor == BRANCO:
            tela.blit(render_texto, (TELA_LARGURA//2 - render_texto.get_width()//2, (TELA_ALTURA//2 + 25) - render_texto.get_height()//2))
            tela.blit(ESTRELAS, (TELA_LARGURA//2 - ESTRELAS.get_width()//2, (TELA_ALTURA//2 - 60) - ESTRELAS.get_height()//2))
            texto_sair = LETRA_PEQUENA.render('CLIQUE NA TECLA "M" PARA VOLTAR AO MENU.', True, BRANCO)
            tela.blit(texto_sair, (TELA_LARGURA//2 - texto_sair.get_width()//2, (TELA_ALTURA//2 + 85) - texto_sair.get_height()//2))
        else:
            tela.blit(render_texto, (TELA_LARGURA//2 - render_texto.get_width()//2, TELA_ALTURA//2 - render_texto.get_height()//2))
            texto_sair = LETRA_PEQUENA.render('CLIQUE NA TECLA "M" PARA VOLTAR AO MENU.', True, BRANCO)
            tela.blit(texto_sair, (TELA_LARGURA//2 - texto_sair.get_width()//2, (TELA_ALTURA//2 + 50) - texto_sair.get_height()//2))

        # Se clicar na tecla "m" fecha a tela e volta para o menu
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_m:
                fechar_tela = True
                
        pygame.display.update()

def tela_modo_jogo(tela):
    """ ### Dispõe ao usuário dois modos de jogo. 
    -'normal' ou 'tempo' """
    clock = pygame.time.Clock()
    modo = None # normal ou tempo
    tempo = None

    fechar_tela = False
    while not fechar_tela:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()

        # FUNDO
        tela.fill(AZUL_ESCURO)
        pygame.draw.rect(tela, ROSA, (0, 0, 30, TELA_ALTURA))
        pygame.draw.rect(tela, AZUL_CLARO, (TELA_LARGURA-30, 0, 30, TELA_ALTURA))

        # TEXTO
        texto = LETRA_BIG.render('MODO DE JOGO', True, BRANCO)
        tela.blit(texto, (((TELA_LARGURA-texto.get_width())//2), ((TELA_ALTURA-200)//2)))

        # BOTOES
        botao_normal = tela.blit(BOTAO_NORMAL, (((TELA_LARGURA-50-(BOTAO_NORMAL.get_width()+BOTAO_TEMPO.get_width())) // 2), ((TELA_ALTURA-50)//2)))
        botao_tempo = tela.blit(BOTAO_TEMPO, (((TELA_LARGURA+50-(BOTAO_NORMAL.get_width()-BOTAO_TEMPO.get_width())) // 2), ((TELA_ALTURA-50)//2)))

        # TEMPOS
        # Posições
        x1 = (TELA_LARGURA + 70 - (BOTAO_NORMAL.get_width() - BOTAO_TEMPO.get_width())) // 2
        x2 = (TELA_LARGURA + 70 + 120 + 160 - (BOTAO_NORMAL.get_width() - BOTAO_TEMPO.get_width())) // 2
        y1 = (TELA_ALTURA + BOTAO_TEMPO.get_height() + 50) // 2
        y2 = (TELA_ALTURA + BOTAO_TEMPO.get_height() + 50 + 45 + 90) // 2

        # Bases
        base_min5 = pygame.Rect(x1, y1, 120, 45)
        base_min10 = pygame.Rect(x2, y1, 120, 45)
        base_min30 = pygame.Rect(x1, y2, 120, 45)
        base_min60 = pygame.Rect(x2, y2, 120, 45)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fechar_tela = True

            # Quando clicado na tela
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Se for o botão de "jogo normal"
                if botao_normal.collidepoint(pos): 
                    fechar_tela = True
                    modo = 'normal'
                # Se for o botão de "jogo com tempo"
                elif botao_tempo.collidepoint(pos):
                    modo = 'tempo'
                # somente se o botao de tempo for selecionado, os botões abaixo podem ser selecionados
                elif modo == 'tempo':
                    if base_min5.collidepoint(evento.pos):
                        tempo = 5
                        fechar_tela = True
                    elif base_min10.collidepoint(evento.pos):
                        tempo = 10
                        fechar_tela = True
                    elif base_min30.collidepoint(evento.pos):
                        tempo = 30
                        fechar_tela = True
                    elif base_min60.collidepoint(evento.pos):
                        tempo = 60
                        fechar_tela = True

        # Somente se o modo de tempo for selecionado, aparecem as opções de tempo
        if modo == 'tempo':
            tempos(tela, pos, base_min5, base_min10, base_min30, base_min60)

        pygame.display.update()
    return modo, tempo

def tela_jogo(tela, tabuleiro, modo, tempo=None):
    """ ### Mostra a tela de jogo baseada no modo escolhido.
    - **Modos**: 'normal' ou 'tempo' """
    clock = pygame.time.Clock()
    rect = tabuleiro.get_rect(topleft=(101, 100))
    controlador = Controlador(tabuleiro)
    
    # Se for modo tempo, converte minutos recebidos em segundos
    if modo == 'tempo' and tempo != None:
        tempo_restante = tempo * 60
        inicio = pygame.time.get_ticks() // 1000
        tempo_pausado = 0
    else:
        tempo_restante = None
        inicio = None
        tempo_pausado = None

    fechar_tela = False
    while not fechar_tela:
        clock.tick(FPS)

        # Background e Tabuleiro
        tela.blit(BG_TELA_JOGO, (0, 0))
        tela.blit(tabuleiro, rect)

        rosas_restantes = controlador.tabuleiro.pecas_rosas
        brancas_restantes = controlador.tabuleiro.pecas_brancas

        # TEXTOS PLACAR
        pontuacao_placar(rosas_restantes, brancas_restantes, tela)
        cor = controlador.turno
        turno(tela, cor)

        # Texto para pausar
        texto_sair = LETRA_PEQUENA.render('CLIQUE NA TECLA "P" PARA PAUSAR O JOGO.', True, BRANCO)
        tela.blit(texto_sair, ((TELA_LARGURA - texto_sair.get_width() - TELA_ALTURA//2)//2, (TELA_ALTURA - 30) - texto_sair.get_height()//2))

        # Verifica se o jogo terminou: se sim, retorna o vencedor
        if controlador.vencedor is not None:
            tela_fim(tela, controlador.vencedor)
            return
        
        # Se estiver no modo "tempo"
        if modo == 'tempo':
            # Calcula segundos restantes
            agora = pygame.time.get_ticks() // 1000
            segundos_passados = (agora - inicio) - tempo_pausado
            segundos_restantes = tempo_restante - segundos_passados

            if segundos_restantes < 0:
                segundos_restantes = 0
            
            # Define a cor do tempo: quando atingir 1min, ele fica rosa
            cor_tempo = AZUL_ESCURO
            if segundos_restantes <= 60:
                cor_tempo = ROSA

            # Desenha temporizador na tela
            timer(tela, cor_tempo, segundos_restantes)

            # Se acabar o tempo, fim de jogo (nenhum vencedor)
            if segundos_restantes == 0:
                tela_fim(tela, 'nenhum')
                return

        # Voltar ao menu ou sair
        for evento in pygame.event.get():
            # Gerenciamento do tabuleiro
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicao = pygame.mouse.get_pos()
                resultado = obtem_clique(posicao, (LARGURA_TABULEIRO, ALTURA_TABULEIRO), offset=(101, 100))
                if resultado is not None:
                    linha, coluna = resultado
                    controlador.gerencia_clique(linha, coluna)

            # Se o usuário quiser sair, mostra a tela de pop-up
            if evento.type == pygame.QUIT:
                print_pop_up = tela.copy() # Salva o frame atual do jogo
                if modo =='tempo':
                    tempo_inicio_pausa = pygame.time.get_ticks() // 1000
                    escolha = pop_up(tela, print_pop_up, rosas_restantes, brancas_restantes)
                    tempo_fim_pausa = pygame.time.get_ticks() // 1000
                    tempo_pausado += (tempo_fim_pausa - tempo_inicio_pausa)
                else:
                    escolha = pop_up(tela, print_pop_up, rosas_restantes, brancas_restantes)

                if escolha == "sair":
                    fechar_tela = True  # sai do jogo
                # se for "continuar", não faz nada e volta ao loop normal

            # Gerenciamento do pause
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                print_pausa = tela.copy() # Salva o frame atual do jogo
                if modo == 'tempo':
                    tempo_inicio_pausa = pygame.time.get_ticks() // 1000
                    pausa = tela_pause(tela, print_pausa, rosas_restantes, brancas_restantes) # Pausa o jogo
                    tempo_fim_pausa = pygame.time.get_ticks() // 1000
                    tempo_pausado += (tempo_fim_pausa - tempo_inicio_pausa)
                else:
                    pausa = tela_pause(tela, print_pausa, rosas_restantes, brancas_restantes) # Pausa o jogo
                if not pausa:
                    return
                
        controlador.atualiza_jogo()
        pygame.display.update()

def tela_pause(tela, frame, rosas_restantes, brancas_restantes):
    """ ### Tira um print da tela e mostra que o jogo foi pausado. """
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        tela.blit(frame, (0, 0)) # Tela de fundo(jogo)
        
        # Sobreposição
        sobreposicao = pygame.Surface((TELA_LARGURA, TELA_ALTURA), pygame.SRCALPHA)
        sobreposicao.fill((0, 0, 0, 200))
        tela.blit(sobreposicao, (0 , 0))
        
        # Texto "JOGO PAUSADO"
        texto_pausado = PRINCIPAL.render('JOGO PAUSADO', True, ROSA)     
        tela.blit(texto_pausado, (TELA_LARGURA//2 - texto_pausado.get_width()//2, TELA_ALTURA//2 - texto_pausado.get_height()//2))

        # Texto voltar ao jogo
        texto_sair = LETRA_PEQUENA.render('CLIQUE NA TECLA "P" PARA VOLTAR AO JOGO.', True, BRANCO)
        tela.blit(texto_sair, (TELA_LARGURA//2 - texto_sair.get_width()//2, (TELA_ALTURA - 250) - texto_sair.get_height()//2))

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                return True
            if evento.type == pygame.QUIT:
                escolha = pop_up(tela, rosas_restantes, brancas_restantes)
                if escolha == "sair":
                    return False 
        pygame.display.update()

def tela_regras(tela):
    """ ###Mostra a tela de regras do jogo. """
    while True:
        # Voltar ao menu ou sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                return True

        tela.blit(BG_TELA_REGRAS, (0, 0))
        pygame.display.update()

def tela_inicial(tela, tabuleiro):
    """ ### Mostra a tela inicial do jogo. """
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
        botao_regras = Botao(BOTAO_REGRAS, (posicao_x, 392)) # 300 + 62 + 30
        botao_sair = Botao(BOTAO_SAIR, (posicao_x, 484)) # 300 + 62 + 62 + 60

        for botao in [botao_jogar, botao_regras, botao_sair]:
            botao.atualizar(tela)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Tela de jogo
                if botao_jogar.verifica_posicao(posicao_mouse_menu):
                    modo, tempo = tela_modo_jogo(tela)
                    if modo == 'normal':
                        tela_jogo(tela, tabuleiro, modo)
                    elif modo == 'tempo':
                        tela_jogo(tela, tabuleiro, modo, tempo)
                # Tela de Regras
                elif botao_regras.verifica_posicao(posicao_mouse_menu):
                    if not tela_regras(tela):
                        return False
                # Sair 
                elif botao_sair.verifica_posicao(posicao_mouse_menu):
                    rodando = False
        pygame.display.update()