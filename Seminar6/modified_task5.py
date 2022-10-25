# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 2310

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

print('Программа после улучшения ?!')
lst = [i for i in range(1, n//2+1)]
prime_list = list(filter(is_prime, lst))         #фильтруем простые числа
deviders_list = [i for i in prime_list if n % i == 0]  #наполняем лист из списка простых чисел, удовлетворяющих требованию n % i == 0
print('Список простых чисел в диапазоне до N/2 +1 ')
print(prime_list)
print('Список простых множителей(делителей) по методу - решето Эратосфена')
print(deviders_list)
print('Для сравнения результат старого кода ')

if __name__ == '__main__':
    print(task2(n))

