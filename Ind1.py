'''
Парой называется класс с двумя полями, которые обычно имеют имена first и second. Требуется реализовать тип данных с помощью такого класса. Во всех заданиях обязательно должны
присутствовать:
    метод инициализации __init__ ; метод должен контролировать значения аргументов на
    корректность;
    ввод с клавиатуры read ;
    вывод на экран display .
Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры. 
Функция должна получать в качестве аргументов значения для полей структуры и возвращать структуру требуемого типа. При передаче ошибочных параметров следует выводить сообщение
и заканчивать работу.
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.
Поле first — дробное число, координата точки x на плоскости; поле second — дробное
число, координата точки y на плоскости. Реализовать метод distance() — расстояние
точки от начала координат.
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def is_number(a):
    try:
        float(a)
    except ValueError:
        return False
    return True


def make_cords(first, second):
    if is_number(first) and is_number(second) and first > 0 and second > 0:
        coordinates = Coordinates(first, second)
        return coordinates
    else:
        raise ValueError


class Coordinates:
    def __init__(self, first=0.0, second=0.0):
        if is_number(first) and is_number(second):
            if first > 0 and second > 0:
                self.__first = first
                self.__second = second
            else:
                raise ValueError
        else:
            raise ValueError

    def read(self):
        self.__first = float(input('Enter first coordinate (x): '))
        self.__second = float(input('Enter second coordinate (y): '))

    def distance(self):
        return math.sqrt(math.pow(self.__first, 2) + math.pow(self.__second, 2))

    def display(self):
        print(f'Entered point is ({self.__first},{self.__second})')


if __name__ == '__main__':
    test1 = make_cords(2.25, 4)
    test1.display()
    print(f"The distance is: {test1.distance()}")
    test1.read()
    print(f"The distance is: {test1.distance()}")

    # Пример исключения
    test2 = make_cords("asddsa", 4)
    test2.display()
    test2.distance()
