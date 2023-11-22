# btw this is all copy/pasted from the pygame docs its not plagerism!!

# Example file showing a circle moving on screen
import pygame

from util import Coordinates
from game_objects import Player

# pygame setup
pygame.init()
screen_res = (1280, 720)
screen = pygame.display.set_mode(screen_res)

clock = pygame.time.Clock()
running = True
dt = 0
camera = (0, 0)

mouse_screen_offset = Coordinates(pygame.mouse.get_pos()[0] - screen_res[0]/2*-.5, pygame.mouse.get_pos()[1] - screen_res[1]/2*-.5)

# pygame.event.set_grab(True)
# disabling this until its really needed

# create player object aaaa
playerCords = Coordinates(screen_res[0]/2, screen_res[1])
player = Player(playerCords)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_screen_offset.x = -1 * (pygame.mouse.get_pos()[0] - screen_res[0]/2)*.5 
    mouse_screen_offset.y = -1 * (pygame.mouse.get_pos()[1] - screen_res[1]/2)*.5

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    player.draw()

    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    '''

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()