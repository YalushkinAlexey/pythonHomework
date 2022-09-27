# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def first(x, y, z):
    return not (x or y or z)

def second(x, y, z):
    return not (x) and not (y) and not (z)

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(
                f'x = {x}, y = {y}, z = {z},  ¬(X ⋁ Y ⋁ Z) = {first(x,y,z)},  ¬X ⋀ ¬Y ⋀ ¬Z = {second(x,y,z)} ')
