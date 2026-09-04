import pygame
import sys

from physics_engine.vector import Vector
from physics_engine.celestial_body import CelestialBody
from physics_engine.simulation import Simulation
from rendering.render import draw_body

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Celestial Mechanics Simulator")
clock = pygame.time.Clock()

BG_COLOUR = (0, 0, 10)

#Set up simulation with two bodies
sim = Simulation()
sim.bodies.append(CelestialBody(400, 400, mass=8000, radius=30))  # heavier
sim.bodies.append(CelestialBody(800, 400, mass=200, radius=12))   # lighter

body_colours = [(255, 200, 50), (100, 180, 255)]  #one colour per body, matched by index

dt = 0.5  #simulation time step

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    sim.step(dt)

    screen.fill(BG_COLOUR)
    for body, colour in zip(sim.bodies, body_colours):
        draw_body(screen, body, colour)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()