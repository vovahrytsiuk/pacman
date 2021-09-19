import pygame
from player import Player
import tkinter
from config import *
from menu import Menu
from road_block import RoadBlock
from dot import Dot
from spirit import Spirit

def get_random_coordinates():
    r_x, r_y = field.get_random_position()
    r_x *= BLOCK_SIZE
    r_y *= BLOCK_SIZE
    return [r_x, r_y]

class Game(object):
    def __init__(self):
        # score variable
        self.score = 0
        self.game_over = True
        # font for score displaying
        self.font = pygame.font.Font(None, 35)
        # create menu bar
        self.menu = Menu(("Restart", "Exit"), font_size=60)
        # create player
        self.players = pygame.sprite.Group()
        player_coordinates = get_random_coordinates()
        self.player = Player(player_coordinates[1], player_coordinates[0])
        self.players.add(self.player)
        # roads for player
        self.horizontal_roads = pygame.sprite.Group()
        self.vertical_roads = pygame.sprite.Group()
        for i, road in enumerate(field.get_field()):
            for j, block in enumerate(road):
                if block == 1:
                    self.horizontal_roads.add(RoadBlock(j * BLOCK_SIZE + BLOCK_SIZE / 4,
                                                        i * BLOCK_SIZE + BLOCK_SIZE / 4,
                                                         BLOCK_SIZE / 2, BLOCK_SIZE / 2, BLACK))
                elif block == 2:
                    self.vertical_roads.add(RoadBlock(j * BLOCK_SIZE + BLOCK_SIZE / 4,
                                                        i * BLOCK_SIZE + BLOCK_SIZE / 4,
                                                        BLOCK_SIZE / 2, BLOCK_SIZE / 2, BLACK))
        # create spirits
        self.spirits = pygame.sprite.Group()
        spirit_coordinates = get_random_coordinates()
        self.spirits.add(Spirit(spirit_coordinates[1], spirit_coordinates[0], field.get_field()))
        spirit_coordinates = get_random_coordinates()
        self.spirits.add(Spirit(spirit_coordinates[1], spirit_coordinates[0], field.get_field(), 1))
        spirit_coordinates = get_random_coordinates()
        self.spirits.add(Spirit(spirit_coordinates[1], spirit_coordinates[0], field.get_field(), 4))
        # to do add more spirits
        # eat for player
        self.dots_group = pygame.sprite.Group()
        for i, road in enumerate(field.get_field()):
            for j, block in enumerate(road):
                if block != 0:
                    self.dots_group.add(Dot(j * BLOCK_SIZE + 12, i * BLOCK_SIZE + 12,
                                            WHITE, 8, 8))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.game_over:
                self.menu.handle_events(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over:
                        if self.menu.current_item == 0:
                            # start new game
                            self.__init__()
                            self.game_over = False
                        elif self.menu.current_item == 1:
                            # exit game
                            return False

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()

                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

        return True

    def game_logic(self):
        if not self.game_over:
            self.player.move(self.horizontal_roads, self.vertical_roads)
            hit_with_eat = pygame.sprite.spritecollide(self.player, self.dots_group, True)
            for _ in hit_with_eat:
                self.score += 1
            hit_with_spirits = pygame.sprite.spritecollide(self.player, self.spirits, True)
            if len(hit_with_spirits) > 0:
                self.player.bang = True
                self.game_over = True
            for spirit in self.spirits:
                spirit.move()

    def display_game(self, window):
        window.fill(BLACK)
        if self.game_over:
            self.menu.display_menu(window)
        else:
            self.draw_field(window)
            self.dots_group.draw(window)
            self.spirits.draw(window)
            self.players.draw(window)
            #
            text = self.font.render("Score: " + str(self.score), True, GREEN)
            # Put the text on the screen
            window.blit(text, [150, 20])
        pygame.display.flip()

    def draw_field(self, window):
        self.horizontal_roads.draw(window)
        self.vertical_roads.draw(window)
        for i, road in enumerate(field.get_field()):
            for j, block in enumerate(road):
                if block == 1:
                    pygame.draw.line(window, RED, [j * BLOCK_SIZE, i * BLOCK_SIZE], [(j + 1) * BLOCK_SIZE, i * BLOCK_SIZE], 5)
                    pygame.draw.line(window, RED, [j * BLOCK_SIZE, (i + 1) * BLOCK_SIZE], [(j + 1) * BLOCK_SIZE, (i + 1) * BLOCK_SIZE], 5)
                elif block == 2:
                    pygame.draw.line(window, RED, [j * BLOCK_SIZE, i * BLOCK_SIZE], [j * BLOCK_SIZE, (i + 1) * BLOCK_SIZE], 5)
                    pygame.draw.line(window, RED, [(j + 1) * BLOCK_SIZE, i * BLOCK_SIZE], [(j + 1) * BLOCK_SIZE, (i + 1) * BLOCK_SIZE], 5)



