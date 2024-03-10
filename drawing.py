import pygame
from const import *

class StartMenu():
    def __init__(self):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 20
        self.x = (width / 2) - (self.rectWidth / 2)

        self.textStart = font.render('Start', True, white, red)
        self.textStartRect = self.textStart.get_rect()
        self.textStartRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - 10)
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50
        self.playButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        self.textQuit = font.render('Quit', True, white, red)
        self.textQuitRect = self.textQuit.get_rect()
        self.textQuitRect.center = (width / 2, ((height / 5) * 4) - (self.rectHeight / 2) - 35)
        self.yQuit = ((height / 5) * 4) - (self.rectHeight / 2) - 73
        self.quitButtonRect = pygame.Rect(self.x, self.yQuit, self.rectWidth, self.rectHeight)

    def drawPlayButton(self):
        pygame.draw.rect(screen, red, self.playButtonRect,  0, 3)
        screen.blit(self.textStart, self.textStartRect)

    def drawQuitButton(self):
        pygame.draw.rect(screen, red, self.quitButtonRect,  0, 3)
        screen.blit(self.textQuit, self.textQuitRect)

    def checkClickSettings(self, pos):
        if self.playButtonRect.collidepoint(pos):
            return True
        
    def checkClickEndGame(self, pos):
        if self.quitButtonRect.collidepoint(pos):
            return True


    def update(self):
        self.drawPlayButton()
        self.drawQuitButton()


class SettingsMenu:
    def __init__(self):

        self.packText = font.render('Choose an Additional Package', True, orange, white)
        self.packtextRect = self.packText.get_rect()
        self.packtextRect.center = (width / 2, ((height / 5) * 4) - (height / 2) - 35)
        self.ypacktext = ((height / 5) * 4) - (height / 2) - 73

    def drawText(self):
        screen.blit(self.packText, self.packtextRect)

    def update(self):
        self.drawText()