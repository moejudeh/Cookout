import pygame
import sys
from pygame.locals import *
pygame.init()

sys.path.append("../Cookout")

from Assests.colors import * # Gets colors
from player import *




# creating the window
displayHeight = 1280
displayWidth = 720
backgroundColor = WHITE #white screen

# UNCOMMENT WHEN HAVE BACKGROUND SCREEN
# background = pygame.transform.scale(pygame.image.load("IMAGE GOES HERE"), (displayHeight, displayWidth))

screen = pygame.display.set_mode((displayHeight, displayWidth))
pygame.display.set_caption("Cookout")

# used to close the window or keep game running
running = True

# internal clock for FPS speed
clock = pygame.time.Clock() 

# Game Display
player = Player(displayHeight / 2, displayWidth / 2, 75, 75, "Assests/img/CharacterSheet.png", screen , 5)

while running:
    #sets the background to backgroundColor
    screen.fill(backgroundColor)

    ## UNCOMMENT WHEN HAVE BACKGROUND
    # screen.blit(background)


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