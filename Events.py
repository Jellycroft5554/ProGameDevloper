import pygame
pygame.init()

screen=pygame.display.set_mode([600,600])

R=255,0,0
G=0,255,0
B=0,0,255
W=255,255,255
BL=0,0,0

screen.fill(W)

class Circle():

    def __init__(self,screen,color,pos,radius,wid=0):
        self.radius=radius
        self.color=color
        self.position=pos
        self.screen=screen
        self.wid=wid

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.radius,self.wid)

    def grow(self,x):
        self.radius += x
        pygame.draw.circle(self.screen,self.color,self.position,self.radius,self.wid)

position=(300,300)
radius=50
wid=0

pygame.draw.circle(screen,R,position,radius,wid)
pygame.display.update()

circle1=Circle(R,position,radius+40,2)
circle2=Circle(B,position,radius+70,7)
circle3=Circle(G,position,radius+20,0)

running=True 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif (event.type==pygame.MOUSEBUTTONDOWN):
            circle1.draw()
            circle2.draw()
            circle3.draw()
            pygame.display.update()
        elif (event.type==pygame.MOUSEBUTTONUP):
            circle1.grow(10)
            circle2.grow(30)
            circle3.grow(20)
            pygame.display.update()

pygame.quit()