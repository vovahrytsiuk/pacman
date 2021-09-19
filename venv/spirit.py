import pygame
from config import *
import random

class Spirit(pygame.sprite.Sprite):
    d_x = 0
    d_y = 0

    def __init__(self, start_x, start_y, field, speed = 2):
        pygame.sprite.Sprite.__init__(self)
        self.field = field
        # set direction of movement
        self.start_direction(start_x, start_y)
        # upload sprite
        self.image = pygame.image.load("images/spirit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (start_x, start_y)
        self.speed = speed

    def make_step(self):
        # make step
        self.rect.x += self.d_x
        self.rect.y += self.d_y

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

    def define_crossroads(self):
        crossroads = []
        for(i, road) in enumerate(self.field):
            for(j, block) in enumerate(road):
                if block == 3:
                    crossroads.append((j*BLOCK_SIZE, i*BLOCK_SIZE))
        return crossroads

    def change_directions(self):
        if self.rect.topleft in self.define_crossroads():
            # define random direction
            r_d = random.choice(("left", "right", "up", "down"))
            if r_d == "right":
                self.d_x = self.speed
                self.d_y = 0
            elif r_d == "left":
                self.d_x = -self.speed
                self.d_y = 0
            elif r_d == "up":
                self.d_x = 0
                self.d_y = self.speed
            elif r_d == "down":
                self.d_x = 0
                self.d_y = -self.speed

    def move(self):
        self.make_step()
        self.step_in_extreme_positions()
        self.change_directions()

    def start_direction(self, start_x, start_y):
        x = int(start_x / BLOCK_SIZE)
        y = int(start_y / BLOCK_SIZE)
        # find first available direction
        # dx = -1 dy = 0
        if self.field[y][x - 1] is 1 or self.field[y][x - 1] is 3:
            self.d_x = -1
            self.d_y = 0
        # dx = 1 dy = 0
        elif self.field[y][x + 1] is 1 or self.field[y][x + 1] is 3:
            self.d_x = 1
            self.d_y = 0
        # dx = 0 dy = -1
        elif self.field[y - 1][x] is 2 or self.field[y - 1][x] is 3:
            self.d_x = 0
            self.d_y = -1
        # dx = 0 dy = 1
        elif self.field[y + 1][x] is 2 or self.field[y + 1][x] is 3:
            self.d_x = 0
            self.d_y = 1





