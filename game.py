import pygame as pg
import random

WIDTH = 750
HEIGHT = 500
FPS = 30


WHITE = (255, 255, 255)
BLACK = (225, 225, 225)
RED = (225, 225, 225)
GREEN = (225, 225, 225)
BLUE = (225, 225, 255)


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()


running = True
while running:
    
    clock.tick(FPS)
    
    for event in pg.event.get():
       
        if event.type == pg.QUIT:
            running = False

    
    
    
    screen.fill(WHITE)
    
    pg.display.flip()

def __init__(self, color, x, y):
    self.color = color
    self.x = x
    self.y = y
    
   def draw(self, screen):
       pg.draw.line
                   