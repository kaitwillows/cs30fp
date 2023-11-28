import pygame
from util import Coordinates


'''
class GameObjects:
    def __init__():
'''
    

# unity did not work in my favour so im just gonna make all this from scratch aaaaa but i also have a cart after this so idk how thats gonna go for me aaaaaaa
class Player:
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
        self.sprite = pygame.image.load('./assets/ralsei.png')
    def draw(self):
        from main import mouse_screen_offset, screen
        screen.blit(self.sprite, (self.coordinates + mouse_screen_offset).as_tuple())


class Map:
    def __init__(self, initial_position: Coordinates):
        self.initial_position = initial_position
        self.tile_map = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
    def draw(self) -> pygame.Surface:
        tile_size = 200 # find a better place to define this constant
        map_surface = pygame.Surface((tile_size * 5, tile_size * 5))
        map_surface.set_colorkey((255, 255, 255))
        map_surface.fill((255, 255, 255))
        for i, row in enumerate(self.tile_map):
            for j, tile in enumerate(row):
                x = j * tile_size
                y = i * tile_size
                if tile == 1:
                    pygame.draw.rect(map_surface, (0, 0, 0), (x, y, tile_size, tile_size))
        return map_surface


