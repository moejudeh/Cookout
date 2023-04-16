from entity import *

enemies = []

class Carrot(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed, shootSpeed, player):
        super().__init__(x, y, width, height, tileset, screen, speed, shootSpeed, CARROT_HEALTH)

        self.player = player
        self.velocity = [0, 0]

        enemies.append(self)

    def moveEnemy(self):
        enemyCenter = self.getCenter()


        playerCenter = self.player.getCenter()

        xDistance = playerCenter[0] - enemyCenter[0]
        yDistance = playerCenter[1] - enemyCenter[1]

        angle = math.atan2(yDistance, xDistance)

        xVelocity = self.speed * math.cos(angle)
        yVelocity = self.speed * math.sin(angle)

        self.velocity = [xVelocity, yVelocity]


    def update(self):
        super().update()
        self.moveEnemy()

        