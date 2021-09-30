"""Модуль запуска"""

import window1
import window2
import auto_arranger
import prediction_of_furniture
import csv


def main():
    """Главная функция"""
    # Первое окно
    window1.main()

    # Второе окно
    win2 = window2.Main()
    while not win2.frame():
        pass

    auto_arranger.main()

    words = []
    with open('words.csv', 'r', encoding='windows-1251') as file:
        reader = csv.reader(file)
        for row in reader:
            words.append(row)
    words = words[0]

    style = prediction_of_furniture.pred_mod(words)
    with open('style.txt', 'w', encoding='utf-8') as file:
        file.write(str(style))


if __name__ == '__main__':
    main()
