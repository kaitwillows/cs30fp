import pygame
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map with Collision Detection")

# Load images
current_directory = os.path.dirname(__file__)
image_path = os.path.join(current_directory, 'assets')  # Replace 'images' with your folder name
background_image = pygame.image.load(os.path.join(image_path, 'background.png')).convert()
player_image = pygame.image.load(os.path.join(image_path, 'ralsei.png')).convert_alpha()

# Define player properties
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_mask = pygame.mask.from_surface(player_image)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player (example movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Collision detection
    player_mask_offset = (player_rect.x, player_rect.y)
    overlap = background_image.get_rect().colliderect(player_rect)

    if overlap:
        # Get the mask of the overlapping area between player and background
        overlap_mask = pygame.mask.from_surface(background_image, pygame.mask.from_threshold(background_image, RED, (1, 1, 1, 255)))

        # Offset the player mask to the overlapping area
        player_mask_offset = (player_rect.x - overlap_mask.get_bounding_rects()[0].x,
                              player_rect.y - overlap_mask.get_bounding_rects()[0].y)

        # Check for collision between player mask and background mask
        if overlap_mask.overlap(player_mask, player_mask_offset):
            # Collision occurred, handle accordingly (in this example, stopping movement)
            player_rect.x += 5 if keys[pygame.K_LEFT] else 0
            player_rect.x -= 5 if keys[pygame.K_RIGHT] else 0
            player_rect.y += 5 if keys[pygame.K_UP] else 0
            player_rect.y -= 5 if keys[pygame.K_DOWN] else 0

    # Draw player
    screen.blit(player_image, player_rect)

    pygame.display.flip()

pygame.quit()
