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

   #make click for error handling
   if pg.mouse.get_pressed()[0] == True:
      print(x,y)
      print(mayo.x, mayo.y)

   if event.type == pg.KEYDOWN:
      mayo.move(event)
   if mayo.x in range(0,180) and mayo.y >= 245 and mayo.frametxt == 'frame_back':
      pass
      #PUT FRIDGE/PANTRY STUFF HERE!
   if mayo.x in range(320,360) and mayo.y >= 245 and mayo.frametxt == 'frame_back':
      pass
      #PUT COUNTER STUFF (CHOPPING, ETC.) HERE!
   if mayo.x in range(448,515) and mayo.y >= 245 and mayo.frametxt == 'frame_back':
      pass
      #PUT SINK STUFF HERE!
   if mayo.x in range(608,740) and mayo.y >= 245 and mayo.frametxt == 'frame_back':
      pass
      #PUT STOVE/OVEN STUFF HERE!

   if event.type == pg.QUIT:  # for quitting
      running = False
    
  display.update()