import pygame

class Screen:
    SCREEN_RESOLUTION = (1280, 720)
    BACKGROUND = (255, 255, 255)

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_RES) # is SCREEN a constant really??

class Player:
    IMAGE = pygame.image.load("./assets/ralsei.png")
    SIZE = (23, 43) # this could be derived
    SPEED_STRAIGHT = 300
    SPEED_DIAGONAL = 212.13 
    coordinates = [0, 0]
    hitbox = pygame.mask.from_surface(pygame.Surface((SIZE)))
    def move(self):
        pass # TODO

class Bullet: # pray to god i'm doing this right
    def __init__(self, coordinates: list, velocity: list):
        self.coordinates = coordinates
        self.velocity = velocity
    def move(self):
        self.coordinates[0] += self.velocity[0]
        self.coordinates[1] += self.velocity[1]

class Gun:
    BULLET_IMAGE = pygame.image.load("./assets/bullet.png") 
    FIRE_RATE = .3
    time_since_last_fire = 0.0
    bullets = []
    
class Map:
    RAW_IMAGE = pygame.image.load("./assets/map1.png")
    SCALE_FACTOR = 50
    IMAGE = pygame.Surface((RAW_IMAGE.get_width() * SCALE_FACTOR, RAW_IMAGE.get_height() * SCALE_FACTOR))
    IMAGE = pygame.transform.scale(RAW_IMAGE, (RAW_IMAGE.get_width() * SCALE_FACTOR, RAW_IMAGE.get_height() * SCALE_FACTOR), IMAGE)
    MASK = pygame.mask.from_surface(IMAGE)

class Camera: # this might have a lot of problems with circular importing but we can deal with that when we get there
    MOUSE_CAMERA_OFFSET_INFLUENCE = 0.5 
    mouse_camera_offset = [0, 0] # for the player (wait)
    combined_camera_offset = [0, 0]

    def update_camera_position(mouse_coordinates: list): # could be better in reverse order?
        mouse_x, mouse_y = mouse_coordinates

        centered_mouse_x = mouse_x - Screen.SCREEN_RESOLUTION[0]/2
        mouse_camera_offset_x = -centered_mouse_x * Camera.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_x = Player.coordinates[0] - Screen.SCREEN_RESOLUTION[0]/2 + mouse_camera_offset_x # center on player and add mouse offset

        centered_mouse_y = mouse_y - Screen.SCREEN_RESOLUTION[1]/2
        mouse_camera_offset_y = -centered_mouse_y * Camera.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_y = Player.coordinates[1] - Screen.SCREEN_RESOLUTION[1]/2 + mouse_camera_offset_y

        return (mouse_camera_offset_x, mouse_camera_offset_y), (combined_camera_offset_x, combined_camera_offset_y)

