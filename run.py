"""Модуль запуска"""

import window1
import window2
import auto_arranger


def main():
    """Главная функция"""
    # Первое окно
    window1.main()

    # Второе окно
    win2 = window2.Main()
    while not win2.frame():
        pass

    auto_arranger.main()


if __name__ == '__main__':
    main()
