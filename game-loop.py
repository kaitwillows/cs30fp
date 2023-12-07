import pygame
from main import Constants, Player

player = Player()

pygame.init()
SCREEN = pygame.display.set_mode(Constants.SCREEN_RES) # is SCREEN a constant really??

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


