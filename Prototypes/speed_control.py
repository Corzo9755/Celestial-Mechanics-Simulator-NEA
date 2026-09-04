import pygame
import sys

pygame.init()

HEIGHT = 800
WIDTH = 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("speed_control.py")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
position = WIDTH // 2 - 50
speed = 0.2

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.fill((0,0,0))

    rectangle = pygame.Rect(position, HEIGHT // 2 - 25, 100, 50)
    pygame.draw.rect(screen, RED, rectangle)

    pygame.display.flip()

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        speed = speed - 0.2
    if keys[pygame.K_RIGHT]:
        speed = speed + 0.2

    position = position + speed

    clock.tick(60)
pygame.quit()
sys.exit()