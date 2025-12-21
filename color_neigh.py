#import the necessary modules
import pygame
import random
from color import THECOLORS,num_color

#iniliatize the game and set variables
pygame.init()
WIDTH,HEIGHT = 605,450
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Einstein color windows")
cells_x,cells_y = int(WIDTH/40),int(HEIGHT/40)
color = True


#an oject for each cell in th grid
class Cell:
    def __init__(self,x,y):
        self.x =x
        self.y = y
        self.value = 0
        self.visited = False
        self.walls = [True,True,True,True]
    #method to draw each cell having its own walls
    def draw(self):
        #left
        if self.walls[0]:
            pygame.draw.line(window,THECOLORS['black'],(self.x*40,self.y*40+40),(self.x*40 ,self.y*40))
        #right
        if self.walls[1]:
            pygame.draw.line(window,THECOLORS['white'],(self.x*40+40,self.y*40+40),(self.x*40 +40,self.y*40))
        #top
        if self.walls[2]:
            pygame.draw.line(window,THECOLORS['red'],(self.x*40,self.y*40),(self.x*40+40 ,self.y*40))
        #bottom
        if self.walls[3]:
            pygame.draw.line(window,THECOLORS['white'],(self.x*40,self.y*40+40),(self.x*40+40 ,self.y*40+40))
   



#object grid that has all cells to enable acces to cells in groups
class Grid:
    def __init__(self):
        self.cells = [[Cell(x,y) for x in range(cells_x)] for y in range(cells_y) ]
    
    #method to draw the cells 
    def draw(self):
        for i in range(cells_y):
            for j in range(cells_x):
                self.cells[i][j].draw()
#
#an object to create the maze
class Head:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.dirx = 1 #control motion in the y direction
        self.diry=1   #control motion in the x direction
        self.dir = False  #helper to change direction
        self.color = THECOLORS['purple']
        self.distance = random.randint(1,6) #helper to controll the length of every tunnel
        self.dis = 0 #helper to calculate the length of the maze
      
    #method to move the head around the maze
    def move(self):
        self.distance-=1
        self.dis+=1

        if  self.dir:
            #logic to change the direction in the x direction whenever it hits the end of the maze
            self.x+=self.dirx
            if self.x+1 > cells_y-1 or self.x <1:
                self.dirx=-self.dirx

        else:
            #logic to change the direction in the y direction whenever it hits the end of the maze
            self.y+=self.diry
            if self.y+1 > cells_x-1 or self.y <1:
                self.diry=-self.diry

        #make the head move
        pygame.draw.rect(window,THECOLORS['purple'],(grid.cells[self.x][self.y].x*40,grid.cells[self.x][self.y].y*40,40,40))
        
        #logic to change the direction from x to y and vice versa
        if self.distance == 0:
            if self.dir:
                self.dir = False
            else:
                self.dir = True
            #initilize a new length for tunnel
            self.distance= random.randint(1,6)
        return self.dis  #return this distance to stop the maze from being created any more
    
    #method to remove walls to allow the maze to be created
    def remove_walls(self,grid):
        #remove walls while moving in the y direction
        if not self.dir:
            if self.diry ==1:
               grid.cells[self.x][self.y].walls[1] = False
               grid.cells[self.x][self.y+1].walls[0]= False
            if self.diry ==-1:
               grid.cells[self.x][self.y].walls[0] = False
               grid.cells[self.x][self.y-1].walls[1]= False
               
        else:
        #remove walls while moving in the x direction
            if self.dirx ==1:
               grid.cells[self.x][self.y].walls[3] = False
               grid.cells[self.x+1][self.y].walls[2]= False
            elif self.dirx == -1:
                grid.cells[self.x][self.y].walls[2] = False
                grid.cells[self.x-1][self.y].walls[3]= False
        return (self.x,self.y)


