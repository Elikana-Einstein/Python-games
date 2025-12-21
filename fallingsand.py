import pygame
import random
import sys
pygame.init()
window = pygame.display.set_mode((600,500))
pygame.display.set_caption("Einstein falling sand")
cols = int(600/20)
rowss = int(500/20)
grid = [[x for x in range(cols)] for _ in range(rowss)]
def index(i, j):
    # valid i in [0, cols-1], j in [0, rows-1]
    if i < 0 or j < 0 or i > cols-1 or j > rows-1:
       return -1
    else:
        return i * rows + j

c,r =0,1
change= 1

class cell:
    def __init__(self,x,y,v):
        self.c =x
        self.r=y
        self.value= v
        self.pos = 25
    def draw(self):
        color = (255, 255, 255) if self.value == 1 else (255, 255, 0)
        pygame.draw.rect(window,color,(self.c*20,self.r*20,20,20),self.value)
    def check_next(self):
            if grid[self.r][self.c].value ==0 and self.r < rowss - 1:
                if grid[self.r+change][self.c].value ==1:
                        grid[self.r][self.c].value =1
                        grid[self.r+change][self.c].value =0
     


for x in range(cols):
    for y in range(rowss):
        grid[y][x]=cell(x,y,1)
falling =True
grid[random.randint(0,20)][random.randint(0,25)].value = 0

mousex,mousey =None,None

len_row ={}
for x in range(cols):
    len_row[x]=0
already = set()
while falling:

    mousex,mousey= pygame.mouse.get_pos()

    sand =[]
    rows ={}
    for x in range(len(grid)-1):
        for y in range(len(grid[0])-1):
           if grid[x][y].value == 0:
               #sand.append(grid[x][y])
               pass
    for x in sand:
        rows[x.c] = x.r
    for r in range(rowss - 1, -1, -1):  # bottom-up to avoid overwrite
        for c in range(cols):
            grid[r][c].check_next()
    x = len(rows)
    window.fill((0,0,0))
    for x in range(len(grid)):
        for y in range(len(grid[0])):
           grid[x][y].draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            falling = False
    for n in range(x):
        for x in rows:
                k=grid[rows[x]][x].check_next()
    for x in already:
        pass
    if 1 <= mousex < 600 and 1 <= mousey < 500:
        grid[mousey // 20][mousex // 20].value = 0
    
    pygame.display.flip()
    pygame.time.Clock().tick(30)
pygame.quit()