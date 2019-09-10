import pygame
import sys
from pygame import Vector2
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

        self.asteroid_spawn = 60  # asteroida co 60 tick
        self.asteroid_spawn_count = 58

        self.score = 0
        self.font = pygame.font.SysFont("comicsansms", 72)

        self.running = True
        while self.running:

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
        for asteroid in self.asteroids:
            if not asteroid.tick():
                self.asteroids.remove(asteroid)

        for projectile in self.projectiles:
            if not projectile.tick():
                self.projectiles.remove(projectile)

        for asteroid in self.asteroids:
            if self.running:
                self.running = not asteroid.collision1(self.player)

        for asteroid in self.asteroids:
            for projectile in self.projectiles:
                if asteroid.collision2(projectile):
                    if asteroid.size >= 30:
                        self.score += 1
                        self.asteroids.append(Asteroid(self, 1, False, Vector2(asteroid.pos), asteroid.size / 2))
                        self.asteroids.append(Asteroid(self, 1, False, Vector2(asteroid.pos), asteroid.size / 2))
                    self.asteroids.remove(asteroid)
                    self.projectiles.remove(projectile)

        print(len(self.asteroids))

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        self.player.draw()

        text = self.font.render(str(self.score), True, (0, 128, 0))
        self.screen.blit(text, (0, 0))