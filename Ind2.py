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
Создать класс Fraction для работы с дробными числами. Число должно быть представлено
двумя целочисленными полями: целая часть и дробная часть. Реализовать арифметические
операции сложения, вычитания, умножения и операцию сравнения.
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*


class Fraction:
    def __init__(self, integer_part=0, fractional_part=0):
        self.integer_part = integer_part
        self.fractional_part = fractional_part

    def read(self):
        self.integer_part = float(input("Enter the integer part: "))
        self.fractional_part = int(input("Enter the fractional part: "))

    def add(self, other):
        integer_part = self.integer_part + other.integer_part
        fractional_part = self.fractional_part + other.fractional_part
        carry = fractional_part // 100
        fractional_part %= 100
        integer_part += carry
        self.__add = f'{integer_part}.{fractional_part}'
        return self.__add

    def sub(self, other):
        integer_part = self.integer_part - other.integer_part
        fractional_part = self.fractional_part - other.fractional_part
        while fractional_part < 0:
            integer_part -= 1
            fractional_part += 100
        self.__sub = f'{integer_part}.{fractional_part}'
        return self.__sub

    def mul(self, other):
        value = (self.integer_part * 100 + self.fractional_part) * \
                (other.integer_part * 100 + other.fractional_part)
        integer_part = value // 10000
        fractional_part = value % 10000
        self.__mult = f'{integer_part}.{fractional_part}'
        return self.__mult

    def equal_check(self, other):
        if self.__dict__ == other.__dict__:
            self.__checker = f'{self.integer_part}.{self.fractional_part} ' \
                   f'are equal to {other.integer_part}.{other.fractional_part}'
            return self.__checker
        else:
            self.__checker = f'{self.integer_part}.{self.fractional_part} ' \
                   f'are not equal to {other.integer_part}.{other.fractional_part}'
            return self.__checker

    def display(self):
        print(f"Sum of numbers: {self.__add}")
        print(f"Sub of numbers: {self.__sub}")
        print(f"Mult of numbers: {self.__mult}")
        print(f"Check equal of numbers: {self.__checker}")


if __name__ == '__main__':
    frac1 = Fraction(2, 50)
    frac2 = Fraction(1, 75)

    frac_sum = frac1.add(frac2)
    print(f"First num + second num = {frac_sum}")

    frac_diff = frac1.sub(frac2)
    print(f"First num - second num = {frac_diff}")

    frac_prod = frac1.mul(frac2)
    print(f"First num * second num = {frac_prod}")

    frac1_copy = Fraction(2, 50)

    print(frac1.equal_check(frac1_copy))
    print(frac1.equal_check(frac2))

    frac1.read()

    frac1.display()
