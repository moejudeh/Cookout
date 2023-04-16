import pygame
from pygame.locals import *
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

        objects.append(self)


    def getCenter(self):
        return self.x +  self.width / 2, self.y + self.height / 2

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.image, (self.width, self.height)), (self.x, self.y))

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.draw()
    