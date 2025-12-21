#importing the necesary modules
import pygame
import random

#game initialization
pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Einstein snake")
font  = pygame.font.Font(None,36)
starttime = pygame.time.get_ticks()

#setiing constants being used in the game
BLACK = (0,0,0)
width = 400
height = 400
score_val = 0
body_l = 3
time = '0:0'
grid_cell = 10
speed  =10
vel_x,vel_y = speed,0
text_x,text_y = 9,8
einstein = True
body =[]
pause = False
lose = False

#calculating positions
no_cellsx = width / grid_cell
no_cellsy = height / grid_cell
head_x = grid_cell * 10
head_y = grid_cell *15
pos_x =  random.randint(2,int(no_cellsx)-1) *grid_cell
pos_y  = random.randint(12,int(no_cellsy)-1)*grid_cell

body.append((head_x,head_y))

#draw the snake head
def snake_head():
     pygame.draw.rect(window,(255,255,255),(head_x,head_y,10,10))

#generate food
def food():
     pygame.draw.rect(window,(0,0,0,0),(pos_x,pos_y,10,10))
#restart the game
def restart():
     body.clear()
     body_l =  3
     starttime = pygame.time.get_ticks()
     
#draw the snake body
def snakebody():
     if len(body) >2 :
          for x in range(0,len(body)-1):
               pygame.draw.rect(window,(128,0,128),(body[x][0],body[x][1],10,10))

#the main game loop
while einstein:
     window.fill((0,0,0,0))
     pygame.draw.rect(window,(255,0,0),(5,100,width,height))
     pygame.draw.rect(window,(255,255,255),(10,5,470,50))
     snake_head()
     food()
     snakebody()
     
     #get the keyboard events
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  einstein = False
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_DOWN:
                   if vel_x !=0:
                         vel_y = speed
                         vel_x = 0
               if event.key == pygame.K_UP:
                    if vel_x != 0:
                         vel_y = -speed
                         vel_x = 0
               if event.key == pygame.K_LEFT:
                   if vel_y != 0:
                         vel_x = -speed
                         vel_y = 0
               if event.key == pygame.K_RIGHT:
                   if vel_y !=0:
                         vel_x = speed
                         vel_y = 0
               if event.key == pygame.K_SPACE:
                    pause = not pause
               
               #logic to restart the game
               if lose:
                    if event.key == pygame.K_RETURN:
                         lose = False
                         if vel_x !=0:
                              vel_x =0
                              vel_y = speed
                         else:
                              vel_x = speed
                              vel_y = 0
                         starttime = pygame.time.get_ticks()
                         body_l = 3
                         starttime = pygame.time.get_ticks()
                         score_val =0
                         restart()
     #check for collisions with food
     if head_x == pos_x and head_y == pos_y  :
             pos_x,pos_y =   random.randint(2,int(no_cellsx)-1) *grid_cell,random.randint(12,int(no_cellsy)-1)*grid_cell
             score_val +=1
             body_l +=5
             food()
       #logic for time
     def time():
          global time_s,time_H,time_milli
          time_milli = pygame.time.get_ticks()-starttime
          time_mill = time_milli
          time_s = (time_milli//1000)%60
          time_milli = (time_milli//10)%100
          time_H=(time_mill//1000)//60
         
     
     #display the score value
     text_surface = font.render(str(score_val),True,BLACK)
     text_x = ((10 +(470 - text_surface.get_width()))//1)-10
     text_y = (5 +(50 - text_surface.get_height()))//2
     window.blit(text_surface,(text_x,text_y))

     #check if the snake head collides with the wall
     if head_x > 400:
          head_x = 10
     if head_x < 10:
          head_x = 400
     if head_y > 490:
          head_y = 100
     if head_y < 100:
          head_y = 490

     #logic for the snake motion while checking lose and pause status
     if not  pause:
          if not lose:
               head_x +=vel_x
               head_y +=vel_y 
               body.append((head_x,head_y))

               if len(body)> body_l:
                    body.pop(0) 
               time()
                 
     #logic to check if snake head collides with the body
     for x in range(0,len(body)-1):
          
          if head_x == body[x][0] and head_y == body[x][1]:
               lose = True
               vel_x = 0
               vel_y =0
               text_value = 'You loose. Press Enter to start a new game'
               text = font.render(text_value,True,BLACK)
               text_px = (width - text.get_width())//2
               text_py = (height - text.get_height())//2
               window.blit(text,(text_px,text_py)) 
          else:
               #logic to pause the game
               if  pause:
                    #display that game is paused
                    text_val = 'Game paused'
                    text = font.render(text_val,True,BLACK)
                    text_px = (width - text.get_width())//2
                    text_py = (height - text.get_height())//2
                    window.blit(text,(text_px,text_py)) 
    
     #display time     
     time_val = f'{time_H} : {time_s} : {time_milli}'
     text = font.render(time_val,True,BLACK)
     text_px = (10+(470 - text.get_width()))//4
     text_py = (5+(50 - text.get_height()))//2
     window.blit(text,(text_px,text_py)) 
# logic for bonus food
# logic difficulty
# logic for the highest score     
     pygame.display.flip()
     pygame.time.Clock().tick(10)

pygame.quit()