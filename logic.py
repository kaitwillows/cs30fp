import pygame
def collision(walls: list[pygame.Mask], hitbox, coordinates) -> bool:
    collision = False
    for wall in walls:
        if wall.MASK.overlap(hitbox, coordinates): 
            collision = True
    return collision