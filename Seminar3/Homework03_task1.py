# Урок 3. Данные, функции и модули в Python
# Задачи:
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random


def fillList(n):  # заполнение списка
    filled_list = []
    for i in range(0, n-1):
        filled_list.append(random.randint(-10, 11))
    print(filled_list)
    return filled_list


def sumList(x):  # расчет суммы элементов на нечетных поз-х
    sum = 0
    for i in range(0, len(x)):
        if i % 2 != 0:
            sum += x[i]
    return sum


# 1ый способ. Инициализируем список элементов вручную
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = 0
print("Первый способ\n", numbers)
sum_of_numbers = sumList(numbers)
print("сумма чисел на нечетных позициях = ", sum_of_numbers)

# 2ой способ используем генератор псевдослуч. чисел для заполнения списка. необходимо передать лишь длину списка
print("второй способ")
n = int(input("enter length list of numbers N = "))
some_list = []
some_list = fillList(n)
sum_of_numbers = sumList(some_list)
print("сумма чисел на нечетных позициях = ", sum_of_numbers)
