import pygame
from const import *

class questionScreen:
    def __init__(self, qs, q_count, cur_player):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 50
        self.x = (width / 2) - (self.rectWidth / 2)
        self.y = ((height / 12) * 11) 
        self.offset = 100
        self.cur_player = cur_player

        # Question display
        self.q1 = fontLarge.render(qs["Q"+ str(q_count)]["question"], True, orange, white)
        self.q1Rect = self.q1.get_rect()
        self.q1Rect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 130)

        #player display
        self.player = font.render("Player " + str(self.cur_player), True, red, white)
        self.playerRect = self.player.get_rect()
        self.playerRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 190)

        #start button
        self.textNext = font.render('Next', True, white, red)
        self.textNextRect = self.textNext.get_rect()
        self.textNextRect.center = (width / 2, self.y - (self.rectHeight / 2) + 27)
        self.yPlay = (self.y) - (self.rectHeight / 2)
        self.nextButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

    def checkClickNext(self, poss):
        return self.nextButtonRect.collidepoint(poss)
    
    def drawNextButton(self):
        pygame.draw.rect(screen, red, self.nextButtonRect,  0, 3)
        screen.blit(self.textNext, self.textNextRect)

    def update(self):
        screen.blit(self.q1, self.q1Rect)
        screen.blit(self.player, self.playerRect)
        self.drawNextButton()

class answerButton:
    def __init__(self, y, text, player):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 50
        self.x = (width / 2) - (self.rectWidth / 2)
        self.offset = 200
        self.y = y
        self.ansText = text
        self.player = player
        #((height / 5) * 3) - (self.rectHeight / 2) - 50

        # default
        self.textAns = font.render(self.ansText, True, white, red)
        self.textAnsRect = self.textAns.get_rect()
        self.textAnsRect.center = (width / 2, self.y - ((height / 7) / 4) - self.offset)
        self.yAns = self.y - 50 - self.offset
        self.simpleButtonRect = pygame.Rect(self.x, self.yAns, self.rectWidth, self.rectHeight)

    def drawButtons(self):
        pygame.draw.rect(screen, red, self.simpleButtonRect,  0, 3)
        screen.blit(self.textAns, self.textAnsRect)

    def checkClickAns(self, pos, player):
        if (self.simpleButtonRect.collidepoint(pos)):
            if (player == 1):
                return 1
            if (player == 2):
                return 2
        else:
            return 0