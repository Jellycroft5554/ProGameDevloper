import pygame
import os

pygame.mixer.init()
pygame.font.init()

WIDTH,HEIGHT=1000,700

win=pygame.display.setmode((WIDTH,HEIGHT))
caption=pygame.display.set_caption("Space Invaders!")

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

bullet_hit_sound=pygame.mixer.Sound("C:\\Users\\ryani_jvpdg6k\\OneDrive\\Desktop\\Coding\\PRO GAME DEVLOPER\\1.DrawLines.py\\space invaders\\Grenade+1.mp3")
bullet_fire_sound=pygame.mixer.Sound("Gun+Silencer.mp3")

heath_font=pygame.font.SysFont("Comicsans",30)
winner_font=pygame.font.SysFont("Comicsans",100)

fps=60
vs=5
bvs=7
maxb=3
spaceship_w,spaceship_h=55,40

yellow_hit=pygame.USEREVENT+1
red_hit=pygame.USEREVENT+2

red_image=pygame.image.load(os.path.join("space invaders","rocket1.png"))
red_spaceship=pygame.transform.rotate(pygame.transform.scale(red_image,(spaceship_w,spaceship_h)),90)

yellow_image=pygame.image.load(os.path.join("space invaders","rocket2.png"))
yellow_spaceship=pygame.transform.rotate(pygame.transform.scale(yellow_image,(spaceship_w,spaceship_h)),270)

space=pygame.tranform.scale(pygame.image.load(os.path.join("space invaders","space.png")),(WIDTH,HEIGHT))

def draw_window(RED,YELLOW,RED_BULLETS,YELLOW_BULLETS,RED_HEALTH,YELLOW_HEALTH):
    win.blit(space,(0,0))
    pygame.draw.rect(win,WHITE,border)
    RED_HEALTH_TEXT=heath_font.render("Health"+str(RED_HEALTH),1,WHITE)
    YELLOW_HEALTH_TEXT=heath_font.render("Health"+str(YELLOW_HEALTH),1,WHITE)
    win.blit(RED_HEALTH_TEXT,(WIDTH-RED_HEALTH_TEXT.get_width()-10,10))
    win.blit(YELLOW_HEALTH_TEXT,(10,10))
    win.blit(red_spaceship,(red.x,red.y))
    win.blit(yellow_spaceship,(yellow.x,yellow.y))

    for bullet in RED_BULLETS:
        pygame.draw.rect(win,RED,bullet)

    for bullet in YELLOW_BULLETS:
        pygame.draw.rect(win,YELLOW,bullet)

pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and [yellow.x-vs>0]:
        yellow.x-=vs
    if keys_pressed[pygame.K_d] and [yellow.x+vs+yellow.width<border.x]:
        yellow.x+=vs
    if keys_pressed[pygame.K_w] and [yellow.y-vs>0]:
        yellow.y-=vs
    if keys_pressed[pygame.K_s] and [yellow.y+vs+yellow.height<height-10]:
        yellow.y+=vs

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_RIGHT] and [red.x+vs+red.width<border.x]:
        red.x-=vs
    if keys_pressed[pygame.K_LEFT] and [red.x-vs>border.x+border.width]:
        red.x+=vs
    if keys_pressed[pygame.K_UP] and [red.y-vs>0]:
        red.y-=vs
    if keys_pressed[pygame.K_DOWN] and [red.y+vs+red.height<HEIGHT-10]:
        red.y+=vs    
