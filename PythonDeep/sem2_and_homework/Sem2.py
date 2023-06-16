## Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные
# a = 10
# b = 10.1
# str = 'Абырвалг'
# bool = True
# print(type(a), type(b), type(bool), type(str))
import math
import sys

# Задание 2
# data = [1, 2.2, True, 'Oh my Gosh', 2, 2.2, 1]
# for i in range(len(data)) :
#     print(f'тип - {type(data[i])}, номер - {i+1}, значение : {data[i]}, адрес - {id(data[i])}, размер - '
#           f'{sys.getsizeof(data[i])}, хэш - {hash(data[i])}')
#     if type(data[i]) == int : print(' Целое ')
#     if type(data[i]) == str : print(' строка ')

# задание 3
# n = int(input('введите число в 10ой системе : '))
# numX = n
# numDevisor = int(input('в какую систему переводим (2, 3 или 8): '))
# myStr = ''
# while numX >= numDevisor:
#     myStr = str(numX % numDevisor) + myStr
#     numX = numX // numDevisor
# myStr = str(numX) + myStr
# print (myStr)

# задание 4
# from decimal import Decimal
# myPi = Decimal(math.pi)
# diam = Decimal(input('введите диаметр : '))
# print(f'Длина окружности = {myPi*(diam)}, Площадь круга {myPi*(diam/2 * diam/2)} ')

#задание 5  ax^2 + bx + c = 0
# a = float(input('введите a = '))
# b = float(input('введите b = '))
# c = float(input('введите c = '))
# diskr = b*b - 4 * a * c
# if diskr > 0 : print(f'Дискриминант D = {diskr}, Корни уравнения - x1 = {(-b + (diskr ** 0.5)) / (2 * a)} x2 = {(-b - (diskr ** 0.5)) / (2 * a)}')
# elif diskr == 0 : print (f'Дискриминант D = {diskr}, Корень уравнения x = { (-b) / (2 * a)}')
# else : print(f'Дискриминант D = {diskr}, Корни уравнения - x1 = {(-b + (diskr ** 0.5)) / (2 * a)} x2 = {(-b - (diskr ** 0.5)) / (2 * a)}')

