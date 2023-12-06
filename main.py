# this is what i like to call making a game when you don't know how
# i am so bad at this
# why did i do this

# Example file showing a circle moving on screen
import math
import pygame

# from util import Coordinates
from game_objects import Map, Bullet
from util import add_coordinates, multiply_coordinates


# pygame setup
pygame.init()
screen_res = [1280, 720]
screen = pygame.display.set_mode(screen_res)

clock = pygame.time.Clock()
running = True
dt = 0
camera = (0, 0)

mouse_screen_offset = (pygame.mouse.get_pos()[0] - screen_res[0]/2*-.5, pygame.mouse.get_pos()[1] - screen_res[1]/2*-.5)
camera_cordinates = (0, 0)

# pygame.event.set_grab(True)
# disabling this until its really needed

# create player object aaaa

player_image = pygame.image.load("./assets/ralsei.png") # 23 x 43 pixels
# player_hitbox = pygame.Rect(0, 0, 23, 43)
hitbox = pygame.mask.from_surface(pygame.Surface((23, 43)))
player_coordinates = (0, 0)
map = Map("./assets/map1.png") # does this really need to be an object? yes!
map_surface = map.draw()
map_mask = pygame.mask.from_surface(map_surface)
crosshair = pygame.image.load("./assets/crosshair.png")
pygame.mouse.set_visible(False)

player_speed = (300*dt)

left_mouse_down = False
left_mouse_up = False 

fire_rate = .3
time_since_last_fire = 0.0
bullets = []
bullet_sprite = pygame.image.load("./assets/bullet.png")

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # girl
            if event.button == 1: # left mouse click
                left_mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_mouse_down = False
                left_mouse_up = True
            else:
                left_mouse_up = False 

    mouse_screen_offset = (-1 * (pygame.mouse.get_pos()[0] - screen_res[0]/2)*.5), (-1 * (pygame.mouse.get_pos()[1] - screen_res[1]/2)*.5) # why

    camera_cordinates = ((player_coordinates[0] - screen_res[0]/2)*-1, (player_coordinates[1] - screen_res[1]/2)*-1)

    total_offset = add_coordinates(mouse_screen_offset, camera_cordinates)

    # print(total_offset)
    
    time_since_last_fire += dt
    if left_mouse_down:
        if time_since_last_fire >= fire_rate:
            # like i have a math final after this and i did not study (only because i was working till 10 but still)

            raw_crosshair_coordinates = add_coordinates(pygame.mouse.get_pos(), (multiply_coordinates(screen_res, (-.5, -.5))))
            # im so sorry
            magnitude = math.sqrt(raw_crosshair_coordinates[0]**2 + raw_crosshair_coordinates[1]**2) # i am coding this like an ape

            normalized_x = raw_crosshair_coordinates[0] / magnitude
            normalized_y = raw_crosshair_coordinates[1] / magnitude

            try:
                velocity_ratio = raw_crosshair_coordinates[0] / raw_crosshair_coordinates[1] if raw_crosshair_coordinates[0]!=0 else 1
            except: # just please trust me on this (LITERALLY DO NOT TRUST ME ON THIS PLEASE)
                velocity_ratio = 0

            bullet_velocity_y = math.sqrt(1 - normalized_x**2)
            bullet_velocity_x = bullet_velocity_y * math.copysign(1, raw_crosshair_coordinates[0]) * abs(velocity_ratio) if raw_crosshair_coordinates[0] >= 0 else -bullet_velocity_y * velocity_ratio

            bullet_velocity = multiply_coordinates((normalized_x, normalized_y), (10, 10)) # i should have just used unity
            # who on earth let me cook

            bullets.append(Bullet(player_coordinates, (bullet_velocity)))
            time_since_last_fire = 0.0

    
    # for collision check later
    old_player_cords = player_coordinates

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_coordinates = add_coordinates(player_coordinates, (0, -300 * dt))
    if keys[pygame.K_s]:
        player_coordinates = add_coordinates(player_coordinates, (0, 300 * dt))

    try:
        if map_mask.overlap(hitbox, player_coordinates):
            player_coordinates = old_player_cords
    except:
        pass


    old_player_cords = player_coordinates

    if keys[pygame.K_a]:
        player_coordinates = add_coordinates(player_coordinates, (-300 * dt, 0))
    if keys[pygame.K_d]:
        player_coordinates = add_coordinates(player_coordinates, (300 * dt, 0)) 


    try:
        if map_mask.overlap(hitbox, player_coordinates):
            player_coordinates = old_player_cords
    except:
        pass




    screen.fill("grey")


    

    #print((mouse_screen_offset + world_offset).as_tuple[0])
    screen.blit(map_surface, total_offset)
    screen.blit(player_image, add_coordinates((screen_res[0]/2, screen_res[1]/2), mouse_screen_offset))
    screen.blit(crosshair, add_coordinates(pygame.mouse.get_pos(), (-16, -16)))

    for bullet in bullets:
        bullet.move()
        screen.blit(bullet_sprite, add_coordinates(bullet.position, total_offset))

    pygame.display.flip()

    # 120 make smooth
    dt = clock.tick(120) / 1000




pygame.quit()