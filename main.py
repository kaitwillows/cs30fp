# btw this is all copy/pasted from the pygame docs its not plagerism!!

# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screenRes = (1280, 720)
screen = pygame.display.set_mode(screenRes)

clock = pygame.time.Clock()
running = True
dt = 0

camera = (0, 0)


character = pygame.image.load('./assets/ralsei.png')
# character = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))

pygame.event.set_grab(True)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # charX = screenRes[0]*.2 - pygame.mouse.get_pos()[0]*.1
    # charY = screenRes[1]*.2 - pygame.mouse.get_pos()[1]*.1
    charX = screenRes[0]/2 - (pygame.mouse.get_pos()[0] - screenRes[0]/2)*.5
    charY = screenRes[1]/2 - (pygame.mouse.get_pos()[1] - screenRes[1]/2)*.5
    print(f"x: {charX}, y: {charY}")
    
    charPos = (charX, charY) 
    screen.blit(character, charPos)

    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    '''

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()