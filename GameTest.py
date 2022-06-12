import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
import pygame as pg
from pygame.locals import *
from sys import exit

# variaveis
largura, altura = 640, 480
x, y = 300, 215

pg.init()
pg.display.set_caption('jogo')

tela = pg.display.set_mode((largura, altura))
relogio = pg.time.Clock()

while True:
    tela.fill((0, 0, 0))
    relogio.tick(30)

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

    if pg.key.get_pressed()[K_a]:
        if x > 0:
            x -= 20
    if pg.key.get_pressed()[K_d]:
        if x < (largura - 40):
            x += 20
    if pg.key.get_pressed()[K_w]:
        if y > 0:
            y -= 20
    if pg.key.get_pressed()[K_s]:
        if y < (altura - 50):
            y += 20

    pg.draw.rect(tela, (0, 160, 0), (x, y, 40, 50))
    pg.display.update()