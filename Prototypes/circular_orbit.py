#SUCCESS circcle orbiting other circle
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

#Initialises the pygame clock
clock = pygame.time.Clock()

angle = 0   #Angle that the circle will be rotating at in radians 
speed = 0.05  #Initial rate at which the angle will increase and thus speed of travel
radius = 200  #Radius of circle acting as an orbit
x_centre = WIDTH // 2   #Centre of circle acting as orbit
y_centre = HEIGHT // 2

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.fill(BLACK)  #Clear the screen with black

    #Calculate the position of the orbiting object
    x = x_centre + radius * math.cos(angle)
    y = y_centre + radius * math.sin(angle)

    #Drawing the orbiting object
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 15)

    #Drawing the circle acting as an orbit
    pygame.draw.circle(screen, WHITE, (x_centre, y_centre), radius, 1)

    #Update the angle each frame
    angle = angle + speed
    pygame.display.flip()

    #Limit Frame Rate to 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()