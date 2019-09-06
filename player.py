import pygame
from pygame import Vector2


class Player(object):

    def __init__(self, game):
        self.game = game

        win_size = self.game.screen.get_size()
        self.pos = Vector2(win_size[0] / 2, win_size[1] / 2)
        self.vel = Vector2(0, -0.01)  # Starting vel set to - 0.01 for right beginning angle
        self.acc = Vector2(0, 0)

        print(self.pos)
        self.speed = 1
        self.drag = 0.98

    def add_force(self, force):
        self.acc += force

    def tick(self):

        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))

        # Physic
        self.vel *= self.drag

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        win_size = self.game.screen.get_size()
        self.pos.x %= win_size[0]
        self.pos.y %= win_size[1]

        # print(self.vel)

    def draw(self):
        # Player
        points = [Vector2(0, -10), Vector2(5, 5), Vector2(0, 2), Vector2(-5, 5)]

        # Rotation
        angle = self.vel.angle_to(Vector2(0, 1))
        points = [p.rotate(angle) for p in points]
        points = [Vector2(p.x, p.y * -1) for p in points]

        # Update position
        points = [self.pos + p * 2 for p in points]
        pygame.draw.polygon(self.game.screen, (250, 0, 0), points)
