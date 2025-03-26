import pygame
pygame.init()

screen=pygame.display.set_mode([900,900])

R=255,0,0
G=0,255,0
B=0,0,255
P=120,0,120
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

position=(450,450)
radius=50
wid=0

pygame.draw.circle(screen,R,position,radius+200,wid)
pygame.display.update()

circle1=Circle(screen,R,position,radius+30,2)
circle2=Circle(screen,B,position,radius+40,20)
circle3=Circle(screen,G,position,radius+20,0)
circle4=Circle(screen,BL,position,radius+30,0)
circle5=Circle(screen,R,position,radius+100,3)
circle6=Circle(screen,P,position,radius,10)

running=True 
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False     
        if (event.type==pygame.MOUSEBUTTONDOWN):
            circle1.draw()
            circle2.draw()
            circle3.draw()
            circle4.draw()
            circle5.draw()
            circle6.draw()
            pygame.display.update()
        elif (event.type==pygame.MOUSEBUTTONUP):
            circle1.grow(10)
            circle2.grow(30)
            circle3.grow(20)
            circle4.grow(30)
            circle5.grow(-10)
            circle6.grow(10)
            pygame.display.update()

pygame.quit()
