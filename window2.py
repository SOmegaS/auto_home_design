"""Модуль фронтенда"""

import sys
import csv
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

        # Массив изображений
        self.images = {}
        self.load_images()

        # Словарь кнопок
        self.buttons = self.gen_button_group((self.screen.get_size()[0] / 3,
                                              self.screen.get_size()[1] / 10))

        # Холст
        self.canvas = {
            'can': self.gen_canvas((self.screen.get_size()[0] / 3 * 2,
                                    self.screen.get_size()[1])),
            'rect': pg.Rect(0, 0,
                            self.screen.get_size()[0] / 3 * 2,
                            self.screen.get_size()[1])
        }

        # Массив координат точек
        self.points = []

        # Текущая кисть
        self.brush = 'wall'

    def load_images(self):
        """Загрузка изображений"""
        try:
            self.images['net'] = pg.image.load('images/net.png')
            self.images['btn_wall'] = pg.image.load('images/btn_wall.png')
            self.images['btn_door'] = pg.image.load('images/btn_door.png')
            self.images['btn_window'] = pg.image.load('images/btn_window.png')
            self.images['btn_clear'] = pg.image.load('images/btn_clear.png')
            self.images['btn_generate'] = pg.image.load('images/btn_generate.png')
        except FileNotFoundError:
            print('Файлы программы не найдены')

        with open('path.txt', 'r', encoding='windows-1251') as file:
            path = file.read()

        if path != '':
            try:
                self.images['background'] = pg.image.load(path)
            except FileNotFoundError:
                self.images['background'] = None
        else:
            self.images['background'] = None
        print(self.images['background'])

    def frame(self):
        """Отрисовка второго окна"""

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

                # Перебор массива кнопок
                for _, key in enumerate(self.buttons):

                    # Коллизия с курсором
                    if self.buttons[key]['rect'].collidepoint(i.pos):

                        # Очистка
                        if key == 'clear':
                            self.canvas['can'].fill(self.colors['white'])
                            self.points.clear()

                        # Сохранение массива точек
                        if key == 'generate':
                            self.save_points(self.points)
                            return True

                        # Иначе сменить кисть
                        else:
                            self.brush = key

                # Запись новой точки в массив
                if self.canvas['rect'].collidepoint(i.pos):
                    self.points.append((i.pos[0] / self.canvas['can'].get_size()[0],
                                        i.pos[1] / self.canvas['can'].get_size()[1],
                                        self.brush))
                    self.brush = 'wall'

        # Перебор массива точек
        for key, val in enumerate(self.points):
            # Отрисовка точек
            pg.draw.circle(
                self.canvas['can'],
                self.colors['black'],
                (val[0] * self.canvas['can'].get_size()[0],
                 val[1] * self.canvas['can'].get_size()[1]),
                3
            )

            # Отрисовка стен, дверей и окон

            # Цвет линии
            line_color = self.colors['black']
            if val[2] == 'door':
                line_color = self.colors['green']
            elif val[2] == 'window':
                line_color = self.colors['red']

            # Проверка, что точка не одна
            if len(self.points) > 1:
                # Отрисовка линии
                pg.draw.line(
                    self.canvas['can'],
                    line_color,
                    (val[0] * self.canvas['can'].get_size()[0],
                     val[1] * self.canvas['can'].get_size()[1]),
                    (self.points[(key + 1) % len(self.points)][0] *
                     self.canvas['can'].get_size()[0],
                     self.points[(key + 1) % len(self.points)][1] *
                     self.canvas['can'].get_size()[1]),
                    2
                )

        #######################
        # Отрисовка элементов #
        #######################

        # Заполнение экрана белым
        self.screen.fill(self.colors['white'])

        # Отрисовка кнопок
        self.screen.blit(self.buttons['clear']['btn'],
                         self.buttons['clear']['rect'])
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

        return False

    def gen_button(self, size, text):
        """Генерация красивой кнопки"""

        # Поверхность кнопки
        surf = pg.Surface(size)

        # Изображение
        image = pg.transform.scale(self.images[text],
                                   (int(size[0]), int(size[1])))

        # Фоновая картинка
        surf.blit(image, image.get_rect())

        return surf

    def gen_button_group(self, btn_size):
        """Создание панели кнопок"""

        # Словарь кнопок
        buttons = {
            # Кнопка Clear
            'clear': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6,
                    *btn_size
                ),
                'btn': self.gen_button(
                    btn_size,
                    'btn_clear'
                )
            },
            # Кнопка Wall
            'wall': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 2,
                    *btn_size
                ),
                'btn': self.gen_button(
                    btn_size,
                    'btn_wall'
                )
            },
            # Кнопка Door
            'door': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 3,
                    *btn_size
                ),
                'btn': self.gen_button(
                    btn_size,
                    'btn_door'
                )
            },
            # Кнопка Window
            'window': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 4,
                    *btn_size
                ),
                'btn': self.gen_button(
                    btn_size,
                    'btn_window'
                )
            },
            # Кнопка Generate
            'generate': {
                'rect': pg.Rect(
                    self.screen.get_size()[0] / 3 * 2,
                    self.screen.get_size()[1] / 6 * 5,
                    *btn_size
                ),
                'btn': self.gen_button(
                    btn_size,
                    'btn_generate'
                )
            }
        }

        return buttons

    def gen_canvas(self, size):
        """Генерация холста"""

        # Поверхность
        surf = pg.Surface(size)

        # Заливка белым
        surf.fill(self.colors['white'])

        # Отрисовка фонового изображения
        if self.images['background'] is None:
            surf.blit(self.images['net'], self.images['net'].get_rect())
        else:
            img = self.images['background']
            img = pg.transform.scale(img, (int(size[0]), int(size[1])))
            img.set_alpha(128)
            surf.blit(img, img.get_rect())

        # Обводка
        pg.draw.rect(surf, self.colors['black'], (1, 1, size[0] - 1, size[1] - 2), 1)

        return surf

    @staticmethod
    def save_points(points):
        """Сохранение точек в csv формате"""
        # Открытие файла
        with open('point.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            # Запись массива
            writer.writerows(points)


if __name__ == '__main__':
    main = Main()
    while not main.frame():
        pass
