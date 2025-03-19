import pygame
pygame.init()

screen.pygame.display.set_mode([600,600])

R=255,0,0
G=0,255,0
B=0,0,255
W=255,255,255
B=0,0,0

screen.fill(W)

class Circle():

    def __init__(self,radius,color,pos,screen,wid=0):
        self.radius=radius
        self.color=color
        self.position=pos
        self.screen=screen
        self.wid=wid

    def draw(self):
        pygame.draw.circle(self.screen,self.radius,self.color,self.position,self.wid)

    def grow(self,x):
        self.radius += x
        pygame.draw.circle(self.screen,self.radius,self.color,self.position,self.wid)

position=(300,300)
radius=(50)

pygame.draw.circle(screen,radius,R,position)

circle1=Circle(R,position,radius+40,7)

pygame.display.update()
pygame.quit