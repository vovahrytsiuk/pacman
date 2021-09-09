import pygame
from config import *

class Menu(object):
    # state id display current item on menu bar
    current_item = 0
    # initialize menu class
    def __init__(self, items, font_color=(255, 255, 255), selected_item_color=(0, 255, 0), font_size=25):
        # menu color
        self.font_color = font_color
        # color of selected item
        self.selected_item_color = selected_item_color
        # variants in menu
        self.items = items
        # font for displaying menu
        self.font = pygame.font.Font(None, font_size)

    def handle_events(self, event):
        # here i gonna process K_DOWN and K_UP to communicate with menu bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.current_item > 0:
                    self.current_item += -1
            elif event.key == pygame.K_DOWN:
                if self.current_item < len(self.items) - 1:
                    self.current_item += 1

    def display_menu(self, window):
        # display menu on the screen
        for i, item in enumerate(self.items):
            # if process chosen item, draw it with selected item color
            if i == self.current_item:
                label = self.font.render(item, True, self.selected_item_color)
            else:
                label = self.font.render(item, True, self.font_color)
            # try to place label in the correct place of screen
            # label size
            label_width = label.get_width()
            label_height = label.get_height()
            x = (SCREEN_WIDTH - label_width) / 2
            menu_height = label_height * len(self.items)
            y = (SCREEN_HEIGHT - label_height) / 2 + i * label_height
            # put label on window using coordinates x and y
            window.blit(label, (x, y))