class Cat:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dancing_time =0
        self.found = False
    def draw(self,current_cell,goal):
        #draw the looks of the cat
        grid_ =  grid.cells[current_cell[0]][current_cell[1]]
        pygame.draw.circle(window,THECOLORS['blue2'],(grid_.x*40+20,grid_.y*40+20),18,1)
        pygame.draw.circle(window,THECOLORS['red'],(  grid_.x*40+10,grid_.y*40+15),3)
        pygame.draw.circle(window,THECOLORS['red'],(  grid_.x*40+30,grid_.y*40+15),3)
        pygame.draw.circle(window,THECOLORS['blue2'],(grid_.x*40+20,grid_.y*40+20),3)
        pygame.draw.line(window,THECOLORS['purple'],( grid_.x*40+15,grid_.y*40+30),(grid_.x*40+25,grid_.y*40+30),2)

        #if it find the rat it celebrates a little
        if current_cell[0] == goal[0] and current_cell[1] == goal[1]:
            if not self.found:
                self.dancing_time +=1
                pygame.draw.circle(window,THECOLORS[num_color[random.randint(1,9)]],(grid_.x*40+20,grid_.y*40+20),18,2)
                if self.dancing_time < 10:
                    return True
                else:
                    self.found = True
                    return False

class Rat:
    def __init__(self):
        self.x = None
        self.y = None
    
    #make the rat hide hide at som random position in the maze
    def draw(self,idx):
        #draw the looks of the rat
        grid_ =  grid.cells[idx[0]][idx[1]]
        pygame.draw.circle(window,THECOLORS['white'],( grid_.x*40+20,grid_.y*40+20),18)
        pygame.draw.circle(window,THECOLORS['red'],(   grid_.x*40+20,grid_.y*40+20),18,1)
        pygame.draw.circle(window,THECOLORS['green'],( grid_.x*40+10,grid_.y*40+15),3)
        pygame.draw.circle(window,THECOLORS['blue'],(  grid_.x*40+30,grid_.y*40+15),3)
        pygame.draw.circle(window,THECOLORS['yellow'],(grid_.x*40+20,grid_.y*40+20),3)


#create the grid object
grid = Grid()
#create the maze generator object
head = Head(2,0)
#create the cat object
cat = Cat(2,0)

current_cell = (2,0)
hide_idx = None
#create the rat object
rat = Rat()


#help the cat find the path to locate the rat
def check_path(current_cell,cat):
    path = []
    x = current_cell[0]
    y = current_cell[1]

    if x>0 :
        #top and botom
        if grid.cells[x][y].walls[2] == False and  grid.cells[x-1][y].walls[3] == False and not  grid.cells[x-1][y].visited :
                path.append((x-1,y))
    if y>0 :
        #left and right
        if grid.cells[x][y].walls[0] == False and  grid.cells[x][y-1].walls[1] == False and not grid.cells[x][y-1].visited:
            path.append((x,y-1))
    if x<cells_y-1  :
        #bottom and top
        if grid.cells[x][y].walls[3] == False and  grid.cells[x+1][y].walls[2] == False and not  grid.cells[x+1][y].visited :            
                path.append((x+1,y))
    if y<cells_x-1 :
        #right and left
        if grid.cells[x][y].walls[1] == False and  grid.cells[x][y+1].walls[0] == False and not grid.cells[x][y+1].visited :
            path.append((x,y+1))

    if len(path)>0:
        cell = random.choice(path)
        grid.cells[cell[0]][cell[1]].visited = True
        if cat.found:
            return None
        else:
            return cell
#the depth first search algorith

#the breadth first search algorith

#mark the visited cell to help in backtracking
visited_cell = [current_cell]
path = [current_cell]
#a helper to help the rat find a random positon to hide
hide = []
dis = 0
tick =30

#mark the starting cell as visited
grid.cells[current_cell[0]][current_cell[1]].visited = True

#the main game loop
while color:
    window.fill(THECOLORS['wheat'])
    #draw the cells
    grid.draw()
    #
    k=head.remove_walls(grid)
    #stop maze generation 
    if dis < 100:
        dis=head.move()
        hide.append(k)
    if dis == 100:
        if len(hide)>0:
            # find a random position for the rat to hide
            hide_idx = random.choice(hide)
            hide = []
        #make the rat hide at the picked position
        rat.draw(hide_idx)
        tick=5   

        foundTheRat = cat.draw(current_cell,hide_idx)
        if not foundTheRat:

            next_cell = check_path(current_cell,cat)
        else:
            #if the cat finds the rat make it celebrate 
            current_cell = hide_idx
        if next_cell:
            current_cell = next_cell
            visited_cell.append(current_cell)
        else:
            #the backtracking algorithm
            if len(visited_cell)>0:
                current_cell = visited_cell.pop()
                if cat.found:
                    path.append(current_cell)
            if len(visited_cell)==0:
                current_cell=path.pop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            color = False
       
    pygame.display.flip()
    pygame.time.Clock().tick(tick)
pygame.quit()