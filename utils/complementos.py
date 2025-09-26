from utils.config import *
import datetime
    
def obtem_clique(posicao, limites_tabuleiro, offset=(0, 0)):
    """Retorna a posição do clique no tabuleiro.
    Caso for fora do seu perímetro, retorna None."""
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

def formatar_tempo(segundos_restantes):
    """Formata o tempo restante de segundos para o formato H:MM:SS."""
    tempo = datetime.timedelta(seconds=segundos_restantes)
    return str(tempo)

def tocar_musica(modo, som_ligado):
    """Toca a música de acordo com o modo de jogo."""
    if not som_ligado:
        return
    if modo == 'tempo':
        MUSICA_TEMPO.play(-1)
    else:
        MUSICA_NORMAL.play(-1)

def parar_musica(modo):
    """Para a música correspondente modo de jogo."""
    if modo == 'tempo':
        MUSICA_TEMPO.stop()
    else:
        MUSICA_NORMAL.stop()
        