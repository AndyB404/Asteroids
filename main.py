import pygame
import sys
from constants import *
from player import Player
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    play_game = True
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
#groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
#auto-add every instance of these classes to their groups on construction.
    AsteroidField.containers = (updatables)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField()
    player = Player(x, y)
    print("Starting Asteroids!")
#game loop
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(dt)
        for a in asteroids:
            if player.collision(a):
                print("Game over!")
                sys.exit()
        for s in drawables:
                s.draw(screen)
        pygame.display.flip()
#fps limit
        tick_rate = clock.tick(60)
        dt = tick_rate / 1000


    


if __name__ == "__main__":
    main()
