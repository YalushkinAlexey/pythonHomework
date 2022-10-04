# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
n = int(input("длина списка N = "))
some_list = []


def fillList(n):  # заполнение списка
    filled_list = []
    
    for i in range(0, n):
        filled_list.append(random.randint(-10, 11))
    print(filled_list)
    return filled_list


def prodElement(numbers):
    prod_list = []
    if len(numbers) % 2 == 0:
        x = len(numbers)//2
    else:
        x = len(numbers)//2 + 1
    for i in range(0, x):
        prod_list.append(numbers[i] * numbers[len(numbers) - 1 - i])
    print(prod_list)


some_list = fillList(n)
prodElement(some_list)
