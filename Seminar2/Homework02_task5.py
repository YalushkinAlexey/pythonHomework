import random

example_list = []
n = int(input("enter N = "))


def fillList(n):            # заполнение списка
    filledList = []
    for i in range(0, n+1):
        filledList.append(i)
    return filledList


def shuffleList(some_list):         # перемешивание элементов списка
    sh_list = []
    for i in range(len(some_list)):
        # index выбирается случайным образом в диапазоне (0, до последнего эл-та в списке)
        index = random.randint(0, len(some_list) - 1)
        # добавляем в результирующий список эл-та с индексом index
        sh_list.append(some_list[index])
        # чтобы избежать повторов удаляем из начального списка эл-т с индексом index
        some_list.remove(some_list[index])
    return sh_list  # возвращаем результирующий список


some_list = fillList(n)  # заполним
print(f'example list of n numbers \n{some_list}')  # выведем в консоль образец
# перемешиваем и выводим в консоль
print(f'using manual shuffle algorithm \n{shuffleList(some_list)}')

a = []
a = fillList(n)
random.shuffle(a)  # типовой метод из стандартного набора
print(f'using method random.shuffle() \n{a}')
