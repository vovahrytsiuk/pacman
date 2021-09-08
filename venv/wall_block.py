import pygame

class WallBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        # Super class initialization
        pygame.sprite.Sprite.__init__(self)
        # Make this block colorful
        # to do: use sprite image
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Fetch color rect
        self.rect = self.image.get_rect()
        self.rect.topleft(x, y)
