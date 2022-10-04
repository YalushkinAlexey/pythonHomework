# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def task2(n):
    some_list = []
    for i in range(1, n // 2 + 1):
        if n % i == 0 and is_prime(i):
            some_list.append(i)
    return some_list


def is_prime(x):
    for j in range(2, x // 2+1):
        if x % j == 0:
            return False
    return True


if __name__ == '__main__':
    print(task2(123456789))
