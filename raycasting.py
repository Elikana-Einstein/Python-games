import pygame
import math
pygame.init()
RED = (255,0,0)
PURPLE = (128,0,128)

window = pygame.display.set_mode((600,500))
pygame.display.set_caption("Ray casting")
h=10
#boundary object
class Boundary:
    def __init__(self,start,end):
        self.start = start
        self.end  = end
    def draw(self):
        pygame.draw.line(window,(255,255,255),(self.start),(self.end))

#ray object
class Ray:
    def __init__(self,pos,angle):
        self.x1 = pos[0]
        self.y1 = pos[1]


        #convert degrees to radians
        radians = math.radians(angle)
       
       #calculate the new vector B
        self.x2 = self.x1 +70 * math.cos(radians)
        self.y2 = self.y1+70*math.sin(radians)

       
    def draw(self):
        pygame.draw.line(window,(255,255,255),(self.x1,self.y1),(self.x2,self.y2))
    
    def look_at(self,x,y):
        #calculate the original length of the line
        AB = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)

        #direction vector from A to C
        AC = (x - self.x1,y-self.y1)

        #normolize the direction vector
        k = pygame.Vector2(AC[0],AC[1])
        nAC = k.normalize()

        if nAC != 0 :
            vectorAB = (nAC[0]*AB,nAC[1]*AB)
        else:
            return

        #scale the unit vector by original length

        #calculate the new end poit B
        self.x2 = self.x1+ vectorAB[0]
        self.y2 = self.y1+ vectorAB[1]

    
    def cast(self,wall):
        x1 = self.x1  
        y1 = self.y1
        x2 = self.x1 + ((self.x2-self.x1)*3)
        y2 = self.y1 + ((self.y2 - self.y1)*3)

        x3 = wall.start[0]
        y3 = wall.start[1]
        x4 = wall.end[0]
        y4 = wall.end[1]

      
        den = ((x1-x2)*(y3-y4))-((y1-y3)*(x3-x4))
        if den == 0:
            return
        t = (((x1-x3)*(y3-y4))-((y1-y3)*(x3-x4)))/den
        u = (-((x1-x2)*(y1-y3))-((y1-y2)*(x1-x3)))/den

        if t > 0 and t <1 and u > 0:
            px,py = (x1 +t*(x2-x1)),(y1+t*(y2-y1))
            pygame.draw.line(window,(255,255,255),(self.x2,self.y2),(px,py))
            pygame.draw.circle(window,RED,(x2,y2),4)
            
        else:
            return

class Particle:
    def __init__(self):
        self.x = 300       
        self.y = 250

    def draw(self):
        pygame.draw.circle(window,(PURPLE),(self.x,self.y),10)
    def cast(self):
        for a in range(0,360,10):
            ray = Ray((self.x,self.y),(a))
            ray.draw()
            ray.cast(wall)

casting = True

wall = Boundary((100,400),(400,400))
ray = Ray((50,250),280)
part= Particle()
while casting:
    window.fill((0,0,0))
    mousex,mousey = pygame.mouse.get_pos()
   
    wall.draw()
    #ray.draw()
    #ray.cast(wall)
    part.draw()
    part.cast()
    if mousex > 0 and mousex < 600 and mousey > 0 and mousey < 500:
        #ray.look_at(mousex,mousey)
        pass






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            casting = False

    pygame.display.flip()
pygame.quit()
