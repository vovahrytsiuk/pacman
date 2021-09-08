import pygame

class Spirit(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, d_x, d_y):
        pygame.sprite.Sprite.__init__(self)
        # set direction of movement
        self.d_x = d_x
        self.d_y = d_y
        # upload sprite
        self.image = pygame.image.load("spirit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft(start_x, start_y)