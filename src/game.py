import pygame, sys
from pygame.locals import *
pygame.init()
sys.path.append("../Cookout")

from Assests.colors import * # Gets colors
from player import * # Gets player functions
from enemy import * # Gets Enemies functions
from settings import * # Gets game settings

# creating the window
displayHeight = 1280
displayWidth = 720

# CHECKS FOR COLLISIONS
def checkCollisions():
    for e in enemies:
        for b in bullets:
            if b.hit(e):
                e.velocity = b.velocity
                # DELETE BULLET IF HIT SOMETHING
                bullets.remove(b)
                objects.remove(b)
                e.takeDamage()
        
        if e.hit(player):
            e.entityKilled()
            player.takeDamage()


# UNCOMMENT WHEN HAVE BACKGROUND SCREEN
background = pygame.transform.scale(pygame.image.load("Assests/img/background.png"), (displayHeight, displayWidth))

screen = pygame.display.set_mode((displayHeight, displayWidth))
pygame.display.set_caption("Cookout")

# used to close the window or keep game running
running = True

# internal clock for FPS speed
clock = pygame.time.Clock() 


cursor = Object(0, 0, 50, 50, pygame.image.load('Assests/img/cursor.png'), screen)
player = Player(displayHeight / 2, displayWidth / 2, PLAYER_SIZE, PLAYER_SIZE, PLAYER_SHEET, screen , PLAYER_SPEED, cursor)

pygame.mouse.set_visible = False
while running:

    ## Setting Background
    screen.blit(background, (0,0))


    # getting mouse position
    mousePos = pygame.mouse.get_pos()
    cursor.x = mousePos[0] - cursor.width / 2
    cursor.y = mousePos[1] - cursor.height / 2

    for event in pygame.event.get():
        #quit the program if x is pressed
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Kills all enemies
            if(event.key == pygame.K_m):
                for e in enemies:
                    objects.remove(e)
                    enemies.remove(e)

            # Spawns Carrots
            if(event.key == pygame.K_n):
                Carrot(100, 100, CARROT_SIZE, CARROT_SIZE, CARROT_SHEET, screen, CARROT_SPEED, CARROT_SHOOT_SPEED, player)


    for obj in objects:
        obj.update()
        
    for e in enemies:
        if objects.count(e) == 0:
            enemies.remove(e)

    # Make sure bullet stays on map
    for b in bullets:
        if b.x > 1280 or b.x < 0 or b.y > 720 or b.y < 0:
            bullets.remove(b)
            objects.remove(b)

    checkCollisions()
    #allows game to run at 60FPS
    clock.tick(60)
    pygame.display.update()

    # CHECKS IF PLAYER IS DEAD
    if player.health == 0:
        running = False