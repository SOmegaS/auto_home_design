"""Модуль фронтенда"""
import csv
import sys
from tkinter import filedialog
import pygame as pg
import easygui
import os


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pg.init()
SCREEN = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)
direc = ''
end = ["jpg", "jpeg", "png", "bmp", "raw", "tiff", "gif", "psd"]

asset_url = resource_path('images/input.jpg')
btn2 = pg.image.load(asset_url)

KW = []
KW_PR = []
H = 50


def UploadAction(event=None):
    global adress, ending
    filename = filedialog.askopenfilename()
    ending = filename.split('.')[-1]
    adress = filename


button = pg.Rect(250, 200, 100, 30)
button1 = pg.Rect(450, 310, 150, 130)
button2 = pg.Rect(100, 400, 200, 45)
line = pg.Rect(400, 0, 2, 480)
line1 = pg.Rect(400, 60, 250, 2)
line2 = pg.Rect(400, 250, 250, 2)

font_name = pg.font.match_font('Times new roman')


def draw_text(surf, text, size, x, y):
    """Отрисовка текста"""
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class BTN2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(btn2, (150, 150))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = 525
        self.rect.bottom = 450


class InputBox:
    """Класс поля ввода"""

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """Отлавливание событий"""
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            elif button.collidepoint(event.pos):
                # prints current location of mouse
                global KW
                if self.text in KW or self.text.replace(" ", "") in KW:
                    pass

                else:
                    if self.text != '' and self.text.replace(" ", "") != '':
                        self.text = self.text.replace(" ", "")
                        KW.append(self.text)
                self.text = ''
                print(self.text)
            elif button1.collidepoint(event.pos):
                # prints current location of mouse
                global direc
                direc = easygui.fileopenbox()
            elif button2.collidepoint(event.pos):
                # prints current location of mouse
                ending = direc.split('.')[-1]
                # Открытие файла
                with open('words.csv', 'w', encoding='windows-1251') as file:
                    writer = csv.writer(file)
                    # Запись массива
                    print(KW)
                    writer.writerows([KW])
                with open('path.txt', 'w', encoding='windows-1251') as file:
                    file.write(direc)
                print("-" * 8)
                print(KW)
                print(direc)
                print("-" * 8)
                return 'quit'
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            '''Нажатие кнопки'''
            if len(KW) >= 4:
                self.text = ''
            elif len(self.text) > 10:
                if event.key == pg.K_BACKSPACE:
                    '''Нажатие кнопки backspace'''
                    self.text = self.text[:-1]
                elif event.key == pg.K_RETURN:
                    '''Нажатие кнопки Enter'''
                    if self.text in KW or self.text.replace(" ", "") in KW:
                        '''Не добавляем если уже есть в списке'''
                        pass
                    else:
                        if self.text != '' and self.text.replace(" ", "") != '':
                            '''Проверка'''
                            self.text = self.text.replace(" ", "")
                            KW.append(self.text)
                        draw_text(SCREEN, self.text, 17, 300, 205)
                    self.text = ''
                else:
                    pass
            elif self.active:
                if event.key == pg.K_RETURN:
                    if self.text in KW or self.text.replace(" ", "") in KW:
                        pass
                    else:
                        if self.text != '' and self.text.replace(" ", "") != '':
                            self.text = self.text.replace(" ", "")
                            KW.append(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        """Масштабирование поля"""
        # Resize the box if the text is too long.

        for x in KW:
            if x == "":
                KW.remove(x)
        width = max(300, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self):
        """Отрисовка поля ввода"""
        global SCREEN
        # Blit the text.
        SCREEN.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(SCREEN, self.color, self.rect, 2)


all_sprites = pg.sprite.Group()
all_sprites.add(BTN2())


def main():
    """Главная функция кода"""
    clock = pg.time.Clock()
    input_box1 = InputBox(50, 100, 140, 32)
    # input_box2 = InputBox(100, 300, 140, 32)
    # input_boxes = [input_box1, input_box2]
    input_boxes = [input_box1]
    done = False

    while not done:
        for x in KW:
            if " " in x:
                KW[KW.index(x)] = x.replace(" ", "")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                if box.handle_event(event) == 'quit':
                    return
        for box in input_boxes:
            box.update()
        SCREEN.fill((30, 30, 30))
        for box in input_boxes:
            box.draw()

        pg.draw.rect(SCREEN, 'lightskyblue3', button, 2, 15)
        pg.draw.rect(SCREEN, 'dodgerblue2', button2, 2, 30)
        pg.draw.rect(SCREEN, [200, 200, 200], line)
        pg.draw.rect(SCREEN, [200, 200, 200], line1)
        pg.draw.rect(SCREEN, [200, 200, 200], line2)

        all_sprites.update()
        all_sprites.draw(SCREEN)

        draw_text(SCREEN, "Auto Design Concept", 30, 140, 10)
        draw_text(SCREEN, "Key words", 30, 480, 10)
        draw_text(SCREEN, "Add more", 17, 300, 205)
        draw_text(SCREEN, "Generate", 30, 200, 405)

        if len(KW) == 1:
            draw_text(SCREEN, KW[0], 30, 550, 80)
        elif len(KW) == 2:
            draw_text(SCREEN, KW[0], 30, 550, 80)
            draw_text(SCREEN, KW[1], 30, 550, 120)
        elif len(KW) == 3:
            draw_text(SCREEN, KW[0], 30, 550, 80)
            draw_text(SCREEN, KW[1], 30, 550, 120)
            draw_text(SCREEN, KW[2], 30, 550, 160)
        elif len(KW) == 4:
            draw_text(SCREEN, KW[0], 30, 550, 80)
            draw_text(SCREEN, KW[1], 30, 550, 120)
            draw_text(SCREEN, KW[2], 30, 550, 160)
            draw_text(SCREEN, KW[3], 30, 550, 200)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
