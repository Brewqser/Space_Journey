import pygame
from pygame import Vector2
from math import sin, cos, pi


class Player(object):

    def __init__(self, game):
        self.game = game

        win_size = self.game.screen.get_size()
        self.pos = Vector2(win_size[0] / 2, win_size[1] / 2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.angle = 180

        print(self.pos)
        self.speed = 0.55
        self.drag = 0.98

    def add_force(self, force):
        self.acc += force

    def tick(self):

        # Input
        rot = 5
        rad_ang = self.angle * pi / 180

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(self.speed * sin(rad_ang), self.speed * cos(rad_ang)))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(-0.35 * self.speed * sin(rad_ang), -0.35 * self.speed * cos(rad_ang)))
        if pressed[pygame.K_a]:
            self.angle += rot
        if pressed[pygame.K_d]:
            self.angle -= rot

        self.angle %= 360

        # Physic
        self.vel *= self.drag

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        win_size = self.game.screen.get_size()
        self.pos.x %= win_size[0]
        self.pos.y %= win_size[1]

    def draw(self):
        # Player
        points = [Vector2(0, -10), Vector2(5, 5), Vector2(0, 2), Vector2(-5, 5)]

        # Rotation
        points = [p.rotate(self.angle) for p in points]
        points = [Vector2(p.x, p.y * -1) for p in points]

        # Update position
        points = [self.pos + p * 2 for p in points]
        pygame.draw.polygon(self.game.screen, (250, 0, 0), points)
