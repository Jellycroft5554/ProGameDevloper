import pgzrun
from random import randint
TITLE = 'Flappy Ball'
WIDTH = 1200
HEIGHT = 800
R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B
#BLUE = 0, 128, 255
GRAVITY = 2000.0  # pixels per second per second

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50,100)

ball2= Ball(70,150)

def draw():
    screen.clear()
    ball.draw()
    ball2.draw()

def update(self,dt):
    # Apply constant acceleration formulae
    uy = self.vy
    self.vy += GRAVITY * dt
    self.y += (uy + self.vy) * 0.5 * dt

    # Detect and handle the bounce
    if self.y > HEIGHT - self.radius:
        self.y = HEIGHT - self.radius
        self.vy = -self.vy * 0.9
    
    self.x += self.vx * dt
    if self.x > WIDTH-self.radius or self.x < self.radius:
        self.vx = -self.vx

def kick(self,click):
    self.vy = click

def update(dt):
    ball.update(dt)
    ball2.update(dt)

def on_key_down(key):
    if key==keys.SPACE:
        ball.kick(-500)
        ball2.kick(-300)

 
pgzrun.go()