#треугольник
# print('Good news, everyone!\n')
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# triangle = True
# rbTriangle = False
# eqTriangle = False
# if a >= b+c or b >= a+c or c >= a+b : print('нет такого треугольника ')
# elif a == b == c : print('равностороний')
# elif a == b or c == b or c == a : print('равнобедренный ')
# else : print('разносторонний')

# PrimeDigit
# prime = True
# maxDig = 100000
# while True:
#     n = int(input('введите число от 1 до 100000. n = '))
#     if 0 < n < maxDig: break
# for i in range (2, n//2):
#     if n%i == 0 :
#         prime = False
#         break
# if prime : print('число ', n, ' простое')
# else : print('число ', n, ' составное')

#угадайка число
# from random import randint
# num = randint(0, 1000)
# x = 1
# while x < 10:
#     n = int(input('число :'))
#     if n == num :
#         print('угадал')
#         break
#     elif n > num : print('мое число меньше. ', x+1, ' попытка')
#     else : print('мое число больше ',x+1, ' попытка')
#     x +=1
# print('мое число : ', num)
