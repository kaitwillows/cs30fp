import pygame

# maybe have a GameObject parent class so that all the updates can be run with a single for loop?

class Screen:
    SCREEN_RESOLUTION = (1920, 1080)
    BACKGROUND = (255, 255, 255)

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_RESOLUTION)
    def update(self, drawable_objects):
        from game_loop import camera
        camera.update_camera_position()
        self.screen.fill("grey")
        for object in drawable_objects:
            object.draw(self.screen)
        pygame.display.flip()

class Mouse: # oh god
    IMAGE = pygame.image.load("./assets/crosshair.png")
    SIZE = (IMAGE.get_width(), IMAGE.get_width())
    DRAW_OFFSET = (SIZE[0]/2, SIZE[1]/2)
    def draw(self, surface: pygame.Surface):
        mouse_coordinates = pygame.mouse.get_pos()
        crosshair_coordinates = (mouse_coordinates[0] - Mouse.DRAW_OFFSET[0], mouse_coordinates[1] - Mouse.DRAW_OFFSET[1])
        surface.blit(Mouse.IMAGE, crosshair_coordinates)


class Player:
    def __init__(self):
        self.IMAGE = pygame.image.load("./assets/ralsei.png")
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_width())
        self.SPEED_STRAIGHT = 300
        self.SPEED_DIAGONAL = 212.13 
        self.coordinates = [0, 0]
        self.hitbox = pygame.mask.from_surface(pygame.Surface((self.SIZE)))
    def move(self, keys):
        pass # TODO
    def draw(self, surface: pygame.Surface):
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
    def draw(self, surface: pygame.Surface):
        pass # TODO
    
class Map:
    def __init__(self):
        self.RAW_IMAGE = pygame.image.load("./assets/map1.png").convert_alpha()
        self.SCALE_FACTOR = 50
        self.IMAGE = pygame.Surface((self.RAW_IMAGE.get_width() * self.SCALE_FACTOR, self.RAW_IMAGE.get_height() * self.SCALE_FACTOR), pygame.SRCALPHA)
        self.IMAGE = pygame.transform.scale(self.RAW_IMAGE, (self.RAW_IMAGE.get_width() * self.SCALE_FACTOR, self.RAW_IMAGE.get_height() * self.SCALE_FACTOR), self.IMAGE)
        self.MASK = pygame.mask.from_surface(self.IMAGE)
    def draw(self, surface: pygame.Surface):
        from game_loop import camera
        surface.blit(self.IMAGE, camera.combined_camera_offset)

class Camera: # this might have a lot of problems with circular importing but we can deal with that when we get there
    def __init__(self):
        self.MOUSE_CAMERA_OFFSET_INFLUENCE = 0.5 
        self.mouse_camera_offset = [0, 0] # for the player (wait)
        self.combined_camera_offset = [0, 0]

    def update_camera_position(self): # could be better in reverse order?
        from game_loop import player
        # print(combined_camera_offset)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        centered_mouse_x = mouse_x - Screen.SCREEN_RESOLUTION[0]/2
        mouse_camera_offset_x = -centered_mouse_x * self.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_x = player.coordinates[0] - Screen.SCREEN_RESOLUTION[0]/2 + mouse_camera_offset_x # center on player and add mouse offset

        centered_mouse_y = mouse_y - Screen.SCREEN_RESOLUTION[1]/2
        mouse_camera_offset_y = -centered_mouse_y * self.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_y = player.coordinates[1] - Screen.SCREEN_RESOLUTION[0]/2 + mouse_camera_offset_y # center on player and add mouse offset

        self.mouse_camera_offset = [mouse_camera_offset_x, mouse_camera_offset_y]
        self.combined_camera_offset = [combined_camera_offset_x, combined_camera_offset_y]
        

