import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

white = (255,255,255)
pink = (205, 140, 149)
black = (0,0,0)
red = (255,0,0)

display_w = 800
display_h = 450
gameDisplay = pygame.display.set_mode((display_w,display_h))

pygame.display.update()
pygame.display.set_caption('Catatstrophe')


myImage = pygame.image.load("blinky.gif")
imagerect = myImage.get_rect()

font = pygame.font.SysFont(None, 25)

def enemy(enemy_x,enemy_y,block_size):
     pygame.draw.rect(gameDisplay, pink, [enemy_x,enemy_y,block_size,block_size])
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
    gameEnd = False
    block_size = 15
    enemy_x = display_w - block_size
    enemy_y = round(randint(0,display_h - block_size)/10.0)*10.0
    cat_x = 10
    cat_y = 150
    gameOver = False
    difficulty = 1
    while not gameEnd:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("You failed. Press C to continue", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
            
        
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



        enemy_x_change = enemy_speed(difficulty)
        
        enemy_x -= enemy_x_change



        gameDisplay.fill(white)

        enemy(enemy_x,enemy_y,block_size)
        #enemy = pygame.draw.rect(gameDisplay, pink, [enemy_x,enemy_y,block_size,block_size])
        gameDisplay.blit(myImage,(cat_x, cat_y))
        pygame.display.update()

            

        if enemy_x <= 0:
            enemy_x = display_w - block_size
            enemy_y = round(randint(0,display_h - block_size)/10.0)*10.0
            
        clock.tick(30)
    pygame.quit()
    quit()

gameLoop()
