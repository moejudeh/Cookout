import pygame
from pygame.locals import *
from settings import *

pygame.init()
objects = []

class Object:
    def __init__(self, x, y, width, height, image, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.screen = screen
        self.velocity = [0, 0]
        
        self.collider = [width / 2.5, height]
        
        objects.append(self)


    def getCenter(self):
        return self.x +  self.width / 2, self.y + self.height / 2

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.draw()
    
    def hit(self, entity):
        selfX, selfY = self.getCenter()
        selfW = self.collider[0] / 2
        selfH = self.collider[1] / 2

        entityX, entityY = entity.getCenter()
        entityW = entity.collider[0] / 2
        entityH = entity.collider[1] / 2

        if selfX + selfW > entityX - entityW and selfX - selfW < entityX + entityW:
            if selfY + selfH > entityY - entityH and selfY - selfH < entityY + entityH:
                print("collision detected")
                return  True
        return False
    