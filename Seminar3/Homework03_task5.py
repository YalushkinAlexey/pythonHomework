# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи  F−n = (−1)n+1Fn. F−1 = 1,  F−2 = -1,

n = int(input("N = "))
some_list = []


def fibbNegative(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    return fibbNegative(n + 2) - fibbNegative(n + 1)


def fibbPositive(n):
    if n == 1 or n == 2:
        return 1
    return fibbPositive(n - 1) + fibbPositive(n - 2)


# в этом цикле формируем список чисел фибоначчи с отрицательным значением n
for i in range(-n, 0):
    some_list.append(fibbNegative(i))
some_list.append(0)                         # 0й член послед -фибоначчи
for i in range(1, n + 1):                   # формируем список чисел фибоначчи
    some_list.append(fibbPositive(i))
print(some_list)
