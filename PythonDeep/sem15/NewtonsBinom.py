import logging
from datetime import datetime

logging.basicConfig(filename="log.log", filemode="a", encoding="utf-8", level=logging.INFO)
logger = logging.getLogger(__name__)
print("\033[36m{}".format('решаем уравнение вида : a*x*x + b*x + c = 0')+"\033[0m".format('\n'))

#Добавим логирование

while True:
    date = datetime.now()
    logger.info(f'ищем корни уравнения')
    try:
        a = int(input('Введите число a = '))
        b = int(input('Введите число b = '))
        c = int(input('Введите число c = '))
        logger.warning(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second}  Решаем уравнение. Введены числа {a}, {b}, {c}')
        # запишем коэф.
        break
    except :
        print("\033[34m{}".format('Допустимы только числа')+"\033[0m".format('\n'))
        logger.error(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second} Допустимы только числа')
        #запишем ошибку ввода

diskr = b*b - 4*a*c
if diskr>0:
    x1 = (-b+diskr**0.5)
    x2 = (-b + diskr ** 0.5)
    print(f"x1 = {x1},  x2 = {x2}")
    logger.info(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second}   первый корень - {x1}, второй корень - {x2}')
    #запишем решения

elif diskr==0:
    x1 = -b/2*a
    print(f"x1 = {x1}")
    logger.info(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second}    корень уравнения - {x1}')
    # запишем решения

else:
    print(f'Действительных корней нет, дискриминант = {diskr}')
    logger.warning(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second}    Действительных корней нет')
    # запишем решения

print("\033[36m{}".format('посчитаем площадь прямоугольника со сторонами x и y')+"\033[0m".format('\n'))
while True:
    logger.info(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second}    Считаем площадь прямоугольника')
    #обозначим действия

    try:
        x = int(input('Введите х = '))
        y = int(input('Введите y = '))
        if x <=0 or y <=0:
            raise Exception("\033[34m{}".format('Траляля') + "\033[0m".format('\n'))
        print(f'Площадь прямоугольника = {x * y}')
        logger.info(
            f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second}    Площадь = {x*y}')
        #запишем результат

        break
    except ValueError:
        print("\033[34m{}".format('Только числа')+"\033[0m".format('\n'))
        logger.error(
            f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second} ошибка ввода данных')
        #запишем ошибку ввода

    except Exception as ex:
        print("\033[34m{}".format('Допустимы только числа > 0')+"\033[0m".format('\n'))
        logger.error(f'{date.day}, {date.month}, {date.year}   {date.hour}:{date.minute}:{date.second} ошибка ввода данных')
        # запишем ошибку ввода







