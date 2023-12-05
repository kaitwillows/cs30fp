import pygame
from util import add_coordinates
from util import TILE_SIZE


'''
class GameObjects:
    def __init__():
'''
    

# unity did not work in my favour so im just gonna make all this from scratch aaaaa but i also have a cart after this so idk how thats gonna go for me aaaaaaa
class Player:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.sprite = pygame.image.load('./assets/ralsei.png')
    def draw(self, coordinates):
        from main import mouse_screen_offset, screen
        screen.blit(self.sprite, coordinates)


class Map:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def draw(self) -> pygame.Surface:
        map_surface = pygame.Surface((self.width * TILE_SIZE, self.height * TILE_SIZE))
        map_surface.set_colorkey((255, 255, 255))
        map_surface.fill((255, 255, 255))
        for y in range(self.height):
            for x in range(self.width):
                pixel_color = self.image.get_at((x, y))
                if pixel_color == (0, 0, 0, 255):
                    pygame.draw.rect(map_surface, (0, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        return map_surface


class Bullet: # if i didn't regret my life decisions at this point, i soon will
    BULLET_PATH = "./assets/bullet.png" # i mean its like kind of a constant
    # where should the image path be defined?
    # how do i even do the mouse????????? pythagorus???????????????????????
    # nvm bois i got this
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity 
        self.y_velocity = y_velocity # i guess thats it
    def move(self): # we'll do test point for removal (hhhhh)
        self.x += self.x_velocity
        self.y += self.y_velocity


        


