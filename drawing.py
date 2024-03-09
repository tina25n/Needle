import pygame
from const import *

class StartMenu():
    def __init__(self):
        pass

    def drawPlayButton(self):
        rectWidth = width / 3
        rectHeight = height / 7
        pygame.draw.rect(screen, red, pygame.Rect((width / 2) - rectWidth /2, ((height / 5) * 3) - rectHeight/2, rectWidth, rectHeight),  0, 3)

    def draw(self):
        self.drawPlayButton()
