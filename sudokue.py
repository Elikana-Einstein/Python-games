#import libraries and mudules
import pygame
import math
from color import THECOLORS,num_color
from puzzle import grid_puzzle,insert_num,check_col,check_row,blocks,check_block

#inititilize the game
pygame.init()
WIDTH = 630
HEIGHT = 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Einstein sudoku")
font = pygame.font.Font(None,26)
sudoku = True
insert_num()
#an object representing each cell in the grid
class Cell:
    def __init__(self,x,y,value=None):
        self.value = value
        self.active =False
        self.walls = [False,False,False,False]
        self.row = x
        self.col = y
        self.color = None

    def draw(self):
        #logic for showing whether a cell is active or not
        self.color = THECOLORS["red"] if self.active == True else THECOLORS["black"]
        #top
        if self.walls[0]:
            pygame.draw.line(window,self.color,((self.row+3)*40,(self.col+2)*40),(((self.row+3)*40)+40,((self.col+2)*40)),1)
        #bottom
        if self.walls[1]:
            pygame.draw.line(window,self.color,(((self.row+3)*40)+40,((self.col+2)*40)+40),(((self.row+3)*40),((self.col+2)*40)+40),1)
        #left
        if self.walls[2]:
            pygame.draw.line(window,self.color,((self.row+3)*40,(self.col+2)*40),(((self.row+3)*40),((self.col+2)*40)+40),1)
        #right
        if self.walls[3]:
            pygame.draw.line(window,self.color,(((self.row+3)*40)+40,((self.col+2)*40)+40),(((self.row+3)*40)+40,((self.col+2)*40)),1)

    def display_values(self):
        #displaying the numbers
        if self.value == 0:
            pass
        else:
            text_surface = font.render(str(self.value),True,THECOLORS[num_color[self.value]])
            text_x = (((((self.row+3)*40)+40)-text_surface.get_width())-15)
            text_y = (((((self.col+2)*40)+40)-text_surface.get_width())-15)
            window.blit(text_surface,(text_x,text_y))

#object for the entire grid containg cell objects
class Grid:
    def __init__(self):
        self.cells = [[Cell(x,y) for x in range(9)] for y in range(9) ]
        self.rows = [[] for _ in range(9)]
        self.cols = [[] for _ in range(9)]
        self.block = [[] for _ in range(9)]

    #drawing boxes to represent each cell
    def draw(self):
        for x in range(3,12):
            for  y in range(2,11):
                pygame.draw.rect(window,THECOLORS["blanchedalmond"],(x*40,y*40,40,40),2)
    #function to activate and deactivate cells
    def deactivate_cell(self,x,y):
        #Deactivate any aactive cell
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].active:
                    for z  in range(4):
                       self.cells[i][j].walls[z] = False
                       self.cells[i][j].active = False
        #activate the current cell 
        for z in range(4):
            self.cells[x][y].walls[z] = True
        self.cells[x][y].active = True

    #insert a number to a cell
    def insert_num(self,num):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].active:
                    if num == 0:
                        grid_puzzle[i][j] =0
                    for block in blocks:
                        for cell in block:
                            if cell == (i,j):
                                check_block(num,block,cell)
                                break
                    if check_col(num,j):
                        if check_row(num,i):
                            grid_puzzle[i][j] = num
                        
        


#object to represent each  block
class Block:
    def __init__(self):
        pass

#function to draw lines to separate each block
def draw_block_lines(grid):
        for x in range(9):
            for y in range(2,6,3):
                grid.cells[x][y].walls[3] = True
        for x in range(2,6,3):
            for y in range(9):
                grid.cells[x][y].walls[1] = True


    
#create object grid
grid = Grid()

mousex,mousey = None,None

#the main loop for the game
while sudoku:
    window.fill(THECOLORS["aquamarine"])

    #draw each cell in the grid
    grid.draw()
    #draw each block
    draw_block_lines(grid)

    #add values to cells
    for row in range(9):
        for col in range(9):
            grid.cells[row][col].value = grid_puzzle[row][col]
    
    #show the active cell and display values to the grid
    for x in range(9):
        for y in range(9):
            grid.cells[x][y].draw()
            grid.cells[x][y].display_values()

    #add event to the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sudoku=False

        #get the position of the mouth to set the active cell
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            mousex = (mousex-120)//40
            mousey = (mousey-80)//40
            if mousex >-1 and mousex < 9 and mousey > -1 and mousey < 9:
                grid.deactivate_cell(mousey,mousex)
        #get the num key pressed
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_9:
                    grid.insert_num(9)

                if event.key == pygame.K_1:
                    grid.insert_num(1)

                if event.key == pygame.K_2:
                    grid.insert_num(2)

                if event.key == pygame.K_3:
                    grid.insert_num(3)

                if event.key == pygame.K_4:
                    grid.insert_num(4)

                if event.key == pygame.K_5:
                    grid.insert_num(5)

                if event.key == pygame.K_6:
                    grid.insert_num(6)

                if event.key == pygame.K_7:
                    grid.insert_num(7)

                if event.key == pygame.K_8:
                    grid.insert_num(8)
                if event.key == pygame.K_DELETE:
                    grid.insert_num(0)
    pygame.display.flip()

pygame.quit()