class Botao:
    """Classe com atributos dos botões do menu."""
    def __init__(self, imagem, posicao):
        self.imagem = imagem
        self.x = posicao[0]
        self.y = posicao[1]
        self.retangulo = self.imagem.get_rect(center=(self.x, self.y))

    def atualizar(self, tela):
        tela.blit(self.imagem, self.retangulo)

    # verifica se o botão foi pressionado
    def verifica_posicao(self, posicao):
        if posicao[0] in range(self.retangulo.left, self.retangulo.right) and posicao[1] in range(self.retangulo.top, self.retangulo.bottom):
            return True
        return False