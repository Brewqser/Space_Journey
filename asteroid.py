import pygame
from pygame import Vector2


class Asteroid(object):

    def __init__(self, game):
        self.game = game

        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.angle = 0

    def tic(self):
        pass

    def draw(self):
        pass
