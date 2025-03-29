import pygame as pg
from player import Player

pg.init()
display = pg.display

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 750
screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

bg = pg.transform.scale(pg.image.load("bg.png"), (960,750))
mayo = Player("assets/mayo.png",screen)
inventory = pg.image.load("assets/inventory.png")
fp = pg.image.load("assets/fp.png")


running = True
fpb = False

while running == True:
   screen.blit(bg, (0,0))
   mayo.draw()
   x,y = pg.mouse.get_pos()
   screen.blit(inventory,(0,640))

   for event in pg.event.get():
      fpb = False

      #make click for error handling
      if pg.mouse.get_pressed()[0] == True:
         print(x,y)
      
      if event.type == pg.KEYDOWN:
         mayo.move(event)
      if mayo.x in range(0,180) and mayo.y >= 245 and mayo.frametxt == 'frame_back':
        fpb = True
         
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
   
   if fpb == True:
      screen.blit(fp, (0,150))

   display.update()