import pygame, sys
from pygame.locals import *
pygame.init()
sys.path.append("../Cookout")

from Assests.colors import *    # Gets colors
from player import *    # Gets player functions
from enemy import *    # Gets Enemies functions
from settings import *    # Gets game settings
from button import *    # Button creation

# creating the window
screen = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
pygame.display.set_caption("Cookout")
pygame.display.set_icon(pygame.image.load("Assests/icon/gameIcon.ico"))

# Loads Background Image for game
background = pygame.transform.scale(pygame.image.load("Assests/img/background.png"), (DISPLAYWIDTH, DISPLAYHEIGHT))

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

#startScreen Buttons
PLAY_BUTTON = None
QUIT_BUTTON = None
titleButton = None

# RUNS START SCREEN
def startScreen():
    global PLAY_BUTTON, QUIT_BUTTON
    screen.fill(BACKGROUND)

    gameName = scoreFont.render(f'CookOut', True, WHITE)
    screen.blit(gameName, (DISPLAYWIDTH / 2 - gameName.get_width() / 2, DISPLAYHEIGHT / 2 - 250))


    if PLAY_BUTTON is None and QUIT_BUTTON is None:
        PLAY_BUTTON = Button(pygame.image.load("Assests/img/buttonBackground.png"), (640, 300), "PLAY", get_font(75), "#d7fcd4", "White")
        QUIT_BUTTON = Button(pygame.image.load("Assests/img/buttonBackground.png"), (640, 500), "QUIT", get_font(75), "#d7fcd4", "White")


    for button in Buttons:
        button.changeColor((cursor.x, cursor.y))
        button.update(screen)

# RUNS GAME
def playGame():
    global player, gameSpawner, cursor, EndScreenRunning, playScreenRunning, SCORE_GOT
    
    screen.blit(background, (0,0))

    if player is None:
        player = Player(DISPLAYWIDTH / 2, DISPLAYHEIGHT / 2, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SHEET, screen , PLAYER_SPEED, cursor)
        gameSpawner = enemySpawner(screen , player)


    next(gameSpawner)

    objects.remove(cursor)
    objects.append(cursor)

    ## Updates everything
    for obj in objects:
        obj.update()

    # Make sure bullet stays on map
    for b in bullets:
        if b.x > 1280 or b.x < 0 or b.y > 720 or b.y < 0:
            bullets.remove(b)
            objects.remove(b)


    # CHECKS IF PLAYER IS DEAD
    if player.health == 0:
        # Gets rid of Player and spawner

        #Deletes Remaining Entities
        objects.clear()
        enemies.clear()
        powerups.clear()

        playScreenRunning = False
        EndScreenRunning = True
        SCORE_GOT = player.score

        player = None
        gameSpawner = None
        cursor = Object(0, 0, 50, 50, pygame.image.load('Assests/img/cursor.png'), screen)


    if player is not None:
        checkCollisions(player)

# RUNS RESULT SCREEN
def resultScreen():
    global SCORE_GOT, HIGHSCORE, titleButton
    screen.fill(BACKGROUND)

    scoreText = scoreFont.render(f'Score: { SCORE_GOT }', True, BLACK)
    screen.blit(scoreText, (DISPLAYWIDTH / 2 - scoreText.get_width() / 2, DISPLAYHEIGHT / 2 - 200))

    if SCORE_GOT > HIGHSCORE:
        HIGHSCORE = SCORE_GOT

    scoreText = scoreFont.render(f'HighScore: { HIGHSCORE }', True, BLACK)
    screen.blit(scoreText, (DISPLAYWIDTH / 2 - scoreText.get_width() / 2, DISPLAYHEIGHT / 2 - 75))

    if titleButton is None:
        titleButton = Button(pygame.image.load("Assests/img/buttonBackground.png"), (640, DISPLAYHEIGHT / 2  + 100), "Title Screen", get_font(30), "#d7fcd4", "White")
    
    titleButton.changeColor((cursor.x, cursor.y))
    titleButton.update(screen)


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

        # USED FOR BUTTON INPUTS ON SCREENS
        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(Buttons) == 2:
                if Buttons[0].checkForInput((cursor.x, cursor.y)):
                    startScreenRunning = False
                    playScreenRunning = True
                    Buttons.clear()
                    PLAY_BUTTON = None
                    QUIT_BUTTON = None
                    
                elif Buttons[1].checkForInput((cursor.x, cursor.y)):
                    pygame.quit()
                    sys.exit()

            if titleButton is not None:
                if titleButton.checkForInput((cursor.x, cursor.y)):
                    startScreenRunning = True
                    EndScreenRunning = False
                    Buttons.clear()
                    titleButton = None
    
    ## Running Start Screen
    if startScreenRunning:
        startScreen()
    elif playScreenRunning:
        playGame()
    elif EndScreenRunning:
        resultScreen()

    # #allows game to run at 60FPS
    clock.tick(60)
    pygame.display.update()