import pygame
import sys
from Assests.colors import * #Gets colors
from pygame.locals import *
pygame.init()

# creating the window
displayHeight = 1280
displayWidth = 720
backgroundColor = WHITE #white screen
screen = pygame.display.set_mode((displayHeight, displayWidth))
pygame.display.set_caption("Cookout")

# used to close the window or keep game running
running = True

# internal clock for FPS speed
clock = pygame.time.Clock()

#player Appearance
playerColor = RED


#player Movement
player_X = 0
player_Y = 0
playerInput = {"left": False, "right": False, "up": False, "down": False}
playerVelocity = [0, 0]
playerSpeed = 5


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



while running:
    #sets the background to backgroundColor
    screen.fill(backgroundColor)


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

    # moving player
    playerVelocity[0] = playerInput["right"] - playerInput["left"]
    playerVelocity[1] = playerInput["down"] - playerInput["up"] 
    player_X += playerVelocity[0] * playerSpeed
    player_Y += playerVelocity[1] * playerSpeed

    pygame.draw.circle(screen, playerColor, (player_X, player_Y), 25)


    #allows game to run at 60FPS
    clock.tick(60)
    pygame.display.update()