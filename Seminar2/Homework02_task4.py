#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random
n = int(input("enter N = "))  # вводим количество эл-ов
f = open('file.txt', 'w')  # открываем файл для записи
for i in range(0, n):
    # генерируем значение эл-та в диапазоне [-N, N] и задаем тип String
    value = str(random.randint(-n, n))
    f.write(value+'\n')  # записываем в файл
f.close()  # закрываем файл

# считываем номера интересующих нас позиций
a = int(input("position of first element = "))
b = int(input("position of second element = "))

f = open('file.txt', 'r')  # открываем файл для чтения
some_list = f.readlines()  # создаем список на основе файла
print(
    f'value element in {a} positioin is = {int(some_list[a])} ; value element in {b} positioin is = {int(some_list[b])} ')
# выводим конечный рез-т : произведение элементов на позициях a и b
print(
    f'{int(some_list[a])} * {int(some_list[b])} = {int(some_list[a]) * int(some_list[b])}')
f.close()
