#Калькулятор в одну строку со скобками

import re
s = '2+3*(30-10)/2'
# s = str(input("введите выражение вида a+b*(c-d)/e+g  без пробелов f = "))  #Если захочется лапками набить строку. без ошибок пожалуйста

#функция разбивки строки на список в котором числа не обязательно 1значные. возвращает список 
def f(s):
    s1 = re.split('[/+(*)-]+', s)
    lst = []
    j = 0
    lst.append(s1[j] )
    for i in range(len(s)):
        count = 1
        if s[i].isdigit()==False and s[i]!='(' and s[i]!=')' and s[i+1]!='(':
            lst.append(s[i])
            j +=1
            lst.append(s1[j])
       
        elif s[i] == ')':
            lst.append(s[i])
        elif s[i].isdigit()==False and s[i+1]=='(':
            lst.append(s[i])
            lst.append(s[i+1])
            j += 1
            i += 1
            lst.append(s1[j])
    return lst

#функция вычисления по операциям. возвращает результат a(?)b
def oper(x, y, o):
    if o == '+':
        return int(x)+int(y)
    elif o == '-':
        return int(x)-int(y)
    elif o == '*':
        return int(x)*int(y)
    elif o == '/': 
        return int(x)/int(y)

def pr_top(opers):              #заглянем под крышку, глянем приоритет операции и вернем значение приоритета
    if len(opers) > 0:
        o = opers.pop()
        opers.append(o)            #не забываем проверить - а не дно ли это?
        if o == "*" or o == "/":
            return 1
        else:
            return 0
    else:                   #думал дно, но снизу постучали
        return -1


def calculate(lst):         #А это очень сильное колдунство...
    digits = []             #заведем 2 стека, для чисел и операций
    opers = []              #применительно к этой задаче в качестве стека использую List
   
    print('-До итераций lst = ', lst, '  len(lst) = ', len(lst))  
    i = 0
    for el in lst:  
        i += 1                                    #пройдем по списку
        if el.isdigit():                            #если el число положим в стек с числами
            digits.append(el)
            # print(f'{i} итер. el {el} в digits {digits}')
        elif el == ')':             #попалась первая неприятность, начинаем доставать из стеков до момента пока не отроем '('
            o = opers.pop()         #вынули из стека операцию
            while o!= '(':          #если операция не "(" будем копать дальше
                # print(f'попался {el} достанем 2 числа и одну операцию ')
                y = digits.pop()        #пока откапываем из стека чисел число сверху 
                x = digits.pop()        #пока откапываем из стека чисел еще одно число сверху 
                res = oper(x, y, o)     #вычислим результат
                digits.append(res)      #запишем в список чисел
                # print(f'выполнили {x}{o}{y}, {res} записали в digits {digits}')
                o = opers.pop()     #копать копать копать, операцию из стека на проверку    
                # print(f' Попался (')
       
        else:                       #если неприятности в виде скобок пережили
            if el == "*" or el == "/": # смотрим на текущий el эл-т выдадим операции приоритет
                pr = 1
            else:
                pr = 0
            if pr_top(opers) <= pr:     #заглянем под крышку стека операций, кто там сидит и какой приоритет. Если приоритет <= чем у текущей операции :
                # print(f'приоритет el {el} > приоритета из стека opers {opers} ')
                opers.append(el)        #затолкаем текущую операцию в стек оп-й
                # print(f'el уложили в стек {opers}')
            else:                       #Если приоритет > чем у текущей операции :    
                if el == '(':           # И во имя святого Randoma открывающая скобка
                    opers.append(el)    # а в кучу операций ее.потом, что-нибудь придумаем
                    # print(f'Попался ( в стек opers марш {opers} ')
                    
                else:
                    # print(f'ой ой ой. нужно считать, достанем 2 числа из {digits} и операцию из стека {opers}')
                    y = digits.pop()      #если приоритет > чем у текущей и это не скобка, какая - нибудь вычислим рез-т
                    x = digits.pop()
        
                    res = oper(x, y, o)
                    digits.append(res)   #запишем рез-т             
                    # print(f'на текущий момент i = {i}, в стеке чисел у нас {digits} и в стеке операций {opers}')
            # print(f'{i} итер. el {el} в opers {opers}')
    while len(opers) > 0:  # Если список без скобок, то вероятнее всего остались стеки не пустые. Просто просчитаем их
        o = opers.pop()
        y = digits.pop()
        x = digits.pop()
        res = oper(x, y, o)
        digits.append(res)
        
    print(digits)

 
        
if __name__=='__main__':
    some_list = f(s)
    calculate(some_list)