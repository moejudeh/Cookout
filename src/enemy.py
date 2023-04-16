from entity import *
from powerup import *
import random

class Carrot(Entity):
    def __init__(self, width, height, tileset, screen, speed, shootSpeed, player):
        xValue = random.randrange(X_BOUND[0] + 50, X_BOUND[1] - 50)
        yValue = random.randrange(Y_BOUND[0] + 50, Y_BOUND[1] - 75)
        super().__init__(xValue, yValue, width, height, tileset, screen, speed, shootSpeed, CARROT_HEALTH)

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


    def dropHeart(self, outcome, chance):
        if outcome > chance:
            return

        x,y = self.getCenter()
        Powerup(x, y, HEART_SIZE, HEART_SIZE, HEART_SHEET, self.screen, 0, 0, 0)


    def entityKilled(self):
        # chance to drop heart
        outcome = random.random()
        self.dropHeart(outcome, CARROT_HEART_DROP)

        enemies.remove(self)
        self.player.score += 1
        super().entityKilled()
        

def enemySpawner(screen, player):
    while True:
        for i in range(60):
            yield
        Carrot(CARROT_SIZE, CARROT_SIZE, CARROT_SHEET, screen, CARROT_SPEED, CARROT_SHOOT_SPEED, player)