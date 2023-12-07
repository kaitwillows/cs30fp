import pygame

class Constants:
    SCREEN_RES = (1280, 720)
    BACKGROUND = (255, 255, 255)

class Camera:
    

class Player:
    SPRITE = pygame.image.load("./assets/ralsei.png")
    SIZE = (23, 43)
    SPEED_STRAIGHT = 300
    SPEED_DIAGONAL = 212.13
    coordinates = [0, 0]
    hitbox = pygame.mask.from_surface(pygame.Surface((SIZE)))

class Map:
    IMAGE = pygame.image.load("./assets/map1.png")
    SCALE_FACTOR = 50
    SCALED_IMAGE = pygame.transform.scale(IMAGE, IMAGE.get_width() * SCALE_FACTOR, IMAGE.get_height() * SCALE_FACTOR)
    MASK = pygame.mask.from_surface(SCALED_IMAGE)
    


