import sys

import pygame as pg

from src.const import settings
from src.const import path
from src.ai import AI
from src.field import Field
from src.background_randomizer import BackgroundRandomizer


class XO:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру, создаёт игровые объекты и задаёт фоновое изображение."""
        pg.init()

        self.__screen = pg.display.set_mode((settings.SCREEN_SIZE, settings.SCREEN_SIZE))

        self.__ai = AI()
        self.__field = Field()

        pg.display.set_caption(settings.CAPTION)
        pg.display.set_icon(pg.image.load(path.ICON).convert_alpha())
        self.__screen.blit(pg.image.load(BackgroundRandomizer().random_path()).convert_alpha(), (0, 0))

    def run(self):
        """Запуск основного цикла игры."""
        while True:
            self.__event_handler()
            self.__update_screen()

    def __event_handler(self):
        """Обрабатывает события мыши."""
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.__field.click_move_handler(pg.mouse.get_pos(), path.CROSS) and \
                        self.__field.get_n_free_cells > 0:  # ////
                    self.__field.index_move_handler(self.__ai.move(self.__field.get_n_free_cells), path.ZERO)

    def __update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.__field.paint(self.__screen)
        pg.display.flip()
