# this is what i like to call making a game when you don't know how

# Example file showing a circle moving on screen
import pygame

from util import Coordinates
from game_objects import Player, Map

# pygame setup
pygame.init()
screen_res = (1280, 720)
screen = pygame.display.set_mode(screen_res)

clock = pygame.time.Clock()
running = True
dt = 0
camera = (0, 0)

mouse_screen_offset = Coordinates(pygame.mouse.get_pos()[0] - screen_res[0]/2*-.5, pygame.mouse.get_pos()[1] - screen_res[1]/2*-.5)
world_offset = Coordinates(0, 0)

# pygame.event.set_grab(True)
# disabling this until its really needed

# create player object aaaa
player = Player(0, 0)
map = Map() # does this really need to be an object
map_surface = map.draw()
map_mask = pygame.mask.from_surface(map_surface)

player_speed = (300*dt)

while running:

    start_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_screen_offset.x = -1 * (pygame.mouse.get_pos()[0] - screen_res[0]/2)*.5 
    mouse_screen_offset.y = -1 * (pygame.mouse.get_pos()[1] - screen_res[1]/2)*.5
    
    # for collision check later
    old_player_cords = player.coordinates

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.coordinates += Coordinates(0, 300 * dt)
    if keys[pygame.K_s]:
        player.coordinate += Coordinates(0, -300 * dt)
    if keys[pygame.K_a]:
        player.coordinate += Coordinates(300 * dt, 0)
    if keys[pygame.K_d]:
        player.coordinate += Coordinates(-300 * dt, 0)


    if map_mask.get_at((pygame.mouse.get_pos())):
        print("OMG")

    screen.fill("grey")

    #print((mouse_screen_offset + world_offset).as_tuple[0])
    screen.blit(map_surface, (0, 0))
    player.draw(player.coordinates)


    pygame.display.flip()

    # basically just count to 60^-1 cos why not
    dt = clock.tick(60) / 1000



pygame.quit()