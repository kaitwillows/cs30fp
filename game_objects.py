import pygame
from util import Coordinates
from main import mouse_screen_offset, screen


'''
class GameObjects:
    def __init__():
'''
    

# unity did not work in my favour so im just gonna make all this from scratch aaaaa but i also have a cart after this so idk how thats gonna go for me aaaaaaa
class Player:
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates
    sprite = pygame.image.load('./assets/ralsei.png')
    def draw():
        screen.blit(self.sprite, (self.coordinates + mouse_screen_offset).as_tuple())
