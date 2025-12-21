import pygame
import random
import math
pygame.init()
window = pygame.display.set_mode((600,500))
pygame.display.set_caption("Einstein colliding particle")
BLACK = (0,0,0)
PURPLE = (128,0,128)
WHITE = (255,255,255)
RED = (255,0,0)
colliding = True

class particle:
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.velocityx =random.randint(4,8)
        self.velocityy =random.randint(3,7)
        self.mass = random.randint(1,6)
        self.vector = (0,0)
        self.size = math.sqrt(self.mass)*20
        self.color = random.choice(colors)
    def draw(self):
        pygame.draw.circle(window,self.color,(self.posx,self.posy),self.size)
    def motion(self):
        self.posx +=self.velocityx
        self.posy +=self.velocityy
    def wall_collision(self):
        #right wall
        if self.posx+self.size >550:
            self.velocityx = -self.velocityx
        #left wall
        if self.posx-self.size < 50:
            self.velocityx = -self.velocityx
        #bottom wall
        if self.posy + self.size > 450:
            self.velocityy = -self.velocityy
        #top
        if self.posy - self.size < 50:
            self.velocityy = -self.velocityy

    def neighbor_collision(self, other, restitution=1.0):
        # Distance between particles
        dx = self.posx - other.posx
        dy = self.posy - other.posy
        d = math.sqrt(dx**2 + dy**2)

        # Check collision
        if d < (self.size + other.size):
            # Normal vector
            nx = dx / d
            ny = dy / d

            # Relative velocity
            rvx = self.velocityx - other.velocityx
            rvy = self.velocityy - other.velocityy

            # Relative velocity along normal
            v_rel_n = rvx * nx + rvy * ny

            # Only resolve if particles are moving toward each other
            if v_rel_n < 0:
                # Impulse scalar
                j = -(1 + restitution) * v_rel_n / (1/self.mass + 1/other.mass)

                # Apply impulse
                self.velocityx += (j / self.mass) * nx
                self.velocityy += (j / self.mass) * ny

                other.velocityx -= (j / other.mass) * nx
                other.velocityy -= (j / other.mass) * ny



balls =[x for x in range(3)]
colors = [RED,PURPLE,BLACK]
for x in range(len(balls)):
    balls[x] = particle(random.randint(100,500),random.randint(100,400))

while colliding:
    window.fill((0,0,0))
    pygame.draw.rect(window,(255,255,255),(50,50,500,400))
    for x in balls:
        x.draw()
        x.motion()
        x.wall_collision()
    f=1
    for x in balls:
        if f<len(balls):
            for y in range(f,len(balls)):
                x.neighbor_collision(balls[y])
            f+=1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            colliding = False

    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()