import pygame 
from game_objects import * 


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
player = Player([288, 262])
enemy = Enemy([2674, 2661])
gun = Gun() 
enemy_gun = EnemyGun()
mouse = Mouse() 
minimap = MiniMap()
drawable_objects = [map, player, enemy, gun, enemy_gun, minimap, mouse]
moving_objects = [player, enemy, gun, enemy_gun] 
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
                Inputs.left_mouse_down = False 

    Inputs.keys = pygame.key.get_pressed() 

    screen.move(moving_objects, walls) 
    screen.draw(drawable_objects) 

    delta_time = clock.tick(288) / 1000 
pygame.quit()
