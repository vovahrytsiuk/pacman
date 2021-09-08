import pygame
import main.py
import random

class Spirit(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, d_x, d_y, field, speed = 2):
        pygame.sprite.Sprite.__init__(self)
        # set direction of movement
        self.d_x = d_x
        self.d_y = d_y
        # upload sprite
        self.image = pygame.image.load("spirit.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft(start_x, start_y)
        self.field = field
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


