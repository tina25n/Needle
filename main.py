import pygame
from const import *
from enum import Enum
from drawing import StartMenu

pygame.init()

# screen
pygame.display.set_caption('Sixth Sense')

# drawing classes
startMenu = StartMenu()

#background
start_bg_img = pygame.image.load("Sixth Sense.png")
start_bg_img_rect = start_bg_img.get_rect()

bg_img = pygame.image.load("Questions.png")
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
                cur_state = "settings"
            if (startMenu.checkClickEndGame(pos)):
                running = False
                pygame.display.quit()
                pygame.quit()

    if (cur_state == "start"):
        screen.fill(white)
        screen.blit(start_bg_img, start_bg_img_rect)
        startMenu.update()

    if (cur_state == "settings"):
        screen.fill(white)
        screen.blit(bg_img, bg_img_rect)
    

    pygame.display.flip()
