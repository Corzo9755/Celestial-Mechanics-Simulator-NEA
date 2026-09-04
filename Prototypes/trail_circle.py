import pygame
import sys
import math

pygame.init()
HEIGHT = 800
WIDTH = 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("trail_circle.py")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

radius = 300
speed = 0.02
angle = 0
x_pos = WIDTH // 2
y_pos = HEIGHT // 2
max_len_trail= 150
trail = []

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    x = x_pos + radius * math.cos(angle)
    y = y_pos + radius * math.sin(angle)

    
    trail.append((x,y))
    if len(trail) > max_len_trail:
        trail.pop(0)

    screen.fill((0,0,0))

    for i in range (1, len(trail)):
        pygame.draw.line(screen, RED, trail[i-1], trail[i], 2)
    
    pygame.draw.circle(screen, BLUE, (int(x), int(y)), 25)
    pygame.display.flip()

    angle = angle + speed

    clock.tick(60)
pygame.quit()
sys.exit()