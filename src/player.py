from entity import *
import math


# PLAYER STATS
SHOOTSPEED = 20

class Player(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed, cursor):
        super().__init__(x, y, width, height, tileset, screen, speed, SHOOTSPEED)
        self.velocity = [0, 0]
        self.cursor = cursor

    def getInput(self):
        self.velocity = [0, 0]  

        keys = pygame.key.get_pressed()
        mouseKeys = pygame.mouse.get_pressed(num_buttons=3)

        if keys[pygame.K_a]:
            self.velocity[0] = -self.speed
        
        if keys[pygame.K_d]:
            self.velocity[0] = self.speed
        
        if keys[pygame.K_w]:
            self.velocity[1] = -self.speed
        
        if keys[pygame.K_s]:
            self.velocity[1] = self.speed

        if mouseKeys[0]:
            self.shoot(self.cursor)


    def update(self):
        self.getInput()
        super().update()
    