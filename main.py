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
    player = Player(x, y)
    print("Starting Asteroids!")
    while play_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
#fps counter
        #current_fps = clock.get_fps()
        #print(f"FPS: {current_fps:.0f}")
#fps limit
        tick_rate = clock.tick(60)
        dt = tick_rate / 1000


    


if __name__ == "__main__":
    main()
