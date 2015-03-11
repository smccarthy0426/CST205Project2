import pygame, sys, time
from pygame.locals import *
import Tkinter
import tkFileDialog
import tkFont
from random import randint

#Startup

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

screen = pygame.display.set_mode((800, 450))

pygame.display.update()
pygame.display.set_caption('Catatstrophe')


myImage = pygame.image.load("nyan3.png")
imagerect = myImage.get_rect()

font = pygame.font.SysFont(None, 25)


score = 0
clock = pygame.time.Clock()

#Start Menu
def startup():
    #Background Fill
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load('backgroundimage.jpg').convert()
    pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])
    

    #Start Screen
    font = pygame.font.SysFont("helvetica", 36)
    text = font.render("CATATSTROPHE", 1, (1, 1, 1))
    text2 = font.render("Press Enter to start", 1, (1, 1, 1))
    text3 = font.render("Press Esc to quit", 1, (1, 1, 1))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    textpos2 = text.get_rect()
    textpos2.centery = background.get_rect().centery +60
    textpos2.centerx = background.get_rect().centerx
    background.blit(text2,textpos2)
    textpos3 = text.get_rect()
    textpos3.centery = background.get_rect().centery +90
    textpos3.centerx = background.get_rect().centerx
    background.blit(text3,textpos3)
    
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Music Select Screen
def music_select_screen():        
    #Background
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load('backgroundimage.jpg').convert()
    pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])
            
    #Music Select Screen
    font = pygame.font.SysFont("helvetica", 32)
    text = font.render("Select Music", 1, (1, 1, 1))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos) 

            
    #Blit
    screen.blit(background, (0, 0))
    pygame.display.flip()

    music_select()

#User Music Select Input and countdown
def music_select():
    pygame.time.wait(500)
    Tkinter.Tk().withdraw() # Close the root window
    backgroundMusic = tkFileDialog.askopenfilename()
    #Set up music
    pickUpSound = pygame.mixer.Sound(backgroundMusic)
    pygame.mixer.music.load(backgroundMusic)
    

#Countdown Function 
def countdown():
    countdown = 5
    if (countdown ==5):
        while (countdown > 0):
            background = pygame.Surface(screen.get_size())
            background = pygame.image.load('maingamebackgroundimage.jpg').convert()
            pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])
            
            font = pygame.font.SysFont("helvetica", 56)
            text = font.render(str(countdown), 1, (1, 1, 1))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos) 

            
            
            screen.blit(background, (0, 0))
            cat_x = 10
            cat_y = 160
            gameDisplay.blit(myImage,(cat_x, cat_y))
            pygame.display.flip()
            pygame.time.wait(1000)

            
            countdown -= 1

        background = pygame.Surface(screen.get_size())
        background = pygame.image.load('maingamebackgroundimage.jpg').convert()
        pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])
        
        font = pygame.font.SysFont("helvetica", 56)
        text = font.render("GO!", 1, (1, 1, 1))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos) 
    
        screen.blit(background, (0, 0))
        cat_x = 10
        cat_y = 160
        gameDisplay.blit(myImage,(cat_x, cat_y))
        pygame.display.flip()
        pygame.time.wait(1000)
        pygame.mixer.music.play(-1, 0.0)
        musicPlaying = True
        
#Show score function/Game over
def show_score():
            background = pygame.Surface(screen.get_size())
            background = pygame.image.load('maingamebackgroundimage.jpg').convert()
            pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])

        
            screen.blit(background, (0, 0))
            pygame.display.flip()
            font = pygame.font.SysFont("helvetica", 56)
            text = font.render("GAME OVER", 1, (1, 1, 1))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos) 
    
            screen.blit(background, (0, 0))
            pygame.display.flip()
            background.fill((255,255,255))
            pygame.time.wait(300)

            
            font = pygame.font.SysFont("helvetica", 56)
            text = font.render("Score :", 1, (1, 1, 1))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx - 100
            background.blit(text, textpos)
            font = pygame.font.SysFont("helvetica", 56)
            text2 = font.render(score, 1, (1, 1, 1))
            textpos2 = text.get_rect()
            textpos2.centerx = background.get_rect().centerx +100
            background.blit(text2, textpos2)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            background.fill((255,255,255))
            
