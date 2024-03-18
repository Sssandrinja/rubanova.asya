import functools

#1
# class Student:
#     def __init__(self):
#         self.name = None
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
# student = Student()
#
# student.set_name('James')
# print(student.get_name())

#2
# class Product:
#     def __init__(self):
#         self.price = None
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
# product = Product()
#
# product.set_price(112.2)
# print(product.get_price())

#3
# class Calculator(object):
#     __type = 'Calculator'
#
#     @staticmethod
#     def sum(*num):
#         return functools.reduce(lambda x, y: x + y, num)
#
#     @staticmethod
#     def razn(*num):
#         return functools.reduce(lambda x, y: x - y, num)
#
#     @staticmethod
#     def umn(*num):
#         return functools.reduce(lambda x, y: x * y, num)
#
#     @staticmethod
#     def de(*num):
#         return functools.reduce(lambda x, y: x / y, num)
#
#
# calc = Calculator()
#
# print(calc.sum(23, 11, 14, 54, 12, 321))
# print(calc.razn(23, 321))
# print(calc.umn(23, 321))
# print(calc.de(23, 321))


# 4
# class Soda:
#
#     def __init__(self, name, element=None):
#         self.name = name
#         self.element = element
#
#     def show_my_drink(self):
#         if self.element == None:
#             return f'Regular soda'
#
#         return f'{self.name} {self.element}'
#
#
# soda1 = Soda('Лимонад', 'кокос')
# soda2 = Soda('Минералка')
#
# print(soda1.show_my_drink())
# print(soda2.show_my_drink())


#5
# class TriangleChecker:
#     def __init__(self, a, b, c):
#
#         if not all(isinstance(var, (int, float)) for var in (a, b, c)):
#             raise TypeError('Нужно вводить только числа!')
#
#         if a > 0 and b > 0 and c > 0:
#             self.a = a
#             self.b = b
#             self.c = c
#
#         else:
#             raise ValueError('Отрезки должны быть > 0!')
#
#     def is_triangle(self):
#         if self.c < self.a + self.b and self.b < self.a + self.c and self.a < self.b + self.c:
#             return 'Ура, можно построить треугольник!'
#
#         else:
#             return 'Жаль, но из этого треугольник не сделать.'
#
#
# tr = TriangleChecker(3, 3, 7)
# print(tr.is_triangle())




