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

            # Заполнение экрана белым
            self.screen.fill(self.colors['white'])

            # Добавление группы с кнопками
            btn_group = self.generate_button_group((self.screen.get_size()[0] / 3,
                                                    self.screen.get_size()[1]))
            self.screen.blit(btn_group, (self.screen.get_size()[0] / 3 * 2, 0))

            # Отрисовка
            pg.display.update()

            # Тик таймера на fps
            self.clock.tick(self.fps)

    def generate_button(self, size, color, text):
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

    def generate_button_group(self, size):
        """Генерация группы кнопок"""

        # Поверхность кнопки
        surf = pg.Surface(size)

        # Фоновый белый цвет
        surf.fill(self.colors['white'])

        btn_size = (size[0], size[1] / 10)

        # Добавление кнопки Void
        btn_void = {'coord': (0, size[1] / 6),
                    'btn': self.generate_button(btn_size,
                                                self.colors['white'],
                                                'Void')}
        surf.blit(btn_void['btn'], btn_void['coord'])

        # Добавление кнопки Wall
        btn_wall = {'coord': (0, size[1] / 6 * 2),
                    'btn': self.generate_button(btn_size,
                                                self.colors['black'],
                                                'Wall')}
        surf.blit(btn_wall['btn'], btn_wall['coord'])

        # Добавление кнопки Door
        btn_door = {'coord': (0, size[1] / 6 * 3),
                    'btn': self.generate_button(btn_size,
                                                self.colors['green'],
                                                'Door')}
        surf.blit(btn_door['btn'], btn_door['coord'])

        # Добавление кнопки Window
        btn_window = {'coord': (0, size[1] / 6 * 4),
                      'btn': self.generate_button(btn_size,
                                                  self.colors['red'],
                                                  'Window')}
        surf.blit(btn_window['btn'], btn_window['coord'])

        # Добавление кнопки Generate
        btn_generate = {'coord': (0, size[1] / 6 * 5),
                        'btn': self.generate_button(btn_size,
                                                    self.colors['blue'],
                                                    'Generate')}
        surf.blit(btn_generate['btn'], btn_generate['coord'])

        return surf


if __name__ == '__main__':
    main = Main()
    main.loop()
