# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
#
# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# from operator import indexOf


# some_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", 1, 23]
# def hasDigit(lst):
#     for i in range(len(lst)):
#         if type(lst[i])== int or type(lst[i]) == float:
#             return True
#     return False


# if __name__=='__main__':
#     print(hasDigit(some_list))

flat_txt = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]


def secondEnter(a_list, a_str):
    count = 0
    for i in range(len(a_list)):
        if a_list[i] == a_str:
            count += 1
            if count == 2:
                return i
    return -1


def secondEnter2(b_list, b_str):
    start = b_list.index(b_str)
    return b_list.index(b_str, start+1)


if __name__ == '__main__':
    print(secondEnter(flat_txt, 'йцу'))
    print(secondEnter2(flat_txt, 'йцу'))
