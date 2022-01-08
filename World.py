import pygame as pg
import numpy as np

class World():
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode(size = (500,500))
        #backGround = pg.image.load('C:/Users/spike/Pictures/Untitled_Artwork.jpg')
        #win.blit(backGround, (0,0))
        self.wallsPos = [(0,0,500,10),(0,10,10,270),(490,10,10,270),(450,270,40,10),(30,270,340,10),(360,280,10,100),(450,280,10,100),(370,370,80,10),
                    (10,30,250,10),(280,30,100,10),(400,30,40,10),(310,70,60,10),(10,80,60,10),(130,80,50,10),(210,80,20,10),
                    (260,100,20,10),(310,100,40,10),(10,120,70,10),(140,130,230,10),(100,160,190,10),(370,180,50,10),
                    (10,200,200,10),(280,200,60,10),(190,210,70,10),(280,230,40,10),(370,230,80,10),
                    (100,40,10,70),(230,40,10,70),(280,40,10,90),(460,30,10,80),(50,60,10,20),(180,60,10,70),(310,80,10,20),(370,70,10,70),(410,70,10,110),(450,100,10,30),
                    (70,130,10,50),(100,130,10,30),(340,140,10,130),(30,150,10,50),(450,150,10,90),(130,170,10,30),(230,170,10,20),(370,190,10,40),(60,210,30,40),
                    (160,210,10,40),(250,210,10,30),(280,210,10,20),(400,210,10,100),(30,230,10,40),(110,230,30,40),(190,240,10,30),(220,250,10,20)]
        # exterior walls then by row then by column
        self.draw()
   
    def draw(self):
        self.back = pg.draw.rect(self.win,(10,10,10),(0,0,500,500))
        self.walls = [pg.draw.rect(self.win,(200,10,10),wall) for wall in self.wallsPos]
        self.goal = pg.draw.rect(self.win,(10,200,10),(10,270,20,10))

    def update(self):
        pg.display.update()
        pg.event.pump()

        
