# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
n = int(input("длина списка N = "))
some_list = []


def fillList(n):  # заполнение списка
    filled_list = []
    for i in range(0, n):
        filled_list.append(round(random.random()*10, 2))
    print(filled_list)
    return filled_list


def difF(numbers):          # вычисляем мин и макс дробную часть эл-та, затем их разность выводим в консоль
    max = numbers[0] % 1
    min = numbers[0] % 1
    for i in range(0, len(numbers)):
        if max < numbers[i] % 1:
            max = numbers[i] % 1
        if min > numbers[i] % 1:
            min = numbers[i] % 1
    d = round(max - min, 2)
    print(d)


some_list = fillList(n)
difF(some_list)
