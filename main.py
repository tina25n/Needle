import pygame
from const import *
from enum import Enum
from drawing import StartMenu

# screen
pygame.display.set_caption('Sixth Sense')

# drawing classes
startMenu = StartMenu()

#background
bg_img = pygame.image.load("Sixth Sense.png")
bg_img_rect = bg_img.get_rect()


# system
running = True
cur_state = "start"

# game loop 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (startMenu.checkClickSettings(pos)):
                cur_state = "running"
            if (startMenu.checkClickEndGame(pos)):
                running = False
                pygame.display.quit()
                pygame.quit()
            

    screen.fill(white)
    screen.blit(bg_img, bg_img_rect)

    if (cur_state == "start"):
        startMenu.update()

    if (cur_state == "settings"):
        pass
    

    pygame.display.flip()
