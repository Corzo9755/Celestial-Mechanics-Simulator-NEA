import pygame
import sys
import math

pygame.init()

#Set up the display window with width and height dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection Prototype")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, colour):
        pygame.draw.circle(screen, colour, (int(self.x), int(self.y)), self.radius)

    def get_position(self):
        return (self.x, self.y)

    def get_radius(self):
        




def collision_detection(circle1, circle2):
    distance = math.hypot(circle1.x - circle2.x, circle1.y - circle2.y)
    return distance < (circle1.radius + circle2.radius)





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