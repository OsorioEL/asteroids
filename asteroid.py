import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # Draw asteroid using pygame.draw.circle with position, radius and width 2 
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            vector1_radius = self.radius - ASTEROID_MIN_RADIUS
            vector2_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y,vector1_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y,vector2_radius)
            asteroid1.velocity = new_vector1*1.2
            asteroid2.velocity = new_vector2*1.2