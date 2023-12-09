import pygame
from main import *

player = Player()

pygame.init()
screen = Screen()

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


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.update(drawable_objects)









''' here's how its gonna go down
update events, inputs
move objects, test for collisions
    players -- stop against wall, take damage on bullets
    bullets -- terminate against wall and players
    walls
draw screen
'''