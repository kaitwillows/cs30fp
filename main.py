# this is what i like to call making a game when you don't know how

# Example file showing a circle moving on screen
import pygame

# from util import Coordinates
from game_objects import Player, Map
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
player = Player((255, 255))
map = Map() # does this really need to be an object
map_surface = map.draw()
map_mask = pygame.mask.from_surface(map_surface)

player_speed = (300*dt)

while running:

    start_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_screen_offset = (-1 * (pygame.mouse.get_pos()[0] - screen_res[0]/2)*.5), (-1 * (pygame.mouse.get_pos()[1] - screen_res[1]/2)*.5) # why

    camera_cordinates = ((player.coordinates[0] - screen_res[0]/2)*-1, (player.coordinates[1] - screen_res[1]/2)*-1)

    total_offset = mouse_screen_offset + camera_cordinates

    
    # for collision check later
    old_player_cords = player.coordinates

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.coordinates = add_coordinates(player.coordinates, (0, -300 * dt))
    if keys[pygame.K_s]:
        player.coordinates = add_coordinates(player.coordinates, (0, 300 * dt))
    if keys[pygame.K_a]:
        player.coordinates = add_coordinates(player.coordinates, (-300 * dt, 0))
    if keys[pygame.K_d]:
        player.coordinates = add_coordinates(player.coordinates, (300 * dt, 0)) 


    if map_mask.get_at(player.coordinates):
        # player.coordinates = old_player_cords
        pass

    screen.fill("grey")

    #print((mouse_screen_offset + world_offset).as_tuple[0])
    screen.blit(map_surface, total_offset)
    player.draw(add_coordinates((screen_res[0]/2, screen_res[1]/2), mouse_screen_offset))


    pygame.display.flip()

    # basically just count to 60^-1 cos why not
    dt = clock.tick(60) / 1000



pygame.quit()