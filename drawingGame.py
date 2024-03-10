import pygame
from const import *
from logic import sumSocre

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

class scoreScreen:
    def __init__(self, scores):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 50
        self.x = (width / 2) - (self.rectWidth / 2)
        self.y = ((height / 12) * 11) 
        self.offset = 100

        score=sumSocre(scores)

        if(score <= 100 and score >=80):
            title="Are you twins?"
            subtitle = "You both definitely have a sixth-sense!"
        elif(score <80 and score >=50):
            title = "Maybe you do, maybe you don't?"
            subtitle = "You have some kind of connection!"
        else:
            title = "Is the sixth-sense in the room with us?"
            subtitle = "Time to learn more about each other."
        # Title display
        self.titletxt = fontLarge.render(title, True, orange, white)
        self.titletxtRect = self.titletxt.get_rect()
        self.titletxtRect.y = self.y + 50
        self.titletxtRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 130)

        # subTitle display
        self.subtitletxt = fontLarge.render(subtitle, True, orange, white)
        self.subtitletxtRect = self.subtitletxt.get_rect()
        self.subtitletxtRect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 130)

        # Score display
        self.scoretxt = fontLarge.render("Score: " + str(score), True, orange, white)
        self.scoretxtRect = self.scoretxt.get_rect()
        self.scoretxtRect.center = (width / 2, ((height) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 130)

        self.textpa = font.render('Play Again', True, white, red)
        self.textpaRect = self.textpa.get_rect()
        self.textpaRect.center = (width / 2, self.y - (self.rectHeight / 2) + 27)
        self.yPlay = (self.y) - (self.rectHeight / 2)
        self.paButtonRect = pygame.Rect(self.x, self.yPlay, self.rectWidth, self.rectHeight)

    def drawPAButton(self):
        pygame.draw.rect(screen, red, self.paButtonRect,  0, 3)
        screen.blit(self.textpa, self.textpaRect)

    def update(self):
        self.drawPAButton()
        screen.blit(self.scoretxt, self.scoretxtRect)
        screen.blit(self.titletxt, self.titletxtRect)
        screen.blit(self.subtitletxt, self.subtitletxtRect)
        