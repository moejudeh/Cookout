from entity import *

# PLAYER STATS
hearts = []

class Player(Entity):
    def __init__(self, x, y, width, height, tileset, screen, speed, cursor):
        super().__init__(x, y, width, height, tileset, screen, speed, PLAYER_SHOOT_SPEED, PLAYER_HEALTH)
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

    def takeDamage(self):
        objects.remove(hearts.pop())
        super().takeDamage()
 
    def heal(self):
        if(self.health == PLAYER_HEALTH):
            return
        
        else:
            self.health += 1