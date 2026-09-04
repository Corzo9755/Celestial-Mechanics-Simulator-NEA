#Prototype creates a circle and then a sphere which will be used to model the bodies
import pygame
import sys

pygame.init()

#Set up the display window with width and height dimensions
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("body_creation.py")

WHITE = (255, 255, 255)


#Window will run as long as active is True, and when close button pressed window closed
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    pygame.draw.circle(screen, WHITE, (WIDTH //2, HEIGHT // 2), 100)
    pygame.display.flip()

pygame.quit()
sys.exit()