import pygame
import random
from pygame import Vector2
from math import sin, cos, pi
import numpy as np


def make_points():
    size = random.randint(3, 5) * 10
    poi = [Vector2(cos(a/2) * size, sin(a/2) * size) for a in range(0, 12, 1)]
    poi = [p + Vector2(random.randint(-7, 7), random.randint(-7, 7)) for p in poi]
    return poi


def make_vel(max_vel):
    angle = random.randint(0,359)
    rad_ang = angle * pi / 180

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

    def __init__(self, game,max_vel):
        self.game = game

        win_size = self.game.screen.get_size()

        # Asteroid Data
        self.points = make_points()
        self.vel = make_vel(max_vel)
        self.pos = make_pos(self.vel, win_size)
        self.angle = 0
        self.rot = random.randint(-1, 1)

    def tic(self):

        # Physic
        self.pos += self.vel
        self.angle += self.rot

    def draw(self):
        poi = self.points

        # Rotation
        poi = [p.rotate(self.angle) for p in poi]
        poi = [Vector2(p.x, p.y * -1) for p in poi]

        # Update position
        poi = [self.pos + p for p in poi]

        pygame.draw.polygon(self.game.screen, (255, 255, 255), poi)
