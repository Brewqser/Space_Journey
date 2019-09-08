import pygame
import sys
from player import Player
from asteroid import Asteroid
from projectile import Projectile


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
        self.projectiles = []
        self.asteroids = []

        self.asteroid_spawn = 60 # asteroida co 60 tick
        self.asteroid_spawn_count =59 # zmienić !!!!!
        while True:

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.projectiles.append(Projectile(self, self.player))

            # Tick
            self.tps_dt += self.tps_clock.tick() / 1000.0

            while self.tps_dt > 1 / self.tps:
                self.tps_dt -= 1 / self.tps
                self.tick()
                self.asteroid_spawn_count += 1
                if self.asteroid_spawn_count == 60:
                    self.asteroid_spawn_count = 0
                    self.asteroids.append(Asteroid(self, 1))

            # Render
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        self.player.tick()
        # self.asteroid.tic()
        a = 0
        b = 0
        for asteroid in self.asteroids:
            a += 1
            if not asteroid.tick():
                self.asteroids.remove(asteroid)

        for projectile in self.projectiles:
            b += 1
            if not projectile.tick():
                self.projectiles.remove(projectile)

        print(a, b)

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        self.player.draw()


