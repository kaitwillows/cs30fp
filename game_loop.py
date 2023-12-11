import pygame
from main import *

player = Player()

pygame.init()
screen = Screen()
clock = pygame.time.Clock()
delta_time = 0


class Inputs: # this works i guess
    left_mouse_up = False
    left_mouse_down = False
    keys = pygame.key.get_pressed()



camera = Camera()

map = Map()
player = Player()
gun = Gun()
mouse = Mouse()
drawable_objects = [map, player, gun, mouse] # idk this is what chat gpt told me to do so i'm doing it
moving_objects = [player, gun]
walls = [map]



running = True
while running:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left mouse click
                Inputs.left_mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Inputs.left_mouse_down = False # is this right?



    screen.draw(drawable_objects) # draw everything here
    screen.move(moving_objects, walls)

    delta_time = clock.tick(120) / 1000







''' here's how its gonna go down
update events, inputs
move objects, test for collisions
    players -- stop against wall, take damage on bullets
    bullets -- terminate against wall and players
    walls
draw screen
'''