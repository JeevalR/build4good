import pygame as pg

SCREEN_WIDTH = 30 * 32
SCREEN_HEIGHT = 25 * 32
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

bg = pg.image.load("bg.png")

run = True

while (run):
    screen.blit(bg, (0,0))