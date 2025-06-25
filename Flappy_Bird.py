import pygame
from pygame.locals import *
pygame.init()
import random

clock = pygame.time.Clock()
fps = 60

WIDTH = 1100
HEIGHT = 800
Screen = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont("Comic Sans ms",30)

red = (255,0,0)

ground_scroll = 0
scroll_speed = 4

flying = False
game_over = False

pipe_gap = 200
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks()-pipe_frequency

score = 0
passed_pipe = False

def draw_text(text,font,text_clr,x,y):
    img = font.render(text,True,text_clr)
    screen.blit(img,(x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(HEIGHT/2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for num in range(1,7):
            img=pygame.image.load(f"fing/b{num}.png")
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vs=0
        self.clicked=False
    def update(self):
        if flying == True:
            self.vs += 0.5
            if self.vs > 8:
                self.vs == 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vs)
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked == True 
                self.vs= -10
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False
    
            Flap_cool_down = 5
            self.counter += 20
            if self.counter > Flap_cool_down:
                self.counter = 0
                self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.image = self.image[self.images]
            
        self.image =  pygame.transform.rotate(self.image[self.index])(self.velosity)
        self.image = pygame.transform.rotate(self.idex[self.image]),[-90]

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
