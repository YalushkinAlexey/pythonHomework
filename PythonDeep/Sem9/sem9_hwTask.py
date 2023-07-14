# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import csv
import random
from functools import wraps
import json

fileName = 'binom.csv'
NUMMIN = -100
NUMMAX = 100
MINROW = 100
MAXROW = 1000


def writeJson():
    def deco(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            data = func(*args,**kwargs)
            with open('jsonFunc.json', "w", encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=1)
            return data
        return wrapper
    return deco

def binom(fileName = fileName, *args, **kwargs):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            with open(fileName, 'r',encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    a, b, c = row
                    whatAFunc = resultFunc(int(a),int(b), int(c))
                    result.append({"data": (a, b, c),
                                   "result": whatAFunc})
            return (result)
        return wrapper
    return deco

@writeJson()
@binom()

def csvGeneration(fileName):
    with open(fileName, "w", newline="") as f:
        text = csv.writer(f, csv.excel, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        numberStr = random.randint(MINROW, MAXROW)
        for i in range(numberStr):
            a, b, c = random.randint(NUMMIN,NUMMAX), random.randint(NUMMIN, NUMMAX), random.randint(NUMMIN,NUMMAX)
            text.writerow([a,b,c])

def resultFunc(*args):
    a,b,c = args
    disk = (b * b - 4 * a * c)
    if disk > 0:
        x1 = (-b + disk**0.5) / 2*a
        x2 = (-b - disk ** 0.5) / 2 * a
        print (f'x1 = {x1}, x2 = {x2}')
        return x1,x2
    elif disk == 0:
        x1 = x2 = -b/2*a
        return x1,x2
    else : return 'нет действительных корней'



if __name__=="__main__":
    csvGeneration(fileName)
    binom()
    writeJson()