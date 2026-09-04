#SUCCESS orbiting circle in an elliptical orbit
import pygame 
import sys
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Set up the display window with width and height dimensions
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("orbit.py")

clock = pygame.time.Clock()

angle = 0 
speed = 0.05
x_radius = 200
y_radius = 100
x_centre = WIDTH // 2
y_centre = HEIGHT // 2

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.fill(BLACK)  # Clear the screen with black

    # Calculate the position of the orbiting object
    x = x_centre + x_radius * math.cos(angle)
    y = y_centre + y_radius * math.sin(angle)

    # Draw the orbiting object
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 10)
    pygame.draw.ellipse(screen, WHITE, (x_centre - x_radius, y_centre - y_radius, 2 * x_radius, 2 * y_radius), 1)

    # Update the angle each frame
    angle = angle + speed
    pygame.display.flip()

    # Limit Frame Rate to 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()