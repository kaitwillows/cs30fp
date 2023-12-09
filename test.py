import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

window_width = 400
window_height = 300

screen = pygame.display.set_mode((window_width, window_height))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill((0, 0, 0)) 

    # Draw a rectangle at the mouse position to simulate a "window"
    pygame.draw.rect(screen, (255, 255, 255), (mouse_x - 50, mouse_y - 50, 100, 100))

    # Update the display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
