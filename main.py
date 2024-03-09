import pygame
from const import *
from enum import Enum
from drawing import StartMenu

# screen
pygame.display.set_caption('Sixth Sense')

# drawing classes

startMenu = StartMenu()


# system
running = True
cur_state = "start"

# game loop 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    screen.fill(white)

    if (cur_state == "start"):
        startMenu.draw()

    pygame.display.flip()
