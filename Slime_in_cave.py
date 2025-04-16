import pygame
from pygame.locals import *
from time import *
pygame.init()

screen=pygame.display.set_mode((800,512))

player_x=400
player_y=256

keys=[False,False,False,False]

Player=pygame.image.load("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\Slime ball\\Slime ball.png")
Cave=pygame.image.load("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\Slime ball\\image.png")

while player_y<400:
    screen.blit(Cave,(0,0))
    screen.blit(Player,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit(exit(0))
        if event.type==pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            if event.key==K_s:
                keys[1]=True
            if event.key==K_a:
                keys[2]=True
            if event.key==K_d:
                keys[3]=True

        if event.type==pygame.KEYUP:
            if event.key==K_w:
                keys[0]=False
            if event.key==K_s:
                keys[1]=False
            if event.key==K_a:
                keys[2]=False
            if event.key==K_d:
                keys[3]=False

    if keys[0]:
        if player_y>0:
            player_y-=30
    if keys[1]:
        if player_y<512:
            player_y+=30
    if keys[2]:
        if player_x>0:
            player_x-=30
    if keys[3]:
        if player_x<800:
            player_x+=30            

    player_y+=2
    sleep(0.5)

print("Game Over")