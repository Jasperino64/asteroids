import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    
    pygame.display.set_caption("Asteroids")
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = shots, updatable, drawable

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Gama over!")
                sys.exit()
            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))  # Fill the screen with black

        for sprite in drawable:
            sprite.draw(screen)
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000
        pygame.display.flip()  # Update the display


if __name__ == "__main__":
    main()