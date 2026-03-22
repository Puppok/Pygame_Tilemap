import pygame as pg

class TileEditor:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size

        # Пустая карта
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]

        # Текущий выбранный тайл
        self.current_tile = 1

        # Смещение карты на экране
        self.offset_x = 150
        self.offset_y = 60

        # Цвета тайлов
        self.tile_colors = {
            0: (50, 50, 50),  # Пусто (фон)
            1: (139, 69, 19),  # Земля
            2: (0, 200, 0),  # Трава
            3: (100, 100, 100),  # Камень
            4: (255, 100, 0),  # Лава
        }