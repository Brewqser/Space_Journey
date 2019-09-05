import pygame
from pygame import Vector2


class Player(object):

    def __init__(self, game):
        self.game = game
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

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

        self.pos.x %= self.game.window_width
        self.pos.y %= self.game.window_height

        print(self.vel)

    def draw(self):
        rec = pygame.Rect(self.pos.x, self.pos.y, 50, 50)
        pygame.draw.rect(self.game.screen, (250, 250, 0), rec)
