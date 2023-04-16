from entity import *


class Powerup(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed, shootSpeed, health):
        super().__init__(x, y, width, height, tileset, screen, speed, shootSpeed, health)

        powerups.append(self)

        self.collider = [width / 2.5, height / 2.5]
