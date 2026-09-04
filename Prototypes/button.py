#Button prototype success
import pygame
import sys
import math

pygame.init()

HEIGHT = 800
WIDTH = 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("button.py")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y, colour):   #Instantiates the parent class
        self.x = x
        self.y = y
        self.colour = colour

    def set_colour(self, colour):    #Universal method for both subclasses
        self.colour = colour

class CircleButton(Button):
    def __init__(self, x, y, radius, colour):
        super().__init__(x, y, colour)
        self.radius = radius     #Only extra value the circle subclass needs is radius

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

    def is_clicked(self, mouse_pos):   #Same logic as collision detection but with mouse and button
        distance = math.hypot(mouse_pos[0] - self.x, mouse_pos[1] - self.y)
        if distance <= self.radius:
            return True
        return False

class RectangleButton(Button):
    def __init__(self, x, y, width, height, colour):
        super().__init__(x, y, colour)
        self.width = width    #Needs both height and width additionally
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

    def is_clicked(self, mouse_pos):  #Creates a rectangle using pygame in built function
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if rect.collidepoint(mouse_pos):   #Collidepoint function determines if parameter coord in rectangle
            return True
        return False


colourChange1 = RED
colourChange2 = RED
active = True
Button1 = CircleButton(WIDTH //2 - 150, HEIGHT //2, 50, BLUE)
Button2 = RectangleButton(WIDTH //2 + 150, HEIGHT //2 - 35, 125, 75, GREEN)
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:  #Only does the collision test on click
            if Button1_clicked:
                Button1.set_colour(colourChange1)
                if colourChange1 == RED:
                    colourChange1 = BLUE
                else:
                    colourChange1 = RED
            elif Button2_clicked:
                Button2.set_colour(colourChange2)
                if colourChange2 == RED:
                    colourChange2 = GREEN
                else:
                    colourChange2 = RED

    screen.fill((0,0,0))
    
    Button1.draw()
    Button2.draw()
    pygame.display.flip()
    
    Button1_clicked = Button1.is_clicked(pygame.mouse.get_pos())
    Button2_clicked = Button2.is_clicked(pygame.mouse.get_pos())

    clock.tick(60)

pygame.quit()
sys.exit()