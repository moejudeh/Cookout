import pygame, sys
from pygame.locals import *
pygame.init()
sys.path.append("../Cookout")

from Assests.colors import * # Gets colors
from player import * # Gets player functions
from enemy import * # Gets Enemies functions
from settings import * # Gets game settings
from button import * # Button creation

# creating the window
displayHeight = 1280
displayWidth = 720
screen = pygame.display.set_mode((displayHeight, displayWidth))
pygame.display.set_caption("Cookout")

# Loads Background Image for game
background = pygame.transform.scale(pygame.image.load("Assests/img/background.png"), (displayHeight, displayWidth))

## PLAYER AND CURSOR
player = None
cursor = Object(0, 0, 50, 50, pygame.image.load('Assests/img/cursor.png'), screen)
gameSpawner = None

# internal clock for FPS speed
clock = pygame.time.Clock() 

# Disables Mouse
pygame.mouse.set_visible = False

## CONTROLS WHICH SCREEN IS RUNNING
startScreenRunning = True
playScreenRunning = False
EndScreenRunning = False

# RUNS START SCREEN
def startScreen():

    screen.fill(GRASS)

    PLAY_BUTTON = Button(pygame.image.load("Assests/img/buttonBackground.png"), (640, 300), "PLAY", get_font(75), "#d7fcd4", "White")
    QUIT_BUTTON = Button(pygame.image.load("Assests/img/buttonBackground.png"), (640, 500), "QUIT", get_font(75), "#d7fcd4", "White")

    for button in Buttons:
        button.changeColor((cursor.x, cursor.y))
        button.update(screen)


# RUNS GAMEww
def playGame():
    global player, gameSpawner, cursor, startScreenRunning, playScreenRunning
    
    screen.blit(background, (0,0))

    if player is None:
        player = Player(displayHeight / 2, displayWidth / 2, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SHEET, screen , PLAYER_SPEED, cursor)
        gameSpawner = enemySpawner(screen , player)


    next(gameSpawner)

    ## Updates everything
    for obj in objects:
        obj.update()

    # Make sure bullet stays on map
    for b in bullets:
        if b.x > 1280 or b.x < 0 or b.y > 720 or b.y < 0:
            bullets.remove(b)
            objects.remove(b)

    if player is not None:    
        checkCollisions(player)

    # CHECKS IF PLAYER IS DEAD
    if player.health == 0:
        # Gets rid of Player and spawner

        #Deletes Remaining Entities
        objects.clear()
        enemies.clear()
        powerups.clear()

        playScreenRunning = False
        startScreenRunning = True
    
        player = None
        gameSpawner = None
        cursor = Object(0, 0, 50, 50, pygame.image.load('Assests/img/cursor.png'), screen)




while True:

    # getting mouse position
    mousePos = pygame.mouse.get_pos()
    cursor.x = mousePos[0] - cursor.width / 2
    cursor.y = mousePos[1] - cursor.height / 2

    for event in pygame.event.get():
        #quit the program if x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Buttons[0].checkForInput((cursor.x, cursor.y)):
                startScreenRunning = False
                playScreenRunning = True
                
            if Buttons[1].checkForInput((cursor.x, cursor.y)):
                pygame.quit()
                sys.exit()
    
    
    
    # ## Running Start Screen
    if startScreenRunning:
        startScreen()

    elif playScreenRunning:
        playGame()


    #     if event.type == pygame.KEYDOWN:
    #         # Kills all enemies
    #         if(event.key == pygame.K_m):
    #             for e in enemies:
    #                 e.entityKilled()

    #         # Spawns Carrots
    #         if(event.key == pygame.K_n):
    #             Carrot(CARROT_SIZE, CARROT_SIZE, CARROT_SHEET, screen, CARROT_SPEED, CARROT_SHOOT_SPEED, player)

    #         # stationary Carrot
    #         if(event.key == pygame.K_x):
    #             Carrot(CARROT_SIZE, CARROT_SIZE, CARROT_SHEET, screen, 0, CARROT_SHOOT_SPEED, player)


    # #allows game to run at 60FPS
    clock.tick(60)
    pygame.display.update()