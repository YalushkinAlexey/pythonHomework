# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 	Пример:
# 	- 6782 -> 23
# 	- 0,56 -> 11

number = str(input("Введите вещественное число = "))
sumN = 0
for i in range(len(number)):
    if number[i].isdigit():
        sumN += int(number[i])
print(sumN)

number = list(number)
print(sum([int(num) for num in number if num.isdigit()]))

