import pygame
from animation import *
from config import *



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed = 4):
        # Call super class initializer
        pygame.sprite.Sprite.__init__(self)
        # Load sprite from file
        self.image = pygame.image.load("images/pacman.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

        # Load animation image
        walk_image = pygame.image.load("images/walk.png").convert()
        self.right_animation = Animation(walk_image, BLOCK_SIZE, BLOCK_SIZE)
        self.left_animation = Animation(pygame.transform.flip(walk_image, True, False), BLOCK_SIZE, BLOCK_SIZE)
        self.up_animation = Animation(pygame.transform.rotate(walk_image, 90), BLOCK_SIZE, BLOCK_SIZE)
        self.down_animation = Animation(pygame.transform.rotate(walk_image, 270), BLOCK_SIZE, BLOCK_SIZE)
        self.pacman_image = pygame.image.load("images/pacman.png").convert()
        self.pacman_image.set_colorkey(BLACK)
        self.d_x = 0
        self.d_y = 0

        self.bang = False
        self.game_over = False

    def step_in_extreme_positions(self):
        # transition to extreme positions
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0

    def animation(self):
        # start animation
        if self.d_x > 0:
            self.right_animation.animate(ANIMATION_SPEED)
            self.image = self.right_animation.get_current_image()
        elif self.d_x < 0:
            self.left_animation.animate(ANIMATION_SPEED)
            self.image = self.left_animation.get_current_image()
        if self.d_y > 0:
            self.down_animation.animate(ANIMATION_SPEED)
            self.image = self.down_animation.get_current_image()
        elif self.d_y < 0:
            self.up_animation.animate(ANIMATION_SPEED)
            self.image = self.up_animation.get_current_image()

    def move(self, horizontal_roads, vertical_roads):
        if not self.bang:

            self.step_in_extreme_positions()
            for _ in pygame.sprite.spritecollide(self, horizontal_roads, False):
                self.d_y = 0
            for _ in pygame.sprite.spritecollide(self, vertical_roads, False):
                self.d_x = 0
            self.rect.x += self.d_x
            self.rect.y += self.d_y
            self.animation()

    def move_right(self):
        self.d_x = self.speed

    def move_left(self):
        self.d_x = -self.speed

    def move_up(self):
        self.d_y = -self.speed

    def move_down(self):
        self.d_y = self.speed

    def stop_move_right(self):
        if self.d_x != 0:
            self.image = self.pacman_image
        self.d_x = 0

    def stop_move_left(self):
        if self.d_x != 0:
            self.image = pygame.transform.flip(self.pacman_image, True, False)
        self.d_x = 0

    def stop_move_up(self):
        if self.d_y != 0:
            self.image = pygame.transform.rotate(self.pacman_image, 90)
        self.d_y = 0

    def stop_move_down(self):
        if self.d_y != 0:
            self.image = pygame.transform.rotate(self.pacman_image, 270)
        self.d_y = 0




