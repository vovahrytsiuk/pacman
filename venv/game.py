import pygame
from player import Player
import tkinter

class Game(object):
    def __init__(self):
        # create player
        self.player = Player(0, 0, "", "")
        # score variable
        self.score = 0


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            # process another events
