# 10 >> 16
# number = int(input('введите число : '))
# digit = number
# numericStr = '0123456789ABCDEF'
# str = ''
# while digit > 0:
#     str = numericStr[digit % 16] + str
#     digit = digit // 16
# print(f'Число {number} записывается в 16-ой системе как {str}')
# print('Проверка через hex() - ', hex(number))

import fractions
# задача с дробями
str1 = str(input('Введите дробь вида 3/4 : '))
str2 = str(input('Еще одну : '))
first = str1.split('/')
second = str2.split('/')
summa = str(int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])) + '/' + str(int(second[1]) * int(first[1]))
mult = str( int(first[0]) * int( second[0])) + '/' + str ( int(first[1]) * int(second[1]))
print(f'Сумма {summa}, Произведение {mult}')
f1 = fractions.Fraction(int(first[0]), int(first[1]))
f2 = fractions.Fraction(int(second[0]), int(second[1]))
print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')