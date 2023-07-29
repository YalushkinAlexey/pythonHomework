
print("\033[36m{}".format('решаем уравнение вида : a*x*x + b*x + c = 0')+"\033[0m".format('\n'))

while True:
    try:
        a = int(input('Введите число a = '))
        b = int(input('Введите число b = '))
        c = int(input('Введите число c = '))
        break
    except :
        print("\033[34m{}".format('Допустимы только числа')+"\033[0m".format('\n'))


diskr = b*b - 4*a*c
if diskr>0:
    x1 = (-b+diskr**0.5)
    x2 = (-b + diskr ** 0.5)
    print(f"x1 = {x1},  x2 = {x2}")
elif diskr==0:
    x1 = -b/2*a
    print(f"x1 = {x1}")
else:
    print(f'Действительных корней нет, дискриминант = {diskr}')

print("\033[36m{}".format('посчитаем площадь прямоугольника со сторонами x и y')+"\033[0m".format('\n'))
while True:
    try:
        x = int(input('Введите х = '))
        y = int(input('Введите y = '))
        if x <=0 or y <=0:
            raise Exception("\033[34m{}".format('Траляля') + "\033[0m".format('\n'))
        print(f'Площадь прямоугольника = {x * y}')
        break
    except ValueError:
        print("\033[34m{}".format('Только числа')+"\033[0m".format('\n'))
    except Exception as ex:
        print("\033[34m{}".format('Допустимы только числа > 0')+"\033[0m".format('\n'))








