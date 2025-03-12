import pygame as py
from config import screen, WIDTH, HEIGHT, imagem_fundo

class Personagem(py.sprite.Sprite):
    def __init__(self, nome, nome_imagem, posicao_x, posicao_y, imagens):
        super().__init__()
        self.nome = nome
        self.nome_imagem = nome_imagem
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.state = 'idle'
        self.x_speed = 0
        self.y_speed = 0
        self.current_image = 1
        self.last_img_change = 0
        self.no_chao = True
        self.hit_duracao = 10
        self.hit_tempo = 0
        self.vida = 100
        self.imagens = imagens

    def desenhar(self):
        personagem_img = self.imagens[self.state][self.current_image]
        screen.blit(personagem_img, (self.posicao_x, self.posicao_y))

    def update(self):
        if self.vida <= 0:
            self.state = 'death'
            return
        self.last_img_change += 1
        if self.state == 'hit':
            self.hit_tempo += 1
            if self.hit_tempo >= self.hit_duracao:
                self.state = 'idle'
                self.hit_tempo = 0
            return
        if self.state == 'beating' and self.last_img_change > 1:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(self.imagens[self.state])
            if self.current_image == 0:
                self.state = 'idle'
        elif self.last_img_change > 5:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(self.imagens[self.state])

        # Movimentação horizontal
        self.posicao_x += self.x_speed
        margin = 300 if self.nome == 'Demon' else 255
        if self.posicao_x < -margin:
            self.posicao_x = -margin
        elif self.posicao_x + 864 > WIDTH + margin:
            self.posicao_x = WIDTH - 864 + margin