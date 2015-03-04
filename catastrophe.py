import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

white = (255,255,255)
pink = (205, 140, 149)
gameDisplay = pygame.display.set_mode((800, 450))

pygame.display.update()
pygame.display.set_caption('Catatstrophe')


myImage = pygame.image.load("nyan3.gif")
imagerect = myImage.get_rect()






clock = pygame.time.Clock()
def gameLoop():
    gameEnd = False
    lead_x = 750
    lead_y = randint(0,450)
    lead_x_change = 10
    cat_x = 10
    cat_y = 150
    while not gameEnd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEnd = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    cat_y += 50
                if event.key == pygame.K_UP:
                    cat_y -= 50
        if cat_y >= 450 or cat_y <= 0:
            gameEnd = True
        lead_x -= lead_x_change

        gameDisplay.fill(white)

        enemy = pygame.draw.rect(gameDisplay, pink, [lead_x,lead_y,20,20])
        gameDisplay.blit(myImage,(cat_x, cat_y))
        pygame.display.update()
        
        clock.tick(30)
    pygame.quit()
    quit()

gameLoop()
