# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import PLAYER
from shots import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init() 
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  # create a clock object
  clock = pygame.time.Clock()
  dt = 0
  
  # create two groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  
  # create group for asteroids
  asteroids = pygame.sprite.Group()
  
  # create group for shots
  shots = pygame.sprite.Group()
  
  PLAYER.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  Shot.containers = (shots, updatable, drawable)
  
  # instantiate the player
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = PLAYER(x, y)
  
  # Instantiate the asteroid field
  asteroid_field = AsteroidField()

  # main game loop
  # this loop will run until the game is closed
  # it will run at 60 frames per second
  while True:
    updatable.update(dt) # update all objects in the updatable group
    for asteroid in asteroids:
      if player.collision(asteroid):
        sys.exit("Game Over!")
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen,(0,0,0)) # Fill screen
   
   # Collision Check for shots and asteroids
    for asteroid in asteroids:
      for shot in shots:
        if shot.collision(asteroid):
          asteroid.split()
          shot.kill()  
    # loop through all objects in the drawable group
    for obj in drawable:
      obj.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)/1000 # dt is the time since the last frame in seconds

if __name__ == "__main__":
  main()
