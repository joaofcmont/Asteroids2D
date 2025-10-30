import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(60) / 1000  # delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        updatables.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
