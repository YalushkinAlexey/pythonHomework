# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:    
#     1) с помощью математических формул нахождения корней квадратного уравнения    
#     2) с помощью дополнительных библиотек Python    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


def calculate_lcm(x, y): 
    if x > y: 
        greater = x
    else:
        greater = y 

    while(not ((greater % x == 0) and (greater % y == 0))): 
        greater += 1 
    else:
        return greater



if __name__ == "__main__":
    print(calculate_lcm(3, 5))
