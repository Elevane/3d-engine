import pygame
import sys


pygame.init()# initialisation of pygame
WIDTH, LENGTH = 1000,1000#screensize
cubeX, cubeY = WIDTH//2, LENGTH//2#coordinates x and y of the cube, so basically its the center of teh screen at start
screen = pygame.display.set_mode((WIDTH,LENGTH))
clock = pygame.time.Clock()#instanciation of a time object with pygame


verts = (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)


while True: #infinite loop
    dt = clock.tick() / 1000

    for event in pygame.event.get(): #listen to event
        if event.type == pygame.QUIT: # if event is quitting:
            pygame.quit() #stop pygame
            sys.exit() # stop running
    
    screen.fill((155,155,155))# fill the screen with given color


    pygame.display.flip()
