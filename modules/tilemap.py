import pygame as pg
import json

class TileMap:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.map_data = []
        self.width = 0
        self.height = 0

        # Цвета тайлов
        self.tile_colors = {
            0: (50, 50, 50),  # Пусто
            1: (139, 69, 19),  # Земля (твердая)
            2: (0, 200, 0),  # Трава (декор)
            3: (100, 100, 100),  # Камень (твердый)
            4: (255, 0, 0),  # Лава (опасная)
        }

        # Свойства тайлов
        self.solid_tiles = {1, 3}  # Твердые
        self.danger_tiles = {4}  # Опасные

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        self.map_data = data['map']
        self.width = data['width']
        self.height = data['height']