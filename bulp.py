import pygame
import time
pygame.init()

WIDTH=800
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH,HEIGHT))

img1=pygame.image.load("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\bulb\\off.png")
#img2=pygame.image.load("C:\\Users\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\bulb\\on.png")
image1=pygame.transform.scale(img1,(WIDTH,HEIGHT))
#image2=pygame.transform.scale(img2,(WIDTH,HEIGHT))

pygame.display.update()

running=True
while running:
    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        img2=pygame.image.load("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\bulb\\on.png")
        image2=pygame.transform.scale(img2,(WIDTH,HEIGHT))
        screen.blit(image2,(0,0))
        pygame.display.update()

    elif event.type==pygame.MOUSEBUTTONUP:
        img1=pygame.image.load("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\bulb\\off.png")
        image1=pygame.transform.scale(img1,(WIDTH,HEIGHT))
        screen.blit(image1,(0,0))
        pygame.display.update()

pygame.quit()