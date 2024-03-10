import pygame
from const import *
from enum import Enum
from drawingStarting import StartMenu, SettingsMenu, PackageMenu
from drawingGame import questionScreen
from logic import questionsDict

pygame.init()

# screen
pygame.display.set_caption('Sixth Sense')
curr_rounds = 1
curr_player = 1

# drawing classes
startMenu = StartMenu()
settingsMenu = SettingsMenu()
packageMenu = PackageMenu()
qs = questionsDict()
#["Q1"]["question"]
gameScreen = questionScreen(qs.qsDict, curr_rounds, curr_player)

#background
start_bg_img = pygame.image.load("Sixth Sense.png")
start_bg_img_rect = start_bg_img.get_rect()

bg_img = pygame.image.load("Questions.png")
bg_img_rect = bg_img.get_rect()

# system
running = True
cur_state = "start"
clickedOnce = False

# game loop 
while running: 
    curr_rounds +=1
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clickedOnce = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #start
            if (cur_state == "start"):
                if (startMenu.checkClickSettings(pos) and (not clickedOnce)):
                    cur_state = "settings"
                    clickedOnce = True
                if (startMenu.checkClickEndGame(pos) and (not clickedOnce)):
                    running = False
                    pygame.display.quit()
                    pygame.quit()
            #settings
            if (cur_state == "settings"):
                if (settingsMenu.checkClickSimple and (not clickedOnce)):
                    cur_state = "packages"
                    clickedOnce = True
                if (settingsMenu.checkClickMed and (not clickedOnce)):
                    cur_state = "packages"
                    clickedOnce = True
                if (settingsMenu.checkClickHard and (not clickedOnce)):
                    cur_state = "packages"
                    clickedOnce = True
            # package
            if (cur_state == "packages"):
                if (packageMenu.checkClickPackage1 and (not clickedOnce)):
                    cur_state = "game"
                    clickedOnce = True      
                if (packageMenu.checkClickPackage2 and (not clickedOnce)):
                    cur_state = "game"
                    clickedOnce = True
                if (packageMenu.checkClickPackage3 and (not clickedOnce)):
                    cur_state = "game"
                    clickedOnce = True     

            if (cur_state =="game"):
                while (curr_rounds <rounds):
                    gameScreen.update()
                    if (questionScreen.checkClickNext(pos) and (not clickedOnce)):
                        #NEXT QUESTION / PLAYER 2 TURN FUNCTIONALITY
                        clickedOnce = True

    # start menu 
    if (cur_state == "start"):
        screen.fill(white)
        screen.blit(start_bg_img, start_bg_img_rect)
        startMenu.update()

    # settings menu
    if (cur_state == "settings"):
        screen.fill(white)
        screen.blit(bg_img, bg_img_rect)
        settingsMenu.update()

    # package menu
    if (cur_state == "packages"):
        screen.fill(white)
        screen.blit(bg_img, bg_img_rect)
        packageMenu.update()
    
    # game
    if (cur_state == "game"):
        screen.fill(white)
        screen.blit(bg_img, bg_img_rect)
        gameScreen.update()

    pygame.display.flip()
