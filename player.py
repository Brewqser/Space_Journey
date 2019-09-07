import pygame
from pygame import Vector2
from math import sin, cos, pi


class Player(object):

    def __init__(self, game):
        self.game = game

        win_size = self.game.screen.get_size()

        #Player
        self.points = [Vector2(0, -20), Vector2(10, 10), Vector2(0, 4), Vector2(-10, 10)]
        self.pos = Vector2(win_size[0] / 2, win_size[1] / 2)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.angle = 180

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

        poi = self.points

        # Rotation
        poi = [p.rotate(self.angle) for p in poi]
        poi = [Vector2(p.x, p.y * -1) for p in poi]

        # Update position
        poi = [self.pos + p for p in poi]

        pygame.draw.polygon(self.game.screen, (250, 0, 0), poi)
