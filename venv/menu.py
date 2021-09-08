import pygame

class Menu(object):
    # state id display current item on menu bar
    state = 0
    # initialize menu class
    def __init__(self):
        # menu color
        self.color = None
        # color of selected item
        self.selected_item_color = None
        # variants in menu
        self.items = None
        # font for displaying menu
        self.font = None

    def handle_events(self, event):
        # here i gonna process K_DOWN and K_UP to communicate with menu bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state += -1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) - 1:
                    self.state += 1

