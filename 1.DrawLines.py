import pygame

#initialise pygame
pygame.init()

#set up display
screen=pygame.display.set_mode((600,600))
title=pygame.display.set_caption("Rectangles!")

#define colours
L_Blue=(100,149,237)
Red=(255,0,0)
Purple=(128,0,128)
Orange=(255,99,71)
D_Green=(15,128,38)
D_Blue=(18,29,179)
Black=(0,0,0)

#Fill screen with L_Blue
screen.fill(L_Blue)

#create line class
class Line:
    def __init__(self,color,dimensions):
        self.surface=screen
        self.color=color
        self.dimensions=dimensions
    
    #draw function
    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.dimensions)

RedRect=Line(Red,(0,100,600,1))
PurpleRect=Line(Purple,(0,300,600,1))
OrangeRect=Line(Orange,(0,500,600,1))

GreenRect=Line(D_Green,(500,0,1,600))
D_BlueRect=Line(D_Blue,(300,0,1,600))
D_BlackRect=Line(Black,(100,0,1,600))

#Draw horisontal lines
RedRect.draw()
PurpleRect.draw()
OrangeRect.draw()

#Draw verticle lines
GreenRect.draw()
D_BlueRect.draw()
D_BlackRect.draw()

#update the display
pygame.display.update()

#Game roof to keep the window open
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

pygame.quit()