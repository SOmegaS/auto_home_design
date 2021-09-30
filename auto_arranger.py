"""Модуль алгоритма расстановки мебели"""

import csv
import random
import matplotlib.path as mpl_path
import numpy as np


def main():
    """Главная функция"""

    # Массив точек стен
    points = []
    points_type = []

    # Считывание данных из файла
    with open('point.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                points.append([float(row[0]), float(row[1])])
                points_type.append(row[2])

    # Создание полигона
    polygon = mpl_path.Path(np.array(points))

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
        if points_type[key] == 'wall':
            # Первая координата стены
            x_wall1 = val[0]
            y_wall1 = val[1]

            # Вторая координата стены
            x_wall2 = points[(key + 1) % len(points)][0]
            y_wall2 = points[(key + 1) % len(points)][1]

            # Середина стены
            x_middle = (x_wall1 + x_wall2) / 2
            y_middle = (y_wall1 + y_wall2) / 2

            # x мебели
            x_furn = x_middle + 0.01
            # y мебели
            if y_wall2 == y_wall1:
                y_furn = y_wall1
            else:
                y_furn = y_middle - (x_wall2 - x_wall1) * (x_furn - x_middle) / (y_wall2 - y_wall1)
            # Проверка на нахождение в комнате
            if not polygon.contains_point((x_furn, y_furn)):
                # x мебели
                x_furn = x_middle - 0.01
                # y мебели
                y_furn = y_middle - (x_wall2 - x_wall1) * (x_furn - x_middle) / (y_wall2 - y_wall1)

            furniture.append(
                (
                    x_furn,
                    y_furn,
                    furniture_types[random.randint(0, len(furniture_types) - 1)]
                )
            )

    # Сохранение в файл
    with open('furniture.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file, lineterminator='\n')
        # Запись массива
        writer.writerows(furniture)


if __name__ == '__main__':
    print()
    main()
