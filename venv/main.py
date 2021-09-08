import pygame

# config
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TITLE = "PACMAN"

def main():
    # Initialize pygame
    pygame.init()
    # Create screen
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set window title
    pygame.display.set_caption(TITLE)
    # Is game in progress
    is_in_progress = True
    pygame.display.flip()
    # Main game loop
    while is_in_progress:
        pass
    # quit when user press quit button
    pygame.quit()

if __name__ == "__main__":
    main()