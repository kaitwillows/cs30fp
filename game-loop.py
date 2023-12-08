import pygame
from main import *

player = Player()

pygame.init()
screen = Screen()

class Inputs: # ???
    left_mouse_up = False
    left_mouse_down = False



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


