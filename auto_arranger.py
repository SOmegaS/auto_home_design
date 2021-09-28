"""Модуль алгоритма расстановки мебели"""

import csv
import random


def main():
    """Главная функция"""

    # Массив точек стен
    points = []

    # Считывание данных из файла
    with open('point.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                points.append([float(row[0]), float(row[1]), row[2]])

    # Типы мебели
    furniture_types = [
        'chair',
        'table',
        'bed',
        'chest',
        'closet',
        'armchair',
        'sofa',
    ]

    # Массив точек мебели
    furniture = []

    # Проход по массиву точек
    for key, val in enumerate(points):
        if val[2] == 'wall':
            furniture.append(
                (
                    (val[0] + points[(key + 1) % len(points)][0]) / 2,
                    (val[1] + points[(key + 1) % len(points)][1]) / 2,
                    furniture_types[random.randint(0, len(furniture_types) - 1)]
                )
            )

    # Сохранение в файл
    with open('furniture.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Запись массива
        writer.writerows(furniture)


if __name__ == '__main__':
    print()
    main()
