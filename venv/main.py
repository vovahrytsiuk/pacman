import pygame
from game import Game
from config import *



def main():
    # Initialize pygame
    pygame.init()
    # Create screen
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set window title
    pygame.display.set_caption(TITLE)
    # Is game in progress
    is_in_progress = True
    # for control fps
    clock = pygame.time.Clock()
    game = Game()

    # Main game loop
    while is_in_progress:
        is_in_progress = game.process_events()
        game.game_logic()
        game.display_game(window)
        clock.tick(30)
    # quit when user press quit button
    pygame.quit()

if __name__ == "__main__":
    main()