import pygame
import sys
from player import Player


class Game(object):

    def __init__(self):

        # Config
        self.tps = 60.0

        # Init
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_dt = 0.0

        self.player = Player(self)

        while True:

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Tick
            self.tps_dt += self.tps_clock.tick() / 1000.0

            while self.tps_dt > 1 / self.tps:
                self.tps_dt -= 1 / self.tps
                self.tick()

            # Render
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        pass

    def draw(self):
        self.player.draw()

