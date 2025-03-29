import pygame as pg

def get_image(img,frame, width, height,color=(50,50,50)):
        image = pg.Surface((width, height)).convert_alpha()
        image.fill(color) 
        image.blit(img, (0,0), ((frame * width),0, width, height))
        #image = pg.transform.scale(img,(width *scale, height * scale))
        image.set_colorkey(color)
        return image

class Player():
    def __init__(self, image,screen):
        img = pg.transform.scale(pg.image.load(image).convert_alpha(), (768,192))
        frame_back = get_image(img, 0, 192, 192)
        frame_front = get_image(img, 1, 192, 192)
        frame_right = get_image(img, 2, 192, 192)
        frame_left = get_image(img, 3, 192, 192)
        self.frames = {"frame_front" : frame_front,"frame_back" : frame_back,"frame_left" : frame_left,"frame_right" : frame_right}
        self.frametxt = "frame_front"
        self.x = 480
        self.y = 375
        self.screen = screen
        self.velocity = 32
    def can_move(self):
        if self.y < 250:
            self.y = 251
            return False
        if self.y > 556:
            self.y = 555
            return False
        if self.x < 0:
            self.x = 0
            return False
        if self.x > 790:
            self.x = 789
            return False
        return True
    
    def draw(self):
         self.screen.blit(self.frames[self.frametxt],(self.x,self.y))

    def move(self,event):
        #left
        if event.key == pg.K_LEFT:
            if self.can_move():
                self.x -= self.velocity 
            self.frame = self.frames["frame_left"]
            self.frametxt = "frame_left"


        #right
        if event.key == pg.K_RIGHT: 
            if self.can_move():
                self.x += self.velocity 
            self.frame = self.frames["frame_right"]
            self.frametxt = "frame_right"

        #up
        if event.key == pg.K_UP: 
            if self.can_move():
                self.y -= self.velocity 
            self.frame = self.frames["frame_back"]
            self.frametxt = "frame_back"

        #down
        if event.key == pg.K_DOWN: 
            if self.can_move():
                self.y += self.velocity 
            self.frame = self.frames["frame_front"]
            self.frametxt = "frame_front"
