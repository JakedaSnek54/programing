import pygame
from sys import exit
#initialize and setting windows up
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Title')
#background


#game loop
while True:
    #draw all elements
    #update everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
  
    pygame.display.update()
    clock.tick(60)