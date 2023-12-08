import pygame

class Constants:
    SCREEN_RESOLUTION = (1280, 720)
    BACKGROUND = (255, 255, 255)

class Player:
    SPRITE = pygame.image.load("./assets/ralsei.png")
    SIZE = (23, 43) # this could be derived
    SPEED_STRAIGHT = 300
    SPEED_DIAGONAL = 212.13 
    coordinates = [0, 0]
    hitbox = pygame.mask.from_surface(pygame.Surface((SIZE)))

class Map:
    IMAGE = pygame.image.load("./assets/map1.png")
    SCALE_FACTOR = 50
    SCALED_IMAGE = pygame.transform.scale(IMAGE, IMAGE.get_width() * SCALE_FACTOR, IMAGE.get_height() * SCALE_FACTOR)
    MASK = pygame.mask.from_surface(SCALED_IMAGE)

class Camera: # this might have a lot of problems with circular importing but we can deal with that when we get there
    MOUSE_CAMERA_OFFSET_INFLUENCE = 0.5 
    mouse_camera_offset = [0, 0] # for the player (wait)
    combined_camera_offset = [0, 0]

    def update_camera_position(mouse_coordinates: list): # could be better in reverse order?
        mouse_x, mouse_y = mouse_coordinates

        centered_mouse_x = mouse_x - Constants.SCREEN_RESOLUTION[0]/2
        mouse_camera_offset_x = -centered_mouse_x * Camera.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_x = Player.coordinates[0] - Constants.SCREEN_RESOLUTION[0]/2 + mouse_camera_offset_x # center on player and add mouse offset

        centered_mouse_y = mouse_y - Constants.SCREEN_RESOLUTION[1]/2
        mouse_camera_offset_y = -centered_mouse_y * Camera.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_y = Player.coordinates[1] - Constants.SCREEN_RESOLUTION[1]/2 + mouse_camera_offset_y

        return (mouse_camera_offset_x, mouse_camera_offset_y), (combined_camera_offset_x, combined_camera_offset_y)

        
