# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

def task3(lst):
    some_set = set(lst)
    print("remove dublicate using set() ", some_set)


def task3_manual(lst):
    some_list = []
    for i in range(len(lst)):
        if lst[i] not in some_list:
            some_list.append(lst[i])
    print(f'manual method - removed dublicate -  {some_list}')


def task3_rm(lst):
    res = []
    for i in range(len(lst)):
        a = lst[i]
        count = 0
        for j in range(0, len(lst)):
            if i != j:
                if a == lst[j]:
                    count += 1
        if count == 0:
            res.append(a)
    print("unique elements, using loop ", res)


if __name__ == '__main__':
    test_list = [5, 7, 9, 1, 2, 5, 7, 5]
    print("Basic list -", test_list)
    task3(test_list)
    task3_manual(test_list)
    task3_rm(test_list)
