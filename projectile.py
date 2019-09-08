import pygame
from pygame import Vector2
from math import sin, cos, pi


class Projectile(object):

    def __init__(self, game, player):
        self.game = game

        self.speed = 10

        self.pos = Vector2(player.pos)
        self.mid_pos = Vector2(player.pos)
        self.last_pos = Vector2(player.pos)
        rad_ang = player.angle * pi / 180
        self.vel = Vector2(self.speed * sin(rad_ang), self.speed * cos(rad_ang))

    def tick(self):
        self.last_pos = Vector2(self.mid_pos)
        self.mid_pos = Vector2(self.pos)
        self.pos += Vector2(self.vel)
        # print(self.pos, self.last_pos, self.vel)

        win_size = self.game.screen.get_size()
        if self.pos.x > 5 + win_size[0] or self.pos.x < -5:
            return 0
        if self.pos.y > 5 + win_size[1] or self.pos.y < -5:
            return 0

        return 1
    
    def draw(self):
        pygame.draw.line(self.game.screen, (0, 0, 255), self.pos, self.last_pos, 4)
