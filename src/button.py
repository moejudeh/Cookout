import pygame
Buttons = []

class Button():
    def __init__(self, image, pos, textInput, font, baseColor, hoverColor):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.textInput = textInput
        self.font = font
        self.baseColor = baseColor
        self.hoverColor = hoverColor
        self.text = self.font.render(self.textInput, True, self.baseColor)

        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.textRect = self.text.get_rect(center = (self.x, self.y))

        Buttons.append(self)

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textInput, True, self.hoverColor)
        else:
            self.text = self.font.render(self.textInput, True, self.baseColor)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Assests/font.ttf", size)