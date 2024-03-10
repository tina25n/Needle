import pygame
from const import *

class StartMenu():
    def __init__(self):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 20
        self.x = (width / 2) - (self.rectWidth / 2)

        #start button
        self.textStart = font.render('Start', True, white, red)
        self.textStartRect = self.textStart.get_rect()
        self.textStartRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - 10)
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50
        self.playButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        #quit
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
        return self.playButtonRect.collidepoint(pos)
        
    def checkClickEndGame(self, pos):
        return self.quitButtonRect.collidepoint(pos)


    def update(self):
        self.drawPlayButton()
        self.drawQuitButton()


class SettingsMenu:
    def __init__(self):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 50
        self.x = (width / 2) - (self.rectWidth / 2)
        self.offset = 100

        # difficulty
        self.textDiff = fontLarge.render('Select Difficulty:', True, orange, white)
        self.textDiffRect = self.textDiff.get_rect()
        self.textDiffRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 30)

        #simple button
        self.textStart = font.render('Simple', True, white, red)
        self.textStartRect = self.textStart.get_rect()
        self.textStartRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - self.offset)
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50 - self.offset
        self.simpleButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        #medium button
        self.textMed = font.render('Medium', True, white, red)
        self.textMedRect = self.textMed.get_rect()
        self.textMedRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - self.offset + (self.rectHeight + 10))
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50 - self.offset + (self.rectHeight + 10)
        self.medButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        #difficult button
        self.textHard = font.render('Difficult', True, white, red)
        self.textHardRect = self.textHard.get_rect()
        self.textHardRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - self.offset + ((self.rectHeight + 10) * 2))
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50 - self.offset + ((self.rectHeight + 10)*2)
        self.hardButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)


    def drawButtons(self):
        pygame.draw.rect(screen, red, self.simpleButtonRect,  0, 3)
        screen.blit(self.textStart, self.textStartRect)
        pygame.draw.rect(screen, red, self.medButtonRect,  0, 3)
        screen.blit(self.textMed, self.textMedRect)
        pygame.draw.rect(screen, red, self.hardButtonRect,  0, 3)
        screen.blit(self.textHard, self.textHardRect)

    def checkClickSimple(self, pos):
        return self.simpleButtonRect.collidepoint(pos)
    
    def checkClickMed(self, pos):
        return self.medButtonRect.collidepoint(pos)

    def checkClickHard(self, pos):
        return self.hardButtonRect.collidepoint(pos)

    def update(self):
        screen.blit(self.textDiff, self.textDiffRect)
        self.drawButtons()


class PackageMenu:
    def __init__(self):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 50
        self.x = (width / 2) - (self.rectWidth / 2)
        self.offset = 100

        # difficulty
        self.textDiff = fontLarge.render('Select Package:', True, orange, white)
        self.textDiffRect = self.textDiff.get_rect()
        self.textDiffRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 30)

        # default
        self.textStart = font.render('Default', True, white, red)
        self.textStartRect = self.textStart.get_rect()
        self.textStartRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - self.offset)
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50 - self.offset
        self.simpleButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        # package 1
        self.textMed = font.render('Queer Coded', True, white, red)
        self.textMedRect = self.textMed.get_rect()
        self.textMedRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - self.offset + (self.rectHeight + 10))
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50 - self.offset + (self.rectHeight + 10)
        self.medButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

        # package 2
        self.textHard = font.render('Girl Boss', True, white, red)
        self.textHardRect = self.textHard.get_rect()
        self.textHardRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - self.offset + ((self.rectHeight + 10) * 2))
        self.yPlay = ((height / 5) * 3) - (self.rectHeight / 2) - 50 - self.offset + ((self.rectHeight + 10)*2)
        self.hardButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)


    def drawButtons(self):
        pygame.draw.rect(screen, red, self.simpleButtonRect,  0, 3)
        screen.blit(self.textStart, self.textStartRect)
        pygame.draw.rect(screen, red, self.medButtonRect,  0, 3)
        screen.blit(self.textMed, self.textMedRect)
        pygame.draw.rect(screen, red, self.hardButtonRect,  0, 3)
        screen.blit(self.textHard, self.textHardRect)

    def checkClickPackage1(self, pos):
        return self.simpleButtonRect.collidepoint(pos)
    
    def checkClickPackage2(self, pos):
        return self.medButtonRect.collidepoint(pos)
    
    def checkClickPackage3(self, pos):
        return self.hardButtonRect.collidepoint(pos)

    def update(self):
        screen.blit(self.textDiff, self.textDiffRect)
        self.drawButtons()