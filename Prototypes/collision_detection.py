#SUCCESS Prototype detects collision between two circles
import pygame
import sys
import math

pygame.init()

#Set up the display window with width and height dimensions
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection Prototype")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Circle:
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour

    def draw(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.radius)

    def get_position(self):
        return (self.x, self.y)

    def get_radius(self):
        return self.radius

    def set_colour(self, colour):
        self.colour = colour

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


#Function that calculates if the circles are touching by measuring their radii and position
def collision_detection(circle1, circle2):
    circle1_x = circle1.get_position()[0]
    circle1_y = circle1.get_position()[1]
    circle2_x = circle2.get_position()[0]
    circle2_y = circle2.get_position()[1]
    circle1_radius = circle1.get_radius()
    circle2_radius = circle2.get_radius()
    distance = math.hypot(circle1_x - circle2_x, circle1_y - circle2_y)  #Calculates the distance inbetween the 2 centres
    if distance < (circle1_radius + circle2_radius):  #If the distance is smaller than both radii combined then collision true
        return True
    else:
        return False


circle1 = Circle(WIDTH // 2 - 300, HEIGHT // 2, 100, GREEN)
circle2 = Circle(WIDTH // 2 + 300, HEIGHT // 2, 100, BLUE)

#Window will run as long as active is True, and when close button pressed window closed
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.fill((0, 0, 0))
    circle1.draw()
    circle2.draw()

    if collision_detection(circle1, circle2) == True:
        circle1.colour = RED
        circle2.colour = RED

    x1, y1 = circle1.get_position()
    x2, y2 = circle2.get_position()
    circle1.move(x1 + 1, y1)
    circle2.move(x2 - 1, y2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()