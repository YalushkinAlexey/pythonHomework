# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
import random
from random import *
#
filename = input('filename ->>> ')
n = 0  #кол-во строк

def fu(filename:str, n : int):
    with open(filename, "r+") as f:
        for i in range(n):
            f.write("text message\n")
        endF = ''
        endF = str(randint(-1000,1001)) + "|" + str(round(uniform(-1000,1001), 2))
        f.write(endF)

fu(filename, 3)

# Задача №2
# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные. Полученные имена сохраните в файл.

# import string, random
# from random import randint
#
# def nameX():
#     n = randint(4, 8)
#     print(n)
#     glasn = 'aeioyu'
#     bool = False
#     while not bool:
#         name = ''
#         for i in range(n):
#             ch = random.choice(string.ascii_letters)
#             name = name + ch.lower()
#         for i in glasn:
#             if i in name :
#                 bool = True
#                 break
#     print(name)
#     return name.capitalize()
#
# def wrFile(filename, name):
#     with open(filename, "a+") as f:
#         f.write(name+'\n')
# wrFile("text2",nameX())

