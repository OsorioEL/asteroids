# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import PLAYER

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
  
  PLAYER.containers = (updatable, drawable)
  
  #instnciate the player
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  player = PLAYER(x, y)

  # main game loop
  # this loop will run until the game is closed
  # it will run at 60 frames per second
  while True:
    updatable.update(dt) # update all objects in the updatable group
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    pygame.Surface.fill(screen,(0,0,0)) # Fill screen
    # loop through all objects in the drawable group
    for obj in drawable:
      obj.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)/1000 # dt is the time since the last frame in seconds

if __name__ == "__main__":
  main()
