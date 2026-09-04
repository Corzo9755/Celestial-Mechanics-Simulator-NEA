import pygame
import sys

#Must initialise pygame whenever it is used at the start
pygame.init()

def create_window(name):
    #Sets the dimensions of the window to pop up and adds a caption to it
    WIDTH = 1280
    HEIGHT = 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(name)
    return screen, WIDTH, HEIGHT

screen, WIDTH, HEIGHT = create_window("screen.py")

#Game loop needed to ensure the screen will only close when user requests
active = True
while active:
    #If the user presses the exit button it escapes the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    #Fills the entire screen with the chosen colour using its RGB code, black here
    screen.fill((0,0,0))

#Quits all the pygame modules and then sys terminates the python program
pygame.quit()
sys.exit()
