import pygame
import random
from pygame import Vector2
from math import sin, cos, pi
import numpy as np


def make_points(size):

    poi = [Vector2(cos(a/2) * size, sin(a/2) * size) for a in range(0, 12, 1)]
    poi = [p + Vector2(random.randint(-7, 7), random.randint(-7, 7)) for p in poi]
    return poi


def make_vel(max_vel):
    angle = random.randint(0, 719)
    rad_ang = angle * pi / 180
    print(rad_ang)

    vel = Vector2(max_vel * sin(rad_ang), max_vel * cos(rad_ang))
    return vel


def make_pos(vel,win_size):
    if vel.x >= 0 and vel.y >= 0:
        if random.randint(0, 1):
            pos = Vector2(0, random.randint(0, win_size[1]))
        else:
            pos = Vector2(random.randint(0, win_size[0]), 0)
    if vel.x < 0 and vel.y >= 0:
        if random.randint(0, 1):
            pos = Vector2(win_size[0], random.randint(0, win_size[1]))
        else:
            pos = Vector2(random.randint(0, win_size[0]), 0)
    if vel.x >= 0 and vel.y < 0:
        if random.randint(0, 1):
            pos = Vector2(0, random.randint(0, win_size[1]))
        else:
            pos = Vector2(random.randint(0, win_size[0]), win_size[1])
    if vel.x < 0 and vel.y < 0:
        if random.randint(0, 1):
            pos = Vector2(win_size[0], random.randint(0, win_size[1]))
        else:
            pos = Vector2(random.randint(0, win_size[0]), win_size[1])

    return pos


class Asteroid(object):

    def __init__(self, game, max_vel, new=True, pos=Vector2(0, 0), size=0):
        self.game = game

        win_size = self.game.screen.get_size()

        # Asteroid Data
        if new:
            self.size = random.randint(3, 5) * 10
            self.points = make_points(self.size)
            self.vel = make_vel(max_vel)
            self.pos = make_pos(self.vel, win_size)
            self.angle = 0
            self.rot = random.randint(-1, 1)
        else:
            self.size = size
            self.points = make_points(self.size)
            self.vel = make_vel(max_vel * 2)
            self.pos = pos
            self.angle = 0
            self.rot = random.randint(-1, 1)

    def tick(self):

        # Physic
        print(self.vel)
        self.pos += self.vel
        self.angle += self.rot

        win_size = self.game.screen.get_size()
        if self.pos.x > 100 + win_size[0] or self.pos.x < -100:
            return 0
        if self.pos.y > 100 + win_size[1] or self.pos.y < -100:
            return 0

        return 1

    def draw(self):
        poi = self.points

        # Rotation
        poi = [p.rotate(self.angle) for p in poi]
        poi = [Vector2(p.x, p.y * -1) for p in poi]

        # Update position
        poi = [self.pos + p for p in poi]

        pygame.draw.polygon(self.game.screen, (255, 255, 255), poi)

    def collision1(self, player):
        tmp = Vector2(self.pos - player.pos).magnitude()
        if int(tmp) < self.size:
            return True
        return False

    def collision2(self, projectile):
        tmp = Vector2(self.pos - projectile.pos).magnitude()
        if int(tmp) < self.size:
            return True
        return False
