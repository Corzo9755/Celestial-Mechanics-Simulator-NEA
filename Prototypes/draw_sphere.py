import pygame
import sys

pygame.init()
HEIGHT = 800
WIDTH = 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("draw_sphere.py")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
UNKOWN = (10, 150, 255)

clock = pygame.time.Clock()

def draw_sphere(surface, centre, radius, colour):
    x, y = centre
    #Draws many circles inside each other starting from full radius (80) going down by 1 each time
    for i in range(radius, 0, -1):
        fade = i / radius   #Just a measurement of how close to the full circle size the circle is
        #Turns each smaller circle lighter and lighter in colour changing 1 colour channel at a time
        r_new = min(255, int(colour[0] + (255 - colour[0]) * (1 - fade) * 0.6))
        g_new = min(255, int(colour[1] + (255 - colour[1]) * (1 - fade) * 0.6))
        b_new = min(255, int(colour[2] + (255 - colour[2]) * (1 - fade) * 0.6))
        new_colour = (r_new, g_new, b_new)  #Joins the 3 new colour values into 1 new_colour
        offset = int((radius - i) * 0.3)  #Shifts each circle slightly towardss a corner to give the shading effect
        pygame.draw.circle(surface, new_colour, (x - offset, y - offset), i)

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.fill((0,0,0))
    draw_sphere(screen, (WIDTH //2, HEIGHT //2), 80, UNKOWN)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()