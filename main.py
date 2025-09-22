# Groups & flow:
# - Player.containers = (updatables, drawables)  # sets which groups a new Player() joins
# - Player(x, y) -> CircleShape.__init__ adds to those groups and sets position
# - Game loop:
#     updatables.update(dt)      # calls each sprite.update(dt)
#     for s in drawables: s.draw(screen)

import pygame
from constants import *
from player import Player

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
# Player.containers: auto-add new Player() to these groups on construction
    Player.containers = (updatables, drawables)
    player = Player(x, y)
    print("Starting Asteroids!")
#game loop
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatables.update(dt)
        for s in drawables:
                s.draw(screen)
        pygame.display.flip()
#fps limit
        tick_rate = clock.tick(60)
        dt = tick_rate / 1000


    


if __name__ == "__main__":
    main()
