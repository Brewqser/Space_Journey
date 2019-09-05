import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
rec = pygame.Rect(10, 10, 50, 50)
clock = pygame.time.Clock()
dt = 0.0
tps = 60.0
vel = 10

while True:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # Tick
    dt += clock.tick()/1000.0

    while dt > 1 / tps:
        dt -= 1 / tps

        # Inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            rec.y -= vel
        if keys[pygame.K_s]:
            rec.y += vel
        if keys[pygame.K_a]:
            rec.x -= vel
        if keys[pygame.K_d]:
            rec.x += vel

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (250, 250, 0), rec)
    pygame.display.flip()
