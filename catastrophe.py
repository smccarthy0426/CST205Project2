import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

white = (255,255,255)
pink = (255, 20, 147)
green = (0,155,0)
gold = (255,215,0)
black = (0,0,0)
orange = (255,102,0)
purple = (160,32,240)
red = (255,0,0)

display_w = 800
display_h = 450
gameDisplay = pygame.display.set_mode((display_w,display_h))

pygame.display.update()
pygame.display.set_caption('Catatstrophe')


myImage = pygame.image.load("nyan3.gif")
imagerect = myImage.get_rect()

font = pygame.font.SysFont(None, 25)

def enemy1(enemy1_x,enemy1_y,block_size):
    pygame.draw.rect(gameDisplay, pink, [enemy1_x,enemy1_y,block_size,block_size])
    pygame.display.update()

def enemy2(enemy2_x,enemy2_y,block_size):
    pygame.draw.rect(gameDisplay, gold, [enemy2_x,enemy2_y,block_size,block_size])
    pygame.display.update()
    
def enemy3(enemy3_x,enemy3_y,block_size):
    pygame.draw.rect(gameDisplay, green, [enemy3_x,enemy3_y,block_size,block_size])
    pygame.display.update()
    
def enemy4(enemy4_x,enemy4_y,block_size):
    pygame.draw.rect(gameDisplay, orange, [enemy4_x,enemy4_y,block_size,block_size])
    pygame.display.update()
    
def enemy5(enemy5_x,enemy5_y,block_size):
    pygame.draw.rect(gameDisplay, purple, [enemy5_x,enemy5_y,block_size,block_size])
    pygame.display.update()
    

def enemy_speed(difficulty):
    speed = 10
    if difficulty == 1:
        speed = 5
    elif difficulty == 2:
        speed = 10
    elif difficulty == 3:
        speed = 15
    elif difficulty == 4:
        speed = 20
    else:
        speed = 25
    return speed
        
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 250])

def lives_to_screen(msg,color):
    lives_text = font.render(msg, True, color)
    gameDisplay.blit(lives_text, [250, 10])



clock = pygame.time.Clock()
def gameLoop():
    #initialize game elements
    gameEnd = False
    block_size = 15
    enemy1_x = display_w - block_size
    enemy1_y = round(randint(0,90)/10.0)*10.0
    enemy2_x = display_w - block_size
    enemy2_y = round(randint(91,180)/10.0)*10.0
    enemy3_x = display_w - block_size
    enemy3_y = round(randint(181,270)/10.0)*10.0
    enemy4_x = display_w - block_size
    enemy4_y = round(randint(270,361)/10.0)*10.0
    enemy5_x = display_w - block_size
    enemy5_y = round(randint(361,450)/10.0)*10.0
    cat_x = 10
    cat_y = 150
    gameOver = False
    difficulty = 5
    while not gameEnd:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("You failed. Press C to continue", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
            

        #While the game is running, allow the user to move the main character
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEnd = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    cat_y += 50
                if event.key == pygame.K_UP:
                    cat_y -= 50
        if cat_y >= 450 or cat_y <= 0:
            gameOver = True


        #use the speed function to set the constant change of the enemies
        enemy1_x_change = enemy_speed(difficulty) +20
        enemy2_x_change = enemy_speed(difficulty) +10
        enemy3_x_change = enemy_speed(difficulty) 
        enemy4_x_change = enemy_speed(difficulty) -5
        enemy5_x_change = enemy_speed(difficulty) -10

        #Constant movement for enemies
        enemy1_x -= enemy1_x_change
        enemy2_x -= enemy2_x_change
        enemy3_x -= enemy3_x_change
        enemy4_x -= enemy4_x_change
        enemy5_x -= enemy5_x_change


        gameDisplay.fill(white)

        #Call the enemy functions to draw the enemies
        enemy1(enemy1_x,enemy1_y,block_size)
        enemy2(enemy2_x,enemy2_y,block_size)
        enemy3(enemy3_x,enemy3_y,block_size)
        enemy4(enemy4_x,enemy4_y,block_size)
        enemy5(enemy5_x,enemy5_y,block_size)


        
        gameDisplay.blit(myImage,(cat_x, cat_y))
        pygame.display.update()

        #If the main character and the enemies touch, the game will end 
        if abs(cat_y - enemy1_y) <= 15 and abs(cat_x - enemy1_x) <= 15:
            gameOver = True

        if abs(cat_y - enemy2_y) <= 15 and abs(cat_x - enemy2_x) <= 15:
            gameOver = True
            
        if abs(cat_y - enemy3_y) <= 15 and abs(cat_x - enemy3_x) <= 15:
            gameOver = True

        if abs(cat_y - enemy4_y) <= 15 and abs(cat_x - enemy4_x) <= 15:
            gameOver = True

        if abs(cat_y - enemy5_y) <= 15 and abs(cat_x - enemy5_x) <= 15:
            gameOver = True

        #Give the enemies a new starting position after the enemies pass the cat
        if enemy1_x <= 0:
            enemy1_x = display_w - block_size
            enemy1_y = round(randint(0,display_h - block_size)/10.0)*10.0
            
        if enemy2_x <= 0:
            enemy2_x = display_w - block_size
            enemy2_y = round(randint(0,display_h - block_size)/10.0)*10.0
            
        if enemy3_x <= 0:
            enemy3_x = display_w - block_size
            enemy3_y = round(randint(0,display_h - block_size)/10.0)*10.0

        if enemy4_x <= 0:
            enemy4_x = display_w - block_size
            enemy4_y = round(randint(0,display_h - block_size)/10.0)*10.0

        if enemy5_x <= 0:
            enemy5_x = display_w - block_size
            enemy5_y = round(randint(0,display_h - block_size)/10.0)*10.0
            
        clock.tick(30)
    pygame.quit()
    quit()

gameLoop()
