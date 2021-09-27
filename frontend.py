"""Модуль фронтенда"""

import sys
import pygame as pg


class Main:
    """Главный класс"""

    def __init__(self):

        # Инициализация pygame
        pg.init()

        # Создание поверхности экрана
        self.screen = pg.display.set_mode((1000, 700),
                                          pg.RESIZABLE)

        # Таймер
        self.clock = pg.time.Clock()

        # Количество кадров в секунду
        self.fps = 30

        # Словарь цветов
        self.colors = {
            'black': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
        }

        # Словарь кнопок
        self.buttons = self.gen_button_group((self.screen.get_size()[0] / 3,
                                              self.screen.get_size()[1] / 10))

        # Холст
        self.canvas = {
            'can': self.gen_canvas((self.screen.get_size()[0] / 3 * 2,
                                    self.screen.get_size()[1])),
            'rect': pg.Rect(0, 0,
                            self.screen.get_size()[
                                0] / 3 * 2,
                            self.screen.get_size()[1])
        }

    def loop(self):
        """Цикл работы программы"""
        while True:

            # Отлавливание событий
            for i in pg.event.get():

                # Выход из приложения
                if i.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                # Нажатие клавиши
                elif i.type == pg.KEYDOWN:
                    print(i.key)

                # Нажатие кнопок мыши
                elif i.type == pg.MOUSEBUTTONDOWN:
                    for _, key in enumerate(self.buttons):
                        if self.buttons[key]['rect'].collidepoint(i.pos):
                            print(key)

            #################
            # Логика работы #
            #################

            # Словарь кнопок
            self.buttons = self.gen_button_group((self.screen.get_size()[0] / 3,
                                                  self.screen.get_size()[1] / 10))

            # Холст
            self.canvas = {
                'can': self.gen_canvas((self.screen.get_size()[0] / 3 * 2,
                                        self.screen.get_size()[1])),
                'rect': pg.Rect(0, 0,
                                self.screen.get_size()[
                                    0] / 3 * 2,
                                self.screen.get_size()[1])
            }

            #######################
            # Отрисовка элементов #
            #######################

            # Заполнение экрана белым
            self.screen.fill(self.colors['white'])

            # Отрисовка кнопок
            self.screen.blit(self.buttons['void']['btn'],
                             self.buttons['void']['rect'])
            self.screen.blit(self.buttons['wall']['btn'],
                             self.buttons['wall']['rect'])
            self.screen.blit(self.buttons['door']['btn'],
                             self.buttons['door']['rect'])
            self.screen.blit(self.buttons['window']['btn'],
                             self.buttons['window']['rect'])
            self.screen.blit(self.buttons['generate']['btn'],
                             self.buttons['generate']['rect'])

            # Отрисовка холста
            self.screen.blit(self.canvas['can'],
                             self.canvas['rect'])

            # Отрисовка
            pg.display.update()

            # Тик таймера на fps
            self.clock.tick(self.fps)

    def gen_button(self, size, color, text):
        """Генерация красивой кнопки"""

        # Поверхность кнопки
        surf = pg.Surface(size)

        # Фоновый белый цвет
        surf.fill(self.colors['white'])

        # Черная обводка круга
        pg.draw.circle(surf, self.colors['black'],
                       (size[0] / 4, size[1] / 2),
                       min(size) / 4, 2)

        # Круг с указанным цветом
        pg.draw.circle(surf, color,
                       (size[0] / 4, size[1] / 2),
                       min(size) / 4 - 2)

        # Текст кнопки
        text = pg.font.Font(None, 30).render(text, True, self.colors['black'])
        surf.blit(text, (size[0] / 5 * 2, size[1] / 2 - 9))

        return surf

    def gen_button_group(self, btn_size):
        """Создание панели кнопок"""
        # Словарь кнопок
        buttons = {
            # Кнопка Void
            'void': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6,
                    *btn_size),
                'btn': self.gen_button(
                    btn_size,
                    self.colors['white'],
                    'Void')},
            # Кнопка Wall
            'wall': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 2,
                    *btn_size),
                'btn': self.gen_button(
                    btn_size,
                    self.colors['black'],
                    'Wall')},
            # Кнопка Door
            'door': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 3,
                    *btn_size),
                'btn': self.gen_button(
                    btn_size,
                    self.colors['green'],
                    'Door')},
            # Кнопка Window
            'window': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 4,
                    *btn_size),
                'btn': self.gen_button(
                    btn_size,
                    self.colors['red'],
                    'Window')},
            # Кнопка Generate
            'generate': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 5,
                    *btn_size),
                'btn': self.gen_button(
                    btn_size,
                    self.colors['blue'],
                    'Generate')
            }
        }

        return buttons

    def gen_canvas(self, size):
        """Генерация холста"""

        # Поверхность
        surf = pg.Surface(size)

        # Заливка белым
        surf.fill(self.colors['white'])

        return surf


if __name__ == '__main__':
    main = Main()
    main.loop()
