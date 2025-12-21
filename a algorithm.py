import pygame
import random 
import math
WIDTH = 500    
HEIGHT = 500 
GREEN = (0,255,0)  
RED =(255,0,0)
WHITE =(255,255,255)
PURPLE = (128,0,128)
cols,rows = 5,5
width= int(WIDTH/cols)
height= int(WIDTH/rows)

grid = [[5 for _ in range(cols) ] for _ in range(rows)]
pygame.init()
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('A* algorithm')
einstein = True

open_set = []
closed_set = []

class spot:
    def __init__(self,x,y):
        self.f = 0
        self.g = 0
        self.h = 0
        self.x = x
        self.y = y
        self.neighbor = []
    def draw(self,color,y=1):
        pygame.draw.rect(window,color,(self.x*width,self.y*height,width,height),y)
    def addNeighbour(self,grid):
        x = self.x
        y= self.y
        if x < rows-1:
            self.neighbor.append(grid[x+1][y])
        if x >0:
            self.neighbor.append(grid[x-1][y])
        if y < rows-1:
            self.neighbor.append(grid[x][y+1])
        if y >0:
            self.neighbor.append(grid[x][y-1])
    def show(self):
        print(
        self.f,
        self.g,
        self.h,
        self.x,
        self.y,
         )
        for x in self.neighbor:
            print(x.x,x.y)


def remove(arr,idx):
    for x in arr:
        if x  == idx:
            arr.remove(x)
def heuristic(a,b):
    d = math.sqrt((b.x-a.x)**2 +(b.y-a.y)**2) #dist(a.x,a.y,b.x,b.y)
    return d
while einstein:
    window.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            einstein = False
    
    for x in range(0,rows):
        for z in range(0,cols):
            grid[x][z] = spot(x,z)
            grid[x][z].draw(RED)
    for x in range(0,rows):
        for z in range(0,cols):
            grid[x][z].addNeighbour(grid)
    start = grid[0][0]
    end = grid[cols-1][rows-1]

    open_set.append(start)
    if len(open_set)>0:
        pass
    pass

    for x in closed_set:
        x.draw(WHITE,0)
    for x in open_set:
        x.draw(WHITE,0)
    
    nearest =0
    for x in range(len(open_set)-1):
        if open_set[x].f < open_set[nearest].f:
            nearest = x
    print(open_set[nearest].x,nearest)
    current = open_set[nearest]
    if current == end:
        print('over')
    #remove(open_set,current)
    closed_set.append(current)
    for x in current.neighbor:
        if x not in closed_set:
            tempG = current.g +1 
        if x in open_set:
            if tempG < x.g:
                x.g = tempG  
        else:
            x.g = tempG
            open_set.append(x)      

        x.h = heuristic(x,end)
        x.f = x.g +x.h
    #current.show()
    pygame.display.flip()

pygame.quit()