import pygame
from circleshape import CircleShape   
from constants import * 

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x,y,SHOT_RADIUS)
    
    def draw(self, screen):
        # Draw asteroid using pygame.draw.circle with position, radius and width 2 
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), SHOT_RADIUS, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt   