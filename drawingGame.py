import pygame
from const import *

class questionScreen:
    def __init__(self, qs, q_count):
        self.rectWidth = width / 3 - 20
        self.rectHeight = height / 7 - 50
        self.x = (width / 2) - (self.rectWidth / 2)
        self.offset = 100

        # Question display
        self.q1 = fontLarge.render(qs["Q"+ str(q_count)]["question"], True, orange, white)
        self.q1Rect = self.q1.get_rect()
        self.q1Rect.center = (width / 2, ((height / 5) * 3) - (self.rectHeight / 2) - ((height / 7) / 4) - 50 - self.offset - 30)

    def update(self):
        screen.blit(self.q1, self.q1Rect) 