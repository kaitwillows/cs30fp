import pygame
import os

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Load images
rect_image = pygame.Surface((50, 50))
rect_image.fill((255, 0, 0))  # Red rectangle

# Create a rectangle
rect = rect_image.get_rect()
rect.center = (width // 2, height // 2)

# Create a mask for the rectangle
rect_mask = pygame.mask.from_surface(rect_image)

# Create a mask for the obstacle (replace this with your obstacle)
obstacle_mask = pygame.mask.from_surface(pygame.Surface((50, 50)))
obstacle_mask.fill()

running = True
while running:
    screen.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update rectangle position (for example, move it to the right)
    rect.x += 1

    # Check for collision between rectangle and obstacle mask
    if rect_mask.overlap(obstacle_mask, (obstacle_mask.get_rect().x - rect.x, obstacle_mask.get_rect().y - rect.y)):
        print("Collision detected!")

    # Draw the rectangle
    screen.blit(rect_image, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
