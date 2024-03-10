import pygame

pygame.font.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('freesansbold.ttf', 32)

# IBM COLOR BLIND SAFE PALETTE
red = (220, 38, 127)
purple = (120, 94, 240)
blue = (100, 143, 255)
orange = (254, 97, 0)
yellow = (255, 176, 0)
white = (255,255,255)