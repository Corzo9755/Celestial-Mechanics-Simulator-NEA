import pygame

def draw_body(surface, body, colour):
    x, y = int(body.position.x), int(body.position.y)
    radius = int(body.radius)

    for i in range(radius, 0, -1):
        fade = i / radius
        r = min(255, int(colour[0] + (255 - colour[0]) * (1 - fade) * 0.6))
        g = min(255, int(colour[1] + (255 - colour[1]) * (1 - fade) * 0.6))
        b = min(255, int(colour[2] + (255 - colour[2]) * (1 - fade) * 0.6))
        offset = int((radius - i) * 0.3)
        pygame.draw.circle(surface, (r, g, b), (x - offset, y - offset), i)