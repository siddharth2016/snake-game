import pygame
from pygame.locals import *

if __name__ == "__main__":
    
    pygame.init()
    pygame.display.set_mode((1000, 500))
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False