# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму (округляйте до 3 знаков после запятой).
# Пример:
# Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
some_list = []
n = int(input("введите n="))
for i in range(1, n+1):
    some_list.append(round(((1+(1/i))**i), 3))
print(some_list)

print([round(((1+(1/num))**num), 3) for num in range(1, n+1) ])