import pygame
import time
pygame.init()

WIDTH=600
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))

caption=pygame.display.set_caption("Happy Birthday")

img1=pygame.image.load("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\Birthday\\happy-birthday-writing.jpg")
image1=pygame.transform.scale(img1,(WIDTH,HEIGHT))

running=True
while running:
    font=pygame.font.SysFont("Comic sansms",30)
    text=font.render("!HAVE A GREAT DAY :D!",True,(255,0,0))
    screen.fill("red")
    screen.blit(image1,(0,0))
    screen.blit(text,(20,20))
    pygame.display.update()
    time.sleep(4)

pygame.quit()