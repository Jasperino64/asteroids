import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        # split the asteroid into two smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius / 2
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        angle = random.uniform(20, 50)
        a1.velocity = self.velocity.rotate(angle)
        a2.velocity = self.velocity.rotate(-angle)