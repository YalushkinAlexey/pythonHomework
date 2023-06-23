# решение с модулем выдает больше вариантов
from itertools import combinations
from itertools import permutations
myDict = {'продукты': 10, 'котел': 2.1, 'хлеб': 0.7, 'топор': 2.3, 'динамит': 1, 'вода': 1.5, 'палатка': 2, 'арбуз': 8}
maxWeight = 13
bigBag = {}

print("Вес всех вещей")
print(round(sum(myDict.values()),2))

weight = maxWeight
#    int(input("Введите грузоподъемность рюкзака в граммах\n"))

itemName = [*myDict.keys()]
variants = []
for n in range(1, len(itemName) + 1):
    comby = combinations(itemName, n)
#    print(list(comby))
    for variant in comby:
        sumItems = 0
        tempVariant = set()
        for el in variant:
            if sumItems + myDict[el] > weight:  # если сумма с добавление вещи превысит лимит, то
                continue
            sumItems += myDict[el]
            tempVariant.add(el)
        if tempVariant not in variants:  # полученное до этого множество добавляем в список вариантов (если его там еще нет)
            variants.append(tempVariant)

# проверим являются ли варианты подмножествами других вариантов, если да, то удалим эти варианты
i = 0
while i < len(variants):
    for j in range(0, len(variants)):
        if i == j:
            continue
        if variants[i] < variants[j]:
            variants.pop(i)
            break
    else:
        i += 1

print(f"Количество полученных вариантов: {len(variants)}")
print()

for var in sorted(variants, key=lambda x: sum(myDict[s] for s in x), reverse=True):
    print(*sorted(list(var)))
    wght = sum(myDict[s] for s in var)
    print(f" вес предметов {wght}")
    print()
