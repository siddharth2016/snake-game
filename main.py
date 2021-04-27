import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((1000, 500))
    
    block = pygame.image.load("resources/block.jpeg")
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))
    
    pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == QUIT:
                running = False