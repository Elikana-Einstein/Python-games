#import the necessary module
import pygame
import random
from queue import Queue
pygame.init()

switch =set()
#set the constants
BLACK = (0,0,0)
PURPLE = (128,0,128)
WHITE = (255,255,255)
RED = (0,255,0)
info = pygame.display.Info()
HEIGHT,WIDTH =250,300
cell_w =20
cols = int(WIDTH/cell_w)
rows = int(HEIGHT/cell_w)
tick = 250

#initialize the game
window =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Einstein maze")

#find the grid position
def index(i, j):
    # valid i in [0, cols-1], j in [0, rows-1]
    if i < 0 or j < 0 or i > cols-1 or j > rows-1:
       return -1
    else:
        return i * rows + j

grids =[] #store the positions of each cell
stack =[] #implement stack for creating maze
checkStack = []
way = []
visited = {1}
generation_done = False
queue = []
que_check=[]
solving = False


#create an object for each cell
class cell:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.wall = [True,True,True,True]
        self.visited = False
        self.path = False
        self.checked =False
    #draw the four lines for each cell
    def draw(self):
        x = self.i * cell_w
        y = self.j * cell_w
        if self.wall[0]:
            pygame.draw.line(window,WHITE,(x,y), (x+cell_w,y),2)
        if self.wall[1]:
            pygame.draw.line(window,WHITE,(x+cell_w,y+cell_w),(x+cell_w,y),2)

        if self.wall[2]:
            pygame.draw.line(window,WHITE,(x+cell_w,y+cell_w),(x,y+cell_w),2)

        if self.wall[3]:
            pygame.draw.line(window,WHITE,(x,y+cell_w),(x,y),2)
        if  self.path:
                pygame.draw.rect(window,PURPLE,(x+1,y+1,cell_w-1,cell_w-1))
                
    #check a neighbour to explore
    def checkNeighbours(self):
            neighbours = []
            t  = index(self.i-1,self.j)
            if t != -1:
                top = grids[t]
                if not top.visited:
                    neighbours.append(top)
            r  = index(self.i,self.j+1)
            if r != -1:
                right = grids[r]
                if not right.visited:
                    neighbours.append(right)
            b  = index(self.i+1,self.j)
            if b != -1:
                bottom = grids[b]
                if not bottom.visited:
                    neighbours.append(bottom)
            l  = index(self.i,self.j-1)
            if l != -1:
                left = grids[l]
                if not left.visited:
                    neighbours.append(left)
            
            if neighbours:
                n = random.randint(0,len(neighbours)-1)
                return neighbours[n]
            return None
    #solv the maze
    def solve_maze(self):
        path =[]
        current_cell.checked =True
        if current_cell.wall[0] == False :
              path.append(grids[index(self.i,self.j-1)])
        if current_cell.wall[1] == False :

              path.append(grids[index(self.i+1,self.j)])

        if current_cell.wall[2] == False :
              path.append(grids[index(self.i,self.j+1)])

        if current_cell.wall[3] == False :
              path.append(grids[index(self.i-1,self.j)])
        if self not in checkStack:
            visited.add(index(self.i,self.j))
        
        for x in path:
             if not x.checked :
                  return x
    
    def gotten_solution(self):
        print('hhh')
        if self in way:
            pass
            #self.path = True
    
    
#remove walls to create the maze
def remove_walls(c, n):
        dx = c.i - n.i
        dy = c.j - n.j
        # c is the neighbor, n is the current cell
        if dx == 1 and dy == 0:
            # c is to the right of n
            n.wall[1] = False
            c.wall[3] = False
        elif dx == -1 and dy == 0:
            # c is to the left of n
            n.wall[3] = False
            c.wall[1] = False
        elif dy == 1 and dx == 0:
            # c is below n
            n.wall[2] = False
            c.wall[0] = False
        elif dy == -1 and dx == 0:
            # c is above n
            n.wall[0] = False
            c.wall[2] = False

def open_neighbors(idx):
    c = grids[idx]
    neighbors = []
    # top
    if not c.wall[0]:
        t = index(c.i, c.j-1)
        if t != -1 and t not in que_check:
            neighbors.append(t)
    # right
    if not c.wall[1] :
        r = index(c.i+1, c.j)
        if r != -1 and r not in que_check:
            neighbors.append(r)
    # bottom
    if not c.wall[2]:
        b = index(c.i, c.j+1)
        if b != -1 and b not in que_check:
            neighbors.append(b)
    # left
    if not c.wall[3]:
        l = index(c.i-1, c.j)
        if l != -1 and l not in que_check:
            neighbors.append(l)
    return neighbors
            

def highlight(current_cell):
        current_cell.path =True

def solved():
    for x in grids:
         x.path = False
follow =False
def draw_path():
    follow =True
#get the coordinate of each grid cell
for i in range(cols):
    for j in range(rows):
        k = cell(i,j)
        grids.append(k)
current_cell = grids[0]

gr=0
current =0
maze = True
while maze:
    window.fill(RED)
    
    for x in grids:
        x.draw()
    current_cell.visited = True
    next_cell = current_cell.checkNeighbours()
    if next_cell:
        remove_walls(next_cell,current_cell)
        next_cell.visited = True
        stack.append(current_cell)
        current_cell = next_cell

    elif len(stack) >0:
        current_cell = stack.pop()
    if len(stack)==0:
        switch.add(1)
    #current_cell.gotten_solution()
    #maze generation is done, start solving
    ''' if len(stack)== 0 :
        current_cell.checked =True
        current_cell.path =True
        next_check=current_cell.solve_maze()
        if next_check:
            highlight(next_check)
            checkStack.append(current_cell)
            current_cell = next_check
        elif len(checkStack)>0:
            current_cell = checkStack.pop()
            visited.add(index(current_cell.i,current_cell.j))

            if len(checkStack) == 0:
                solved()
                generation_done = True'''
    if generation_done:
        '''start_idx = 0
        end_idx = len(grids)-1
        from collections import deque
        q= deque([start_idx])
        visited_bfs = {start_idx}
        parent = {start_idx:None}
        found = False
        while q:
                cur = q.popleft()
                if cur == end_idx:
                    found = True
                    break
                for nb in open_neighbors(cur):
                    if nb not in visited_bfs:
                        visited_bfs.add(nb)
                        parent[nb] = cur
                        q.append(nb)
        if found:
             p = end_idx
             while p is not None:
                 #grids[p].path = True
                 way.append(grids[p])
                 p = parent[p]
        x= 0
        follow =True
        tick = 10
        generation_done = False'''  # prevent re-running
    if follow and gr < len(way):
        way[gr].path = True
        gr+=1
    pygame.draw.rect(window,BLACK,(current_cell.i*cell_w+1,current_cell.j*cell_w+1,cell_w-2,cell_w-2))


    #try to implement depth first search
    if len(switch) ==1:
        tick =3
        neigh = open_neighbors(current)
        que_check.append(current)
        if len(neigh)==1:
            if len(que_check)>0:
                queue.append(current)
                queue.append(neigh[0])
            current = neigh[0]

            grids[current].path = True
        if len(neigh) == 2:
            queue.append(current)
            que_check.append(current)
            current=neigh[0]
            grids[current].path = True
        if len(neigh) ==0:
            que_check.append(current)
            current = queue.pop()
            grids[current].path=False
            
    #get keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            maze = False

    pygame.display.flip()
    pygame.time.Clock().tick(tick)  # Slower speed to see generation

pygame.quit()
