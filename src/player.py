from entity import *

class Player(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed):
        super().__init__(x, y, width, height, tileset, screen, speed)