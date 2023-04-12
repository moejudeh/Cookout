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

#player Appearance
playerColor = RED

#player Movement
playerInput = {"left": False, "right": False, "up": False, "down": False}


# checkInput
# checks player for input for WASD
def checkInput(key, value):
    if key == pygame.K_a:
        playerInput["left"] = value

    if key == pygame.K_d:
        playerInput["right"] = value

    if key == pygame.K_w:
        playerInput["up"] = value

    if key == pygame.K_s:
        playerInput["down"] = value



# Game Display
# testObject = Object(400, 400, 50, 50, pygame.image.load("Assests/img/heart.png"), screen)
# testEntity = Entity(400, 400, 50, 50, "Assests/img/player-Sheet.png", screen , 5)
player = Player(displayHeight / 2, displayWidth / 2, 75, 75, "Assests/img/player-Sheet.png", screen , 5)

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
        # getting player input
        elif event.type == pygame.KEYDOWN:
            checkInput(event.key, True)
        elif event.type == pygame.KEYUP:
            checkInput(event.key, False)

    # changing velocity of player
    player.velocity[0] = playerInput["right"] - playerInput["left"]
    player.velocity[1] = playerInput["down"] - playerInput["up"] 

    for obj in objects:
        obj.update()

    #allows game to run at 60FPS
    clock.tick(60)
    pygame.display.update()