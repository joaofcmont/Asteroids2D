import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def draw_health_bar(screen, x, y, health, max_health):
        BAR_WIDTH = 200
        BAR_HEIGHT = 20
        fill = (health / max_health) * BAR_WIDTH
        pygame.draw.rect(screen, (255, 0, 0), (x, y, BAR_WIDTH, BAR_HEIGHT))
        pygame.draw.rect(screen, (0, 255, 0), (x, y, fill, BAR_HEIGHT))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, BAR_WIDTH, BAR_HEIGHT), 2)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                asteroid.split()
                if player.damage_cooldown <= 0 and not player.is_dead():
                    player.take_damage()
                    player.damage_cooldown = 1.0  # 1 second of invulnerability
                    if player.is_dead():
                        print("Game over!")
                        sys.exit()


            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        draw_health_bar(screen, 10, 10, player.health, PLAYER_HEALTH)

        for obj in drawable:
            obj.draw(screen)       

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
