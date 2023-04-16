import pygame, sys
from pygame.locals import *
pygame.init()

sys.path.append("../Cookout")

from Assests.colors import * # Gets colors
from player import *


# creating the window
displayHeight = 1280
displayWidth = 720
backgroundColor = GRASS

# UNCOMMENT WHEN HAVE BACKGROUND SCREEN
# background = pygame.transform.scale(pygame.image.load("IMAGE GOES HERE"), (displayHeight, displayWidth))

screen = pygame.display.set_mode((displayHeight, displayWidth))
pygame.display.set_caption("Cookout")

# used to close the window or keep game running
running = True

# internal clock for FPS speed
clock = pygame.time.Clock() 


cursor = Object(0, 0, 50, 50, pygame.image.load('Assests/img/cursor.png'), screen)
player = Player(displayHeight / 2, displayWidth / 2, 75, 75, "Assests/img/CharacterSheet.png", screen , 5, cursor)


pygame.mouse.set_visible = False
while running:
    #sets the background to backgroundColor
    screen.fill(backgroundColor)

    ## UNCOMMENT WHEN HAVE BACKGROUND
    # screen.blit(background)


    # getting mouse position
    mousePos = pygame.mouse.get_pos()
    cursor.x = mousePos[0] - cursor.width / 2
    cursor.y = mousePos[1] - cursor.height / 2

    for event in pygame.event.get():
        #quit the program if x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    for obj in objects:
        obj.update()


    #allows game to run at 60FPS
    clock.tick(60)
    pygame.display.update()