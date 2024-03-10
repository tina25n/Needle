import pygame
from const import *

class StartMenu():
    def __init__(self):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 20
        self.x = (width / 2) - (self.rectWidth / 2)

        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50
        self.playButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        self.yQuit = ((height / 5) * 4) - (self.rectHeight / 2) - 73
        self.quitButtonRect = pygame.Rect(self.x, self.yQuit, self.rectWidth, self.rectHeight)

    def drawPlayButton(self):
        pygame.draw.rect(screen, red, self.playButtonRect,  0, 3)
        pygame.draw.rect(screen, red, self.quitButtonRect,  0, 3)

    def checkClickSettings(self, pos):
        if self.playButtonRect.collidepoint(pos):
            return True
        
    def checkClickEndGame(self, pos):
        if self.quitButtonRect.collidepoint(pos):
            return True


    def update(self):
        self.drawPlayButton()
        
