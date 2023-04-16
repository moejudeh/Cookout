from object import *
import math

#CONSTANTS
DOWN = 0
HORIZONTAL = 1
UP = 2
AnimationFrameRate = 10

bulletSpeed= 20
bullets = []


class Entity(Object):
    def __init__(self, x, y, width, height, tileset, screen, speed, shootSpeed):
        super().__init__(x, y, width, height, None, screen)
        self.speed = speed
        self.tileset = loadTileset(tileset, 16, 16)

        ## USED FOR ANIMATING WALKING
        self.direction = 0
        self.flipX = False
        self.frame = 0
        self.walkFrames = [0, 1, 0, 2]
        self.frameTimer = 0


        ## FOR SHOOTING COOLDOWN
        self.shootCD = shootSpeed
        self.shootTimer = 0

    ## USED FOR ANIMATION
    def changeDirection(self):
        if self.velocity[0] < 0:
            self.direction = HORIZONTAL
            self.flipX = True
        elif self.velocity[0] > 0:
            self.direction = HORIZONTAL
            self.flipX = False
        elif self.velocity[1] > 0:
            self.direction = DOWN
        elif self.velocity[1] < 0:
            self.direction = UP

    def draw(self):
        image = pygame.transform.scale(self.tileset[self.walkFrames[self.frame]][self.direction], (self.width, self.height))

        self.changeDirection()

        image = pygame.transform.flip(image, self.flipX, False)
        self.screen.blit(image, (self.x, self.y))

        ## IF ENTITY IS NOT MOVING SET DEFAULT SPRITE
        if self.velocity[0] == 0 and self.velocity[1] == 0:
            self.frame = 0
            return
        
        self.frameTimer += 1

        ## FRAME RATE OF ANIMATION
        if self.frameTimer < AnimationFrameRate:
            return
        self.frameTimer = 0

        ## CHANGE SPRITE FOR ANIMATION
        self.frame += 1
        if self.frame >= len(self.walkFrames):
            self.frame = 0


    def move(self):
        if self.velocity[0] != 0 and self.velocity[1] != 0:
            self.x += self.velocity[0] / math.sqrt(2)
            self.y += self.velocity[1] / math.sqrt(2)
        else:
            self.x += self.velocity[0]
            self.y += self.velocity[1]

    def update(self):
        self.move()

        self.shootTimer += 1

        self.draw()

    # Shooting
    def shoot(self, aimed):
        if(self.shootTimer < self.shootCD):
            return
        
        self.shootTimer = 0
        
        entityCenter = self.getCenter()
        bullet = Object(entityCenter[0], entityCenter[1], 30, 30, pygame.image.load('Assests/img/knife.png'), self.screen)

        aimedCenter = aimed.getCenter()

        xDistance = aimedCenter[0] - entityCenter[0]
        yDistance = aimedCenter[1] - entityCenter[1]

        angle = math.atan2(yDistance, xDistance)

        xVelocity = bulletSpeed * math.cos(angle)
        yVelocity = bulletSpeed * math.sin(angle)

        bullet.velocity = [xVelocity, yVelocity]

        bullets.append(bullet)




def loadTileset(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    imageWidth, imageHeight = image.get_size()
    tileset = []
    for tileX in range(0, imageWidth // width):
        line = []
        tileset.append(line)
        for tileY in range(0, imageHeight // height):
            rect = (tileX * width, tileY * height, width, height)
            line.append(image.subsurface(rect))
    return tileset