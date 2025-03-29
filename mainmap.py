import pygame as pg
from player import Player

pg.init()
display = pg.display

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 750
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

bg = pg.transform.scale(pg.image.load("bg.png"), (960,750))

mayo = Player("assets/mayo.png",screen)


running = True

while running == True:
  screen.blit(bg, (0,0))
  mayo.draw()
  x,y = pg.mouse.get_pos()
  for event in pg.event.get():

    if event.type == pg.KEYDOWN:
      mayo.move(event)

    #make click
    if pg.mouse.get_pressed()[0] == True:
       print(x,y)

    if event.type == pg.QUIT:  # for quitting
        running = False
    
  display.update()