import pygame
import random
from config import *

class Field(object):
    def __init__(self, column_number, row_number, vertical_ratio=0.3, horizontal_ratio=0.5):
        # generate field
        self.column_number = column_number
        self.row_number = row_number
        self.vertical_ratio = vertical_ratio
        self.horizontal_ratio = horizontal_ratio
        self.field = self.generate_field()
        for i in range(len(self.field)):
            print(self.field[i])

    def get_current_algorithm(self):
        return self.algorithms[self.current_algorithm_index]

    def get_random_position(self):
        random_row = -1
        random_column = -1
        is_available = False
        while not is_available:
            random_row = random.randint(1, self.row_number - 1)
            random_column = random.randint(1, self.column_number - 1)
            if self.field[random_row][random_column] != 0:
                is_available = True
        return [random_row, random_column]

    def get_field(self):
        return self.field

    def generate_columns(self):
        columns = []
        for i in range(1, self.column_number - 1):
            random_number = random.randint(0, 100)
            if random_number < 100 * self.vertical_ratio:
                columns.append(i)
        return columns

    def generate_rows(self):
        rows = []
        for i in range(1, self.row_number - 1):
            random_number = random.randint(0, 100)
            if random_number < 100 * self.horizontal_ratio:
                rows.append(i)
        return rows

    def generate_field(self):
        field = [[0] * self.column_number] * self.row_number

        rows = self.generate_rows()
        for row in rows:
            field[row] = [1] * self.column_number

        columns = self.generate_columns()
        for column in columns:
            for i in range(0, self.row_number):
                if field[i][column] == 1:
                    field[i][column] = 3
                else:
                    field[i][column] = 2
        return field


