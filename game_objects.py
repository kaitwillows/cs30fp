import pygame


class Screen: # screen is the game window, it also handles logic and rendering for all game objects
    SCREEN_RESOLUTION = (1280, 1024)
    BACKGROUND = (255, 255, 255)

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_RESOLUTION)

    def move(self, moving_objects: list[object], walls: pygame.mask):
        for object in moving_objects:
            object.move(walls) 

    def draw(self, drawable_objects):
        from game_loop import camera
        camera.update_camera_position()
        self.screen.fill("grey")
        for object in drawable_objects:
            object.draw(self.screen)
        pygame.display.flip() # update the window after everything is drawn


class Camera:
    def __init__(self):
        self.MOUSE_CAMERA_OFFSET_INFLUENCE = 0.5 
        self.mouse_camera_offset = [0, 0] # for the player 
        self.combined_camera_offset = [0, 0]

    def update_camera_position(self): # camera holds different offsets, so the game objects can be drawn at their correct locations
        from game_loop import player, mouse

        mouse_camera_offset_x = -mouse.centered_coordinates[0] * self.MOUSE_CAMERA_OFFSET_INFLUENCE # the mouse offset frames more of what the player is "aiming" at
        combined_camera_offset_x = -player.coordinates[0] + Screen.SCREEN_RESOLUTION[0]/2 + mouse_camera_offset_x # center the camera on player and add mouse offset

        mouse_camera_offset_y = -mouse.centered_coordinates[1] * self.MOUSE_CAMERA_OFFSET_INFLUENCE
        combined_camera_offset_y = -player.coordinates[1] + Screen.SCREEN_RESOLUTION[1]/2 + mouse_camera_offset_y

        self.mouse_camera_offset = [mouse_camera_offset_x, mouse_camera_offset_y]
        self.combined_camera_offset = [combined_camera_offset_x, combined_camera_offset_y]


class Map:
    def __init__(self): 
        self.RAW_IMAGE = pygame.image.load("./assets/map1.png").convert_alpha()
        self.SCALE_FACTOR = 30
        self.IMAGE = pygame.Surface((self.RAW_IMAGE.get_width() * self.SCALE_FACTOR, self.RAW_IMAGE.get_height() * self.SCALE_FACTOR), pygame.SRCALPHA)
        self.IMAGE = pygame.transform.scale(self.RAW_IMAGE, (self.RAW_IMAGE.get_width() * self.SCALE_FACTOR, self.RAW_IMAGE.get_height() * self.SCALE_FACTOR), self.IMAGE)
        self.MASK = pygame.mask.from_surface(self.IMAGE) # MASK is used for testing collision against player, enemy, and bullets (IMAGE draws the map separately)

    def draw(self, surface: pygame.Surface):
        from game_loop import camera
        surface.blit(self.IMAGE, camera.combined_camera_offset) # map is essentially always at (0, 0)


class MiniMap:
    def __init__(self):
        from game_loop import map, screen
        self.RAW_IMAGE = pygame.image.load("./assets/map2.png")
        self.SCALE_FACTOR = 2
        self.IMAGE = pygame.Surface((self.RAW_IMAGE.get_width() * self.SCALE_FACTOR, self.RAW_IMAGE.get_height() * self.SCALE_FACTOR))
        self.IMAGE = pygame.transform.scale(self.RAW_IMAGE, (self.RAW_IMAGE.get_width() * self.SCALE_FACTOR, self.RAW_IMAGE.get_height() * self.SCALE_FACTOR))
        self.minimap_size = (self.IMAGE.get_width(), self.IMAGE.get_height())
        self.map_size = (map.IMAGE.get_width(), map.IMAGE.get_height())
        self.draw_offset = screen.SCREEN_RESOLUTION[0] - self.minimap_size[0] # draw at the top right of the screen

        self.player_pixel = pygame.Surface((3, 3)) # a 3x3 square to represent the player
        self.player_pixel.fill((0, 255, 0)) # green
        self.enemy_pixel = pygame.Surface((3, 3))
        self.enemy_pixel.fill((255, 0, 0)) # red


    def draw(self, surface: pygame.Surface):
        from game_loop import player, enemy

        surface.blit(self.IMAGE, (self.draw_offset, 0))

        # determine where the player should be on the minimap
        player_draw_pos_x = (player.coordinates[0] / self.map_size[0]) * self.minimap_size[0] + self.draw_offset
        player_draw_pos_y = (player.coordinates[1] / self.map_size[1]) * self.minimap_size[1]
        player_draw_pos = (player_draw_pos_x, player_draw_pos_y)
        surface.blit(self.player_pixel, player_draw_pos)

        enemy_draw_pos_x = (enemy.coordinates[0] / self.map_size[0]) * self.minimap_size[0] + self.draw_offset
        enemy_draw_pos_y = (enemy.coordinates[1] / self.map_size[1]) * self.minimap_size[1]
        enemy_draw_pos = (enemy_draw_pos_x, enemy_draw_pos_y)
        surface.blit(self.enemy_pixel, enemy_draw_pos)