def gameLoop():
                background = pygame.Surface(screen.get_size())
                background = pygame.image.load('maingamebackgroundimage.jpg').convert()
                pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])

        
                screen.blit(background, (0, 0))
                pygame.display.flip()
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
                cat_y = 160
                gameOver = False
                difficulty = 5
                while not gameEnd:

                    while gameOver == True:
                        background = pygame.Surface(screen.get_size())
                        background = pygame.image.load('maingamebackgroundimage.jpg').convert()
                        pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])
                        screen.blit(background, (0, 0))
                        font = pygame.font.SysFont("helvetica", 56)
                        text = font.render("GAME OVER", 1, (1, 1, 1))
                        textpos = text.get_rect()
                        textpos.centerx = background.get_rect().centerx
                        background.blit(text, textpos)
                        font = pygame.font.SysFont("helvetica", 36)
                        text2 = font.render("Press C to continue.", 1, (1, 1, 1))
                        textpos2 = text.get_rect()
                        textpos2.centery = background.get_rect().centery + 55
                        textpos2.centerx = background.get_rect().centerx
                        background.blit(text2, textpos2)
                        font = pygame.font.SysFont("helvetica", 36)
                        text3 = font.render("Press ESC to quit.", 1, (1, 1, 1))
                        textpos3 = text.get_rect()
                        textpos3.centery = background.get_rect().centery +25
                        textpos3.centerx = background.get_rect().centerx
                        background.blit(text3, textpos3)
                        font = pygame.font.SysFont("helvetica", 36)
                        text4 = font.render("Press M to return to the main menu.", 1, (1, 1, 1))
                        textpos4 = text.get_rect()
                        textpos4.centery = background.get_rect().centery -5
                        textpos4.centerx = background.get_rect().centerx
                        background.blit(text4, textpos4)
                        screen.blit(background, (0, 0))
                        pygame.display.flip()
                        background.fill((255,255,255))
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    gameLoop()
                            if (pygame.key.get_pressed()[pygame.K_ESCAPE] != 0):
                                pygame.quit()
                                sys.exit()
                            if (pygame.key.get_pressed()[pygame.K_m] != 0):
                                main()

                    #While the game is running, allow the user to move the main character
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameEnd = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                cat_y += 40
                            if event.key == pygame.K_UP:
                                cat_y -= 40
        
                        if cat_y >= 420:
                            cat_y = 420
                        elif cat_y <= 0:
                            cat_y = 0
                            #gameOver = True


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

                    background = pygame.Surface(screen.get_size())
                    background = pygame.image.load('maingamebackgroundimage.jpg').convert()
                    pygame.display.set_mode([pygame.Surface.get_width(pygame.image.load('backgroundimage.jpg').convert()),pygame.Surface.get_height(pygame.image.load('backgroundimage.jpg').convert())])
                    screen.blit(background, (0, 0))
                    #gameDisplay.fill(white)
                    gameDisplay.blit(myImage,(cat_x, cat_y))
                    

                    #Call the enemy functions to draw the enemies
                    enemy1(enemy1_x,enemy1_y,block_size)
                    enemy2(enemy2_x,enemy2_y,block_size)
                    enemy3(enemy3_x,enemy3_y,block_size)
                    enemy4(enemy4_x,enemy4_y,block_size)
                    enemy5(enemy5_x,enemy5_y,block_size)


            

                    pygame.display.update()
                    
                    #If the main character and the enemies touch, the game will end 
                    if abs(cat_y - enemy1_y) <= 25 and abs(cat_x - enemy1_x) <= 15:
                        gameOver = True

                    elif abs(cat_y - enemy2_y) <= 25 and abs(cat_x - enemy2_x) <= 25:
                        gameOver = True
                
                    elif abs(cat_y - enemy3_y) <= 25 and abs(cat_x - enemy3_x) <= 25:
                        gameOver = True

                    elif abs(cat_y - enemy4_y) <= 25 and abs(cat_x - enemy4_x) <= 25:
                        gameOver = True

                    elif abs(cat_y - enemy5_y) <= 25 and abs(cat_x - enemy5_x) <= 25:
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

                    pygame.display.update()
                    clock.tick(30)
                    
                    
#Enemy/Character Functions
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
        speed = 10
    elif difficulty == 2:
        speed = 25
    elif difficulty == 3:
        speed = 40
    elif difficulty == 4:
        speed = 55
    else:
        speed = 70
    return speed
        
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250, 250])

def lives_to_screen(msg,color):
    lives_text = font.render(msg, True, color)
    gameDisplay.blit(lives_text, [250, 10])


def main():
    startup()
    
    # main game loop
    while True:
        for event in pygame.event.get():
            #StartScreen Input
            if (pygame.key.get_pressed()[pygame.K_RETURN] != 0):
                #Music Select Function
                music_select_screen()
                #Countdown Function
                countdown()
                #Game Start
                gameLoop()
                

                #End Game
                
            elif (pygame.key.get_pressed()[pygame.K_ESCAPE] != 0):
                pygame.quit()
                sys.exit()
            pygame.display.update()
        
            if event.type == QUIT:

                pygame.quit()
                sys.exit()
        pygame.display.update()

    
if __name__ == '__main__': main()

