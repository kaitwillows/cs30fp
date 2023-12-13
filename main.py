import pygame



class Screen:
    SCREEN_RESOLUTION = (800, 800)
    BACKGROUND = (255, 255, 255)
    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_RESOLUTION)
        self.frame = 0
    def move(self, moving_objects: list[object], walls: pygame.mask):
        self.frame += 1
        if self.frame > 5:
            import random, string
            pygame.display.set_caption(''.join(random.choice(string.ascii_letters) for _ in range((10))))
            self.frame = 0
        for object in moving_objects:
            object.move(walls) # scared (warrented)
    def draw(self, drawable_objects):
        from game_loop import camera
        camera.update_camera_position()
        self.screen.fill("grey")
        for object in drawable_objects:
            object.draw(self.screen)
        pygame.display.flip()

class Mouse:
    def __init__(self):
        self.IMAGE = pygame.image.load("./assets/crosshair.png")
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_width())
        self.DRAW_OFFSET = (self.SIZE[0]/2, self.SIZE[1]/2)
        self.centered_coordinates = [0, 0]
    def draw(self, surface: pygame.Surface):
        from game_loop import screen
        mouse_coordinates = pygame.mouse.get_pos()
        centered_coordinates_x = mouse_coordinates[0] - screen.SCREEN_RESOLUTION[0]/2
        centered_coordinates_y = mouse_coordinates[1] - screen.SCREEN_RESOLUTION[1]/2
        self.centered_coordinates = [centered_coordinates_x, centered_coordinates_y]
        crosshair_coordinates = (mouse_coordinates[0] - self.DRAW_OFFSET[0], mouse_coordinates[1] - self.DRAW_OFFSET[1])
        surface.blit(self.IMAGE, crosshair_coordinates)


class Player:
    def __init__(self):
        self.IMAGE = pygame.image.load("./assets/ralsei.png")
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_height())
        self.SPEED_STRAIGHT = 300
        self.SPEED_DIAGONAL = 212.13 
        self.coordinates = [100, 100]
        self.hitbox = pygame.mask.from_surface(pygame.Surface((self.SIZE)))
    def move(self, walls: list):
        from game_loop import Inputs, delta_time

        old_coordinates = self.coordinates[:]
        horizontal_axis = (Inputs.keys[pygame.K_d] ^ Inputs.keys[pygame.K_a])
        vertical_axis = (Inputs.keys[pygame.K_w] ^ Inputs.keys[pygame.K_s])
        if horizontal_axis and vertical_axis:
            speed = self.SPEED_DIAGONAL
        else:
            speed = self.SPEED_STRAIGHT

        # input
        if Inputs.keys[pygame.K_d]:
            self.coordinates[0] += speed * delta_time
        if Inputs.keys[pygame.K_a]:
            self.coordinates[0] -= speed * delta_time
        
        # collision handling
        collision = False
        for wall in walls:
            if wall.MASK.overlap(self.hitbox, self.coordinates): 
                collision = True
        if collision:
            self.coordinates = old_coordinates[:]
        else:
            old_coordinates = self.coordinates[:]

        # input
        if Inputs.keys[pygame.K_s]:
            self.coordinates[1] += speed * delta_time
        if Inputs.keys[pygame.K_w]:
            self.coordinates[1] -= speed * delta_time

        # collision handling
        collision = False
        for wall in walls:
            if wall.MASK.overlap(self.hitbox, self.coordinates): 
                collision = True
        if collision:
            self.coordinates = old_coordinates[:]
        else:
            old_coordinates = self.coordinates[:]
    def draw(self, surface: pygame.Surface):
        from game_loop import camera, screen
        draw_coordinates_x = screen.SCREEN_RESOLUTION[0]/2 + camera.mouse_camera_offset[0]
        draw_coordinates_y = screen.SCREEN_RESOLUTION[1]/2 + camera.mouse_camera_offset[1]
        draw_coordinates = (draw_coordinates_x, draw_coordinates_y)
        surface.blit(self.IMAGE, draw_coordinates)

class Bullet: 
    IMAGE = pygame.image.load("./assets/bullet.png")
    def __init__(self, coordinates: list, velocity: list):
        self.coordinates = coordinates
        self.velocity = velocity
    def move(self):
        self.coordinates[0] += self.velocity[0]
        self.coordinates[1] += self.velocity[1]
    def draw(self, surface: pygame.Surface):
        from game_loop import camera
        draw_coordinates_x = self.coordinates[0] + camera.combined_camera_offset[0]
        draw_coordinates_y = self.coordinates[1] + camera.combined_camera_offset[1]
        draw_coordinates = (draw_coordinates_x, draw_coordinates_y)
        surface.blit(self.IMAGE, draw_coordinates)

class Gun:
    def __init__(self):
        self.VELOCITY_MULTIPLIER = 5
        self.FIRE_RATE = .1
        self.time_since_last_fire = 0.0
        self.bullets = []
    def fire(self): 
        from game_loop import delta_time, Inputs, mouse, player
        import math

        self.time_since_last_fire += delta_time 
        
        if Inputs.left_mouse_down == False:
            return
        if self.time_since_last_fire > self.FIRE_RATE:
            self.time_since_last_fire = 0
        else:
            return
        raw_x, raw_y = mouse.centered_coordinates
        magnitude = math.sqrt(raw_x**2 + raw_y**2)
        if magnitude == 0:
            x_velocity = 0
            y_velocity = 0
        else:
            x_velocity = raw_x / magnitude * self.VELOCITY_MULTIPLIER
            y_velocity = raw_y / magnitude * self.VELOCITY_MULTIPLIER

        self.bullets.append(Bullet(player.coordinates[:], [x_velocity, y_velocity]))

    def move(self, walls):
        self.fire()
        for bullet in self.bullets:
            bullet.move()
    def draw(self, surface: pygame.Surface):
        for bullet in self.bullets:
            bullet.draw(surface)

    
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

class Camera:
    def __init__(self):
        self.MOUSE_CAMERA_OFFSET_INFLUENCE = 0.5 
        self.mouse_camera_offset = [0, 0] # for the player 
        self.combined_camera_offset = [0, 0]
    def update_camera_position(self): 
        from game_loop import player, mouse

        mouse_camera_offset_x = -mouse.centered_coordinates[0] * self.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_x = -player.coordinates[0] + Screen.SCREEN_RESOLUTION[0]/2 + mouse_camera_offset_x # center on player and add mouse offset

        mouse_camera_offset_y = -mouse.centered_coordinates[1] * self.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_y = -player.coordinates[1] + Screen.SCREEN_RESOLUTION[1]/2 + mouse_camera_offset_y # center on player and add mouse offset

        self.mouse_camera_offset = [mouse_camera_offset_x, mouse_camera_offset_y]
        self.combined_camera_offset = [combined_camera_offset_x, combined_camera_offset_y]