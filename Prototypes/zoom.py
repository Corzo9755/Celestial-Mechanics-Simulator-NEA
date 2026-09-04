import pygame
import sys

pygame.init()
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("scroll.py")
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
base_radius = 25

min_scale = 0.5
max_scale = 5
scale = 1

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                scale = scale + 0.1
            elif event.y < 0:
                scale = scale - 0.1
            
    scale = max(min_scale, min(max_scale, scale))
    radius = int(base_radius * scale)

    screen.fill((0,0,0))
    pygame.draw.circle(screen, BLUE, (WIDTH // 2, HEIGHT // 2), radius)
    pygame.display.flip()

pygame.quit()
sys.exit()

    

