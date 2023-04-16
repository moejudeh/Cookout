from entity import *
from Assests.colors import * # Gets colors

# PLAYER STATS
hearts = []
scoreFont = pygame.font.Font("Assests/font.ttf", 50)

class Player(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed, cursor):
        super().__init__(x, y, width, height, tileset, screen, speed, PLAYER_SHOOT_SPEED, PLAYER_HEALTH)
        self.velocity = [0, 0]
        self.cursor = cursor
        self.score = 0

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
        self.updateUI()

        super().update()
    
    def updateUI(self):
        img = pygame.image.load("Assests/img/heart.png")
        
        if len(hearts) == 0:
            newHeart = Object(10, 10, 100, 100, img, self.screen)
            hearts.append(newHeart)
            
        elif self.health > len(hearts):
            newHeart = Object(hearts[len(hearts) - 1].x + 75, 10, 100, 100, img, self.screen)
            hearts.append(newHeart)

        scoreText = scoreFont.render(f'Score: { self.score }', True, BLACK)
        self.screen.blit(scoreText, (1270 - scoreText.get_width(), 50))

    def takeDamage(self):
        if self.health > 0:
            objects.remove(hearts.pop())
            self.score -= 1
            super().takeDamage()
 
    def heal(self):
        if(self.health == PLAYER_HEALTH):
            return
        
        else:
            self.health += 1