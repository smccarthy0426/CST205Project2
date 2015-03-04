import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

white = (255,255,255)
pink = (205, 140, 149)
black = (0,0,0)

display_w = 800
display_h = 450
gameDisplay = pygame.display.set_mode((display_w,display_h))

pygame.display.update()
pygame.display.set_caption('Catatstrophe')


myImage = pygame.image.load("nyan3.gif")
imagerect = myImage.get_rect()

font = pygame.font.SysFont(None, 25)
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 250])



clock = pygame.time.Clock()
def gameLoop():
    gameEnd = False
    block_size = 15
    enemy_x = display_w - block_size
    enemy_y = randint(0,display_h)
    enemy_x_change = 10
    cat_x = 10
    cat_y = 150
    gameOver = False
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
        enemy_x -= enemy_x_change

        gameDisplay.fill(white)

        enemy = pygame.draw.rect(gameDisplay, pink, [enemy_x,enemy_y,block_size,block_size])
        gameDisplay.blit(myImage,(cat_x, cat_y))
        pygame.display.update()
        
        clock.tick(30)
    pygame.quit()
    quit()

gameLoop()
