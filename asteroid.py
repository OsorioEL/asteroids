import pygame
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
        