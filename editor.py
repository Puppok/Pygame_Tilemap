import pygame as pg
from modules.tile_editor import TileEditor

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Tilemap Editor")
clock = pg.time.Clock()

# Создание редактора
editor = TileEditor(width = 20, height = 15, tile_size = 32)

# Попытка загрузить сохраненную карту
editor.load_from_file("tilemap.json")

# Состояние мыши
mouse_pressed = False