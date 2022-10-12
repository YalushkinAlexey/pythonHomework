
 #Напишите программу вычисления арифметического выражения заданного строкой.
 #  Используйте операции +,-,/,*. приоритет операций стандартный.     
import re
s =''
s = input('введите выражение без пробела-\n ')
# some_list = []
# for ch in s:
#     some_list.append()
res = re.split('[/+*-]+', s)
result_sum = 0

def op(s):
    for i in range(1, len(s)-1):
        if res[i] == '*' :
            return int(s[i-1])*int(s[i+1])
        elif res[i] == '/':
            return int(s[i-1])/int(s[i+1])
    for i in range(1, len(s)-1):
        if res[i] == '+' :
            return int(s[i-1])+int(s[i+1]) 
        elif res[i] == '-':
            return int(s[i-1])-int(s[i+1])

result_sum = op(s) 

print(result_sum)