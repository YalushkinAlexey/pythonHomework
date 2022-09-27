# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 	Пример:
# 	- 6782 -> 23
# 	- 0,56 -> 11

number = str(input("введите вещественное число = "))
sum = 0
for i in range(len(number)):
    if number[i].isdigit():
        sum += int(number[i])
print(sum)
