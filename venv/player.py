import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, file_path, move_animation_file):
        # Call super class initializer
        pygame.sprite.Sprite.__init__(self)
        # Load sprite from file
        self.image = pygame.image.load(file_path).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft(x, y)

        # Load animation image
        animation_image = pygame.image.load(move_animation_file)
        # Create animations for this object
