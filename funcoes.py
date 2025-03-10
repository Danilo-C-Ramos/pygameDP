import pygame as py
from config import screen, WIDTH, HEIGHT
# Função para a Tela de Início
def tela_inicio(screen, WIDTH, HEIGHT):
    imagem_fundo_inicio = py.image.load("assets/INICIO.jpg")
    imagem_fundo_inicio = py.transform.scale(imagem_fundo_inicio, (WIDTH, HEIGHT))
    botao_largura = 300
    botao_altura = 80
    botao_x = WIDTH // 2 - botao_largura // 2
    botao_y = HEIGHT // 2 + 100
    fonte = py.font.Font(None, 74)
    fonte_botao = py.font.Font(None, 50)

    esperando = True
    while esperando:
        screen.blit(imagem_fundo_inicio, (0, 0))  # Carregar e desenhar a imagem de fundo
        texto = fonte.render("Batalha das Feras", True, (255, 255, 255))
        screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - 150))

        py.draw.rect(screen, (0, 128, 0), (botao_x, botao_y, botao_largura, botao_altura))
        texto_botao = fonte_botao.render("Iniciar Jogo", True, (255, 255, 255))
        screen.blit(texto_botao, (botao_x + botao_largura // 2 - texto_botao.get_width() // 2, botao_y + botao_altura // 2 - texto_botao.get_height() // 2))
        py.display.update()

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                if botao_x <= mouse_x <= botao_x + botao_largura and botao_y <= mouse_y <= botao_y + botao_altura:
                    esperando = False

# Função para a Tela de Fim
def tela_fim(screen, WIDTH, HEIGHT):
    imagem_fundo_fim = py.image.load("Tela fim.webp")
    imagem_fundo_fim = py.transform.scale(imagem_fundo_fim, (WIDTH, HEIGHT))  # Garantir que seja uma superfície válida
    
    screen.blit(imagem_fundo_fim, (0, 0))
    py.display.update()

    esperando = True
    while esperando:
        for event in py.event.get():
            if event.type == py.QUIT or event.type == py.MOUSEBUTTONDOWN:
                esperando = False
    py.quit()

# Função de animação para o demon
def carregar_imagens_demonio():
    demon_images = {}
    img_list = []
    for i in range(1, 7):
        img_list.append(py.transform.scale(py.image.load(f"assets/Demo idle/01_demon_idle/demon_idle_{i}.png").convert_alpha(), (864, 480)))
    demon_images['idle'] = img_list
    img_list = []
    for i in range(1, 13):
        img_list.append(py.transform.scale(py.image.load(f"assets/Demo andando/02_demon_walk/demon_walk_{i}.png").convert_alpha(), (864, 480)))
    demon_images['walking'] = img_list
    img_list = []
    for i in range(1, 16):
        img_list.append(py.transform.scale(py.image.load(f"assets/Demo batendo/03_demon_cleave/demon_cleave_{i}.png").convert_alpha(), (864, 480)))
    demon_images['beating'] = img_list
    img_list = []
    for i in range(1, 23):
        img_list.append(py.transform.scale(py.image.load(f"assets/Demo morte/05_demon_death/demon_death_{i}.png").convert_alpha(), (864, 480)))
    demon_images['death'] = img_list
    img_list = []
    for i in range(1, 6):
        img_list.append(py.transform.scale(py.image.load(f"assets/Demo tomando/04_demon_take_hit/demon_take_hit_{i}.png").convert_alpha(), (864, 480)))
    demon_images['hit'] = img_list
    return demon_images

# Função de animação para o monstro
def carregar_imagens_monstro():
    mon_images = {}
    img_list = []
    for i in range(1, 16):
        img_list.append(py.transform.scale(py.image.load(f"assets/Mon idle/idle/idle_{i}.png").convert_alpha(), (768, 448)))
    mon_images['idle'] = img_list
    img_list = []
    for i in range(1, 13):
        img_list.append(py.transform.scale(py.image.load(f"assets/Mon andando/walk/walk_{i}.png").convert_alpha(), (768, 448)))
    mon_images['walking'] = img_list
    img_list = []
    for i in range(1, 8):
        img_list.append(py.transform.scale(py.image.load(f"assets/Mon batendo1/1atk/1atk_{i}.png").convert_alpha(), (768, 448)))
    mon_images['beating'] = img_list
    img_list = []
    for i in range(1, 12):
        img_list.append(py.transform.scale(py.image.load(f"assets/Mon morte/death/death_{i}.png").convert_alpha(), (768, 448)))
    mon_images['death'] = img_list
    img_list = []
    for i in range(1, 6):
        img_list.append(py.transform.scale(py.image.load(f"assets/Mon tomando/hurt/hurt_{i}.png").convert_alpha(), (768, 448)))
    mon_images['hit'] = img_list
    return mon_images



def andar(demon, mon, event):
    if event.type == py.KEYDOWN:
            if demon.vida > 0:
                if event.key == py.K_LEFT:
                    demon.state = 'walking'
                    demon.x_speed = -10
                    demon.current_image = 0
                if event.key == py.K_RIGHT:
                    demon.state = 'walking'
                    demon.x_speed = 10
                    demon.current_image = 0
                if event.key == py.K_SPACE:
                    demon.state = 'beating'
                    demon.current_image = 0
            
            if mon.vida > 0:
                if event.key == py.K_d:
                    mon.state = 'walking'
                    mon.x_speed = 10
                    mon.current_image = 0
                if event.key == py.K_a:
                    mon.state = 'walking'
                    mon.x_speed = -10
                    mon.current_image = 0
                if event.key == py.K_r:
                    mon.state = 'beating'
                    mon.current_image = 0

            if event.type == py.KEYUP:
                if event.key in [py.K_LEFT, py.K_RIGHT]:
                    demon.state = 'idle'
                    demon.x_speed = 0
                    demon.current_image = 0
                if event.key in [py.K_d, py.K_a]:
                    mon.state = 'idle'
                    mon.x_speed = 0
                    mon.current_image = 0


# Função de colisão para dano
def verificar_colisao(demon, mon):
    if demon.vida > 0 and mon.vida > 0:
        if abs(demon.posicao_x - mon.posicao_x) < 300:
            if demon.state == 'beating' and mon.state != 'hit':
                mon.state = 'hit'
                mon.current_image = 0
                mon.hit_tempo = 0
                mon.vida -= 6
            elif mon.state == 'beating' and demon.state != 'hit':
                demon.state = 'hit'
                demon.current_image = 0
                demon.hit_tempo = 0
                demon.vida -= 9

# Função para desenhar a tela e as barras de vida
def limpa_screen(demon, mon):
    screen.blit(imagem_fundo, (0, 0))

    # Desenhando as barras de vida
    mon_health_ratio = mon.vida / 100
    py.draw.rect(screen, (255, 0, 0), (50, 50, 500, 25))  # Barra de vida vermelha (fundo)
    py.draw.rect(screen, (0, 255, 0), (50, 50, 500 * mon_health_ratio, 25))  # Barra de vida verde

    demon_health_ratio = demon.vida / 100
    py.draw.rect(screen, (255, 0, 0), (WIDTH - 550, 50, 500, 25))  # Barra de vida vermelha (fundo)
    py.draw.rect(screen, (0, 255, 0), (WIDTH - 550, 50, 500 * demon_health_ratio, 25))  # Barra de vida verde

    # Desenha os personagens
    if demon.vida > 0:
        demon.desenhar()
    if mon.vida > 0:
        mon.desenhar()

