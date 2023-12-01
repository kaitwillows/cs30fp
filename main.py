# this is what i like to call making a game when you don't know how

# Example file showing a circle moving on screen
import pygame

# from util import Coordinates
from game_objects import Map
from util import add_coordinates

# pygame setup
pygame.init()
screen_res = (1280, 720)
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
player = pygame.image.load("./assets/ralsei.png") # 23 x 43 pixels
player_coordinates = (255, 255)
map = Map() # does this really need to be an object? yes!
map_surface = map.draw()
map_mask = pygame.mask.from_surface(map_surface)
crosshair = pygame.image.load("./assets/crosshair.png")
pygame.mouse.set_visible(False)

player_speed = (300*dt)

while running:

    start_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_screen_offset = (-1 * (pygame.mouse.get_pos()[0] - screen_res[0]/2)*.5), (-1 * (pygame.mouse.get_pos()[1] - screen_res[1]/2)*.5) # why

    camera_cordinates = ((player_coordinates[0] - screen_res[0]/2)*-1, (player_coordinates[1] - screen_res[1]/2)*-1)

    total_offset = add_coordinates(mouse_screen_offset, camera_cordinates)

    print(total_offset)

    
    # for collision check later
    old_player_cords = player_coordinates

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_coordinates = add_coordinates(player_coordinates, (0, -300 * dt))
    if keys[pygame.K_s]:
        player_coordinates = add_coordinates(player_coordinates, (0, 300 * dt))

    try:
        if map_mask.get_at(player_coordinates):
            player_coordinates = old_player_cords
    except:
        pass


    old_player_cords = player_coordinates

    if keys[pygame.K_a]:
        player_coordinates = add_coordinates(player_coordinates, (-300 * dt, 0))
    if keys[pygame.K_d]:
        player_coordinates = add_coordinates(player_coordinates, (300 * dt, 0)) 

    try:
        if map_mask.get_at(player_coordinates):
            player_coordinates = old_player_cords
    except:
        pass




    screen.fill("grey")

    #print((mouse_screen_offset + world_offset).as_tuple[0])
    screen.blit(map_surface, total_offset)
    screen.blit(player, add_coordinates((screen_res[0]/2, screen_res[1]/2), mouse_screen_offset))
    screen.blit(crosshair, add_coordinates(pygame.mouse.get_pos(), (-16, -16)))


    pygame.display.flip()

    # 120 make smooth
    dt = clock.tick(120) / 1000




pygame.quit()