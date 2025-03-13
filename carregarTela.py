import pygame as py

class carregarTela:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def exibir_tela(self, imagem_path, texto=None, botao_texto=None):
        imagem = py.image.load(imagem_path)
        imagem = py.transform.scale(imagem, (self.width, self.height))
        self.screen.blit(imagem, (0, 0))

        if texto:
            fonte = py.font.Font(None, 74)
            texto_render = fonte.render(texto, True, (255, 255, 255))
            self.screen.blit(texto_render, (self.width // 2 - texto_render.get_width() // 2, self.height // 2 - 150))

        if botao_texto:
            fonte_botao = py.font.Font(None, 50)
            botao_largura, botao_altura = 300, 80
            botao_x = self.width // 2 - botao_largura // 2
            botao_y = self.height // 2 + 100

            py.draw.rect(self.screen, (0, 128, 0), (botao_x, botao_y, botao_largura, botao_altura))
            texto_botao = fonte_botao.render(botao_texto, True, (255, 255, 255))
            self.screen.blit(texto_botao, (botao_x + botao_largura // 2 - texto_botao.get_width() // 2, botao_y + botao_altura // 2 - texto_botao.get_height() // 2))

            py.display.update()
            
            esperando = True
            while esperando:
                for event in py.event.get():
                    if event.type == py.QUIT:
                        py.quit()
                        quit()
                    if event.type == py.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = py.mouse.get_pos()
                        if botao_x <= mouse_x <= botao_x + botao_largura and botao_y <= mouse_y <= botao_y + botao_altura:
                            esperando = False

    def tela_inicio(self):
        self.exibir_tela("assets/INICIO.jpg", "Batalha das Feras", "Iniciar Jogo")

    def tela_fim(self):
        self.exibir_tela("Tela fim.webp")
        py.quit()