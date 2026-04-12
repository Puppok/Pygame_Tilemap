import pygame as pg
from modules import player, tilemap

# Инициализация
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Tilemap Platformer")
clock = pg.time.Clock()