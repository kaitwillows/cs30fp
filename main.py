import pygame

# idk this is all just copy and pasted from the pygame docs

pygame.init()
screen = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()