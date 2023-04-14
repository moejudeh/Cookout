from entity import *
import math

class Player(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed):
        super().__init__(x, y, width, height, tileset, screen, speed)
        self.velocity = [0, 0]

    def getInput(self):
        self.velocity = [0, 0]

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity[0] = -self.speed
        
        if keys[pygame.K_d]:
            self.velocity[0] = self.speed
        
        if keys[pygame.K_w]:
            self.velocity[1] = -self.speed
        
        if keys[pygame.K_s]:
            self.velocity[1] = self.speed


    def movePlayer(self):

        if self.velocity[0] != 0 and self.velocity[1] != 0:
            self.x += self.velocity[0] / math.sqrt(2)
            self.y += self.velocity[1] / math.sqrt(2)
        else:
            self.x += self.velocity[0]
            self.y += self.velocity[1]

    def update(self):
        self.getInput()
        self.movePlayer()

        self.draw()