class Mouse:
    def __init__(self):
        self.IMAGE = pygame.image.load("./assets/crosshair.png")
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_width())
        self.DRAW_OFFSET = (self.SIZE[0]/2, self.SIZE[1]/2)
        self.centered_coordinates = [0, 0] # the center of the screen counts as (0, 0); this makes it easier to do other calculations relative to the player

    def draw(self, surface: pygame.Surface):
        from game_loop import screen
        mouse_coordinates = pygame.mouse.get_pos()
        centered_coordinates_x = mouse_coordinates[0] - screen.SCREEN_RESOLUTION[0]/2
        centered_coordinates_y = mouse_coordinates[1] - screen.SCREEN_RESOLUTION[1]/2
        self.centered_coordinates = [centered_coordinates_x, centered_coordinates_y]
        crosshair_coordinates = (mouse_coordinates[0] - self.DRAW_OFFSET[0], mouse_coordinates[1] - self.DRAW_OFFSET[1])
        surface.blit(self.IMAGE, crosshair_coordinates)


class Player:
    def __init__(self, spawn_position):
        self.hit_points = 3
        self.image = pygame.image.load("./assets/player/you3.png") # sprite with three hit points
        self.SIZE = (self.image.get_width(), self.image.get_height())
        self.SPEED_STRAIGHT = 300
        self.SPEED_DIAGONAL = 212.13 # 300 * 1/sqrt(2); ensures the player doesn't move faster when going in two directions
        self.coordinates = spawn_position
        self.hitbox = pygame.mask.from_surface(pygame.Surface((self.SIZE)))

    def move(self, walls: list):
        if self.hit_points <= 0:
            return

        from game_loop import Inputs, delta_time
        from logic import collision

        old_coordinates = self.coordinates[:] # to revert coordinates later if collision is detected
        horizontal_axis = (Inputs.keys[pygame.K_d] ^ Inputs.keys[pygame.K_a])
        vertical_axis = (Inputs.keys[pygame.K_w] ^ Inputs.keys[pygame.K_s])
        if horizontal_axis and vertical_axis:
            speed = self.SPEED_DIAGONAL
        else:
            speed = self.SPEED_STRAIGHT

        # horizontal input
        if Inputs.keys[pygame.K_d]:
            self.coordinates[0] += speed * delta_time
        if Inputs.keys[pygame.K_a]:
            self.coordinates[0] -= speed * delta_time

        # collision handling
        if collision(walls, self.hitbox, self.coordinates):
            self.coordinates = old_coordinates[:]
        else:
            old_coordinates = self.coordinates[:]

        # vertical input
        if Inputs.keys[pygame.K_s]:
            self.coordinates[1] += speed * delta_time
        if Inputs.keys[pygame.K_w]:
            self.coordinates[1] -= speed * delta_time

        # collision handling
        if collision(walls, self.hitbox, self.coordinates):
            self.coordinates = old_coordinates[:]
        else:
            old_coordinates = self.coordinates[:]

    def draw(self, surface: pygame.Surface): # player is drawn around the center of the screen, unlike other objects
        from game_loop import camera, screen
        draw_coordinates_x = screen.SCREEN_RESOLUTION[0]/2 + camera.mouse_camera_offset[0]
        draw_coordinates_y = screen.SCREEN_RESOLUTION[1]/2 + camera.mouse_camera_offset[1]
        draw_coordinates = (draw_coordinates_x, draw_coordinates_y)
        surface.blit(self.image, draw_coordinates)
    
    def hit(self): # change the sprite when the player loses hit points
        self.hit_points -= 1
        match self.hit_points:
            case 3:
                self.image = pygame.image.load("./assets/player/you3.png")
            case 2:
                self.image = pygame.image.load("./assets/player/you2.png")
            case 1:
                self.image = pygame.image.load("./assets/player/you1.png")
            case 0:
                self.image = pygame.image.load("./assets/player/you0.png")
                import sys, json
                from game_loop import running
                sys.exit(1)
                


