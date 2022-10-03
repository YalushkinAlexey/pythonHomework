# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

import random


def func(f_name):  # запись в файл
    make_f(f_name)  # создаем файл
    f = open(f_name, 'a')
    f.write(equation())  # расписываем многочлен
    f.close()


def make_f(f_name):       # создание файла
    f = open(f_name, 'w')
    f.close()


def equation():     # приведение многочлена к нормальному виду
    n = int(input("введите степень многочлена "))
    equa = ''
    for i in range(n, -1, -1):
        k = kof(i)  # генерируем коэф.
        if k != 0:
            if i > 1:
                el = str(k)+'*x^'+str(i)
            elif i == 1:
                el = str(k)+'*x'
            else:
                el = str(k)
        # в зависимости от условий расписываем каждый член и добавляем в конечную формулу
        equa = equa + "+" + el
    equa = equa[:-1] + "=0"  # добавим =0 для красоты
    equa = equa[1:]  # уберем знак + спереди
    print(equa)
    return equa


def kof(n):  # генерация коэфициентов членов многочлена
    k = random.randint(0, 101)
    return k


if __name__ == '__main__':
    f_name = 'text.txt'  # тут зададим имя файла.
    func(f_name)
    f_name = 'text1.txt'  # еще разок, понадобится для след задания
    func(f_name)
    # read_file()
