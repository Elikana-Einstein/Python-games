import pygame
import math
import secrets
import string
pygame.init()
WIDTH = 600
HEIGHT = 500
RED = (255,0,0)
PURPLE = (128,0,128)
BLACK = (0,0,0)
window = pygame.display.set_mode((800,500))
pygame.display.set_caption("Fourier series")

series =True
radius =70
time = 0
wave = []
circles = {}
circls = []
class point:
    def __init__(self,x,y):
        self.x =x
        self.y =y
        self.time = 0
    def draw(self):
        self.x+=1
        pygame.draw.circle(window,RED,(self.x,self.y),1)
        
class circle:
    def __init__(self,x,y,r,n):
        self.x = x
        self.y = y
        self.r = r
        self.n = n
        self.radius = (self.r * 1/self.n)

    def draw(self):
        pygame.draw.circle(window,(0,0,0),(self.x,self.y),self.radius,1)
    def dot(self,n=1):
        x1 = (self.radius * math.sin(n *time)) +self.x
        y1 = (self.radius * math.cos(n *time)) +self.y
        pygame.draw.circle(window,RED,(x1,y1),3)
        circles[n] = (x1,y1)
        
    def line(self,x,y):
        pygame.draw.line(window,RED,(self.x,self.y),(x,y))


n_m =1
while series:
    
    window.fill((255,255,255))

    x = (radius * math.sin(time)) + 100
    y = (radius * math.cos(time)) + 250
    
    k = circle(200,250,radius,n_m)
    k.draw()
    res1 = k.dot()
    k.line(circles[1][0],circles[1][1])

    h = circle(circles[1][0],circles[1][1],radius,n_m+2)
    h.draw()
    h.dot(3)
    h.line(circles[3][0],circles[3][1])

    t = circle(circles[3][0],circles[3][1],radius,n_m+4)
    t.draw()
    t.dot(5)

    k = circle(circles[5][0],circles[5][1],radius,n_m+6)
    k.draw()
    k.dot(7)

    j = circle(circles[7][0],circles[7][1],radius,n_m+8)
    j.draw()
    j.dot(n_m+8)
    random_string = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(3))
    random_string = point(500,circles[9][1])

    wave.append(random_string)
    for l in wave:
        l.draw()


    pygame.draw.line(window,PURPLE,(circles[9][0],circles[9][1]),(wave[-1].x,wave[-1].y))
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            series = False
    time-=0.06
    pygame.time.Clock().tick(30)
    pygame.display.flip()
pygame.quit()