class Gun:
    def __init__(self):
        self.VELOCITY_MULTIPLIER = 500
        self.FIRE_RATE = .5
        self.time_since_last_fire = 0.0
        self.bullets = []

    def fire(self): 
        from game_loop import delta_time, Inputs, mouse, player
        import math

        if player.hit_points <= 0:
            return

        self.time_since_last_fire += delta_time 

        # continue only if the players mouse is down AND it's been long enough since the last fire
        if Inputs.left_mouse_down == False:
            return
        if self.time_since_last_fire > self.FIRE_RATE:
            self.time_since_last_fire = 0
        else:
            return
    
        # calculate the bullet velocity using the unit circle; this ensures bullets always go the same speed, reguardless of mouse position
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
        self.fire() # create a new bullet (if applicable)

        # remove dead bullets from list
        new_bullets = [] 
        for bullet in self.bullets:
            bullet.move(walls)
            if bullet.alive == True:
                new_bullets.append(bullet)
        self.bullets = new_bullets

    def draw(self, surface: pygame.Surface): # the gun is not actually drawn, only its bullets
        for bullet in self.bullets:
            bullet.draw(surface)


class Bullet: 
    def __init__(self, coordinates: list, velocity: list):
        self.IMAGE = pygame.image.load("./assets/bullet.png")
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_height())
        self.coordinates = coordinates
        self.velocity = velocity
        self.hitbox = pygame.mask.from_surface(pygame.Surface((self.SIZE)))
        self.alive = True

    def move(self, walls):
        from logic import collision
        from game_loop import player, enemy, delta_time

        self.coordinates[0] += self.velocity[0] * delta_time
        self.coordinates[1] += self.velocity[1] * delta_time

        # test for collision against enemy
        enemy_test_x = self.coordinates[0] - enemy.coordinates[0]
        enemy_test_y = self.coordinates[1] - enemy.coordinates[1]
        try:
            if enemy.hitbox.get_at((enemy_test_x, enemy_test_y)):
                self.alive = False
                enemy.hit()
        except:
            pass

        # test for collision against walls
        if collision(walls, self.hitbox, self.coordinates):
            self.alive = False
        

    def draw(self, surface: pygame.Surface):
        from game_loop import camera
        draw_coordinates_x = self.coordinates[0] + camera.combined_camera_offset[0]
        draw_coordinates_y = self.coordinates[1] + camera.combined_camera_offset[1]
        draw_coordinates = (draw_coordinates_x, draw_coordinates_y)
        surface.blit(self.IMAGE, draw_coordinates)


class Enemy: #Enemy is almost entirely like Player, except it moves in random directions, with a lean towards the player
    def __init__(self, spawn_position):
        self.hit_points = 3
        self.IMAGE = pygame.image.load("./assets/enemy/badguy3.png") 
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_height())
        self.SPEED_STRAIGHT = 300
        self.SPEED_DIAGONAL = 212.13
        self.coordinates = spawn_position
        self.hitbox = pygame.mask.from_surface(pygame.Surface((self.SIZE)))
        self.time_since_move = 0
        self.MOVE_RATE = 1 # how often the enemy changes directions
        self.directions = [False, False, False, False, False, False, False, False, False] # direction is based off the numberpad, (ie. directions[8] is up, and directions[3] is down-right)

    def move(self, walls: list):
        if self.hit_points <= 0:
            return
        from game_loop import Inputs, delta_time, player
        from logic import collision
        import random

        self.time_since_move += delta_time
        if self.time_since_move > self.MOVE_RATE:
            self.directions = []
            self.time_since_move = 0
            for i in range(9): # randomly choose if the enemy will go in any given direction
                self.directions.append(random.choice([True, False]))
            if random.random() < 0.5: # 50% chance the enemy will move towards the player (along x axis)
                if player.coordinates[0] - self.coordinates[0] < 0:
                    self.directions[4] = True
                    self.directions[6] = False
                else:
                    self.directions[4] = False
                    self.directions[6] = True
            if random.random() < 0.5: # (along y axis)
                if player.coordinates[1] - self.coordinates[1] < 0:
                    self.directions[8] = True
                    self.directions[2] = False
                else:
                    self.directions[8] = False
                    self.directions[2] = True

        old_coordinates = self.coordinates[:]
        horizontal_axis = (self.directions[6] ^ self.directions[4])
        vertical_axis = (self.directions[8] ^ self.directions[2])
        if horizontal_axis and vertical_axis:
            speed = self.SPEED_DIAGONAL
        else:
            speed = self.SPEED_STRAIGHT



        # horizonal input
        if self.directions[6]:
            self.coordinates[0] += speed * delta_time
        if self.directions[4]:
            self.coordinates[0] -= speed * delta_time

        # collision handling
        if collision(walls, self.hitbox, self.coordinates):
            self.coordinates = old_coordinates[:]
        else:
            old_coordinates = self.coordinates[:]

        # vertical input
        if self.directions[2]:
            self.coordinates[1] += speed * delta_time
        if self.directions[8]:
            self.coordinates[1] -= speed * delta_time

        # collision handling
        if collision(walls, self.hitbox, self.coordinates):
            self.coordinates = old_coordinates[:]
        else:
            old_coordinates = self.coordinates[:]

    def draw(self, surface: pygame.Surface):
        from game_loop import camera, screen
        draw_coordinates_x = self.coordinates[0] + camera.combined_camera_offset[0]
        draw_coordinates_y = self.coordinates[1] + camera.combined_camera_offset[1]
        draw_coordinates = (draw_coordinates_x, draw_coordinates_y)
        surface.blit(self.IMAGE, draw_coordinates)

    def hit(self):
        self.hit_points -= 1
        match self.hit_points:
            case 3:
                self.IMAGE = pygame.image.load("./assets/enemy/badguy3.png")
            case 2:
                self.IMAGE = pygame.image.load("./assets/enemy/badguy2.png")
            case 1:
                self.IMAGE = pygame.image.load("./assets/enemy/badguy1.png")
            case 0:
                self.IMAGE = pygame.image.load("./assets/enemy/badguy0.png")
                import sys, json
                print("you win!!!")
                with open('scores.json', 'r') as file:
                    scores = json.load(file)
                scores['player'] += 1
                with open('data.json', 'w') as file:
                    json.dump(scores, file)
                sys.exit(2)


