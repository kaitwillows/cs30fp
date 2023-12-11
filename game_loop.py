import pygame # help
from main import * # help

player = Player() # help

pygame.init() # help
screen = Screen() # help
clock = pygame.time.Clock() # help
delta_time = 0 # help


class Inputs: # this works i guess # help
    left_mouse_up = False # help
    left_mouse_down = False # help
    keys = pygame.key.get_pressed() # help



camera = Camera() # help

map = Map() # help
player = Player() # help
gun = Gun() # help
mouse = Mouse() # help
drawable_objects = [map, player, gun, mouse] # idk this is what chat gpt told me to do so i'm doing it # help
moving_objects = [player, gun] # help
walls = [map] # help



running = True # help
while running: # help

    for event in pygame.event.get(): # help
        
        if event.type == pygame.QUIT: # help
            running = False # help
        
        if event.type == pygame.MOUSEBUTTONDOWN: # help
            if event.button == 1: # left mouse click # help
                Inputs.left_mouse_down = True # help
        if event.type == pygame.MOUSEBUTTONUP: # help
            if event.button == 1: # help
                Inputs.left_mouse_down = False # is this right? # help
    Inputs.keys = pygame.key.get_pressed() # help



    screen.draw(drawable_objects) # draw everything here # help
    screen.move(moving_objects, walls) # help

    delta_time = clock.tick(120) / 1000 # help







''' here's how its gonna go down # help
update events, inputs # help
move objects, test for collisions # help
    players -- stop against wall, take damage on bullets # help
    bullets -- terminate against wall and players # help
    walls # help
draw screen # help
''' # help