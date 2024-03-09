import pygame
from const import *


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sixth Sense')
screen.fill(red)
pygame.display.flip()

running = True


# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False