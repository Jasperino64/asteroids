import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    
    pygame.display.set_caption("Asteroids")
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display
        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()