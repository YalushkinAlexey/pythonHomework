#1 задача
# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

myList = [1, 2, 3, 1, 2, 5, 1, 6, 7, 8, 1]
myNewList = []
for i in myList:
    if myList.count(i) > 1 : myNewList.append(i)
myNewList = list(set(myNewList))
print(f'Эти элементы имели повторы в списке, убрали уникальные и повторы {myNewList}')