class EnemyGun:
    def __init__(self):
        self.VELOCITY_MULTIPLIER = 500
        self.FIRE_RATE = .5
        self.time_since_last_fire = 0.0
        self.bullets = []

    def fire(self): 
        from game_loop import delta_time, Inputs, mouse, enemy, player
        import math, random

        if enemy.hit_points <= 0:
            return

        self.time_since_last_fire += delta_time 

        if random.random() < 0.95:
            return
        if self.time_since_last_fire > self.FIRE_RATE:
            self.time_since_last_fire = 0
        else:
            return

        raw_x =  player.coordinates[0] - enemy.coordinates[0]
        raw_y =  player.coordinates[1] - enemy.coordinates[1]

        magnitude = math.sqrt(raw_x**2 + raw_y**2)
        if magnitude == 0:
            x_velocity = 0
            y_velocity = 0
        else:
            x_velocity = raw_x / magnitude * self.VELOCITY_MULTIPLIER
            y_velocity = raw_y / magnitude * self.VELOCITY_MULTIPLIER

        self.bullets.append(EnemyBullet(enemy.coordinates[:], [x_velocity, y_velocity]))

    def move(self, walls):
        self.fire()
        new_bullets = [] 
        for bullet in self.bullets:
            bullet.move(walls)
            if bullet.alive == True:
                new_bullets.append(bullet)
        self.bullets = new_bullets

    def draw(self, surface: pygame.Surface):
        for bullet in self.bullets:
            bullet.draw(surface)


class EnemyBullet: 
    def __init__(self, coordinates: list, velocity: list):
        self.IMAGE = pygame.image.load("./assets/bullet.png")
        self.SIZE = (self.IMAGE.get_width(), self.IMAGE.get_height())
        self.coordinates = coordinates
        self.velocity = velocity
        self.hitbox = pygame.mask.from_surface(pygame.Surface((self.SIZE)))
        self.alive = True

    def move(self, walls):
        from logic import collision
        from game_loop import player, enemy, delta_time
        self.coordinates[0] += self.velocity[0] * delta_time
        self.coordinates[1] += self.velocity[1] * delta_time
        
        player_test_x = self.coordinates[0] - player.coordinates[0]
        player_test_y = self.coordinates[1] - player.coordinates[1]
        try:
            if player.hitbox.get_at((player_test_x, player_test_y)):
                self.alive = False
                player.hit()
        except SystemExit:
            import sys
            sys.exit(1)
        except:
            pass

        if collision(walls, self.hitbox, self.coordinates):
            self.alive = False
        

    def draw(self, surface: pygame.Surface):
        from game_loop import camera
        draw_coordinates_x = self.coordinates[0] + camera.combined_camera_offset[0]
        draw_coordinates_y = self.coordinates[1] + camera.combined_camera_offset[1]
        draw_coordinates = (draw_coordinates_x, draw_coordinates_y)
        surface.blit(self.IMAGE, draw_coordinates)

