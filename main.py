import pygame as py
from pygame import mixer
from funcoes import *
from config import screen, WIDTH, HEIGHT, FPS, clock
from personagem import *
from carregarTela import *

# Chamando a tela de início
telas = carregarTela(screen, WIDTH, HEIGHT)
telas.tela_inicio()

# Carregar as imagens dos personagens
demon_images = carregar_imagens_demonio()
mon_images = carregar_imagens_monstro()

# Criando os personagens
demon = Personagem('Demon', 'demon_idle_1', 620, 100, demon_images)
mon = Personagem('Monstro', 'idle_1', -250, 200, mon_images)

# Loop principal do jogo
game = True
while game:
    clock.tick(FPS)
    
    # Termina o jogo se um dos personagens estiver morto
    if demon.vida <= 0 or mon.vida <= 0:
        game = False

    for event in py.event.get():
        if event.type == py.QUIT:
            game = False

        andar(demon, mon, event)

    demon.update()
    mon.update()
    verificar_colisao(demon, mon)
    limpa_screen(demon, mon)

    py.display.update()

# Fechar o jogo
telas.tela_fim()
mixer.music.stop()
mixer.quit()
py.quit()