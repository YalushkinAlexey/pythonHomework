# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_number = int(input("N = "))
binary_number = ""
n = decimal_number
# while n > 0:
#     # в рез. строку добписываем элемент,  а потом строку с предидущего цикла. Потом что первый на вход = последний на выход LIFO, 
#     # если делать наоборот получится перевернутое число например 12(decimal) 1100(bin), а было бы 0011
#     binary_number = str(n % 2) + binary_number
#     n = int(n / 2)
# print(f'Decimal {decimal_number} to binary {binary_number}')

f = lambda n: n // 2                #стало
str_bin =""
def binary_concatenation(str_bin):
    str_bin = str(n % 2) + str(str_bin)
    return str_bin
while n > 0:
    str_bin =  binary_concatenation(str_bin)
    n = f(n)    
print(f'Decimal {decimal_number} to binary {str_bin}')