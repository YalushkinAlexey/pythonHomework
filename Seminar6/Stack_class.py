

class Stack:
   
    def __init__(self):
        self.stack = []
    
    def push(self, item):                                   #добавление эл-та
        self.stack.append(item)
    
    def pop(self):                                          #возврат значения и удаление из списка крайнего
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
    
    def peek(self):                                         #заглянем под крышечку, вернем значение крайнего
        if len(self.stack) == 0:
            return None
        else:
            item = self.stack[len(self.stack)-1]
            return item

import re

#выполнение основной задачи
#дана строка '2+2*(3-1)/2'
s = '2+3*(30-10)/2'
#сначала надо разбить на составляющие!!

def f(s):
    s1 = re.split('[/+(*)-]+', s)
    lst = []
    j = 0
    lst.append(s1[j] )
    for i in range(len(s)-1):
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

def oper(x, y, o):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/': 
        return x / y

def calculate(lst):
    st = Stack()
    st.push(lst[0])
    op = Stack()
    op.push(lst[1])
    op_dict = {'+': 0, '-': 0, '*': 1, '/': 1, '(':1, ')':1}
    for i in range(2, len(lst)):
        if lst[i].isdigit ==True:
            st.push(lst[i])
        else:
            if lst[i]=='(':
                op.push(lst[i])
                
                
            else:
                top_op = op.peek()                                              #разобрать
                print(top_op,' ^^^ ', op_dict[top_op])
                if op_dict[lst[i]] > op_dict[top_op] and lst[i]!=')':
                    op.push(lst[i])
                elif lst[i] == ')':          #действие по ")"
                    while True:
                        y = int(st.pop())
                        x = int(st.pop())
                        o = op.pop()
                        res = oper(x, y, o)
                        
                        st.push(res)
                        if op.peek() =='(':
                            break
    print('***', op.stack)

some_list = []
some_list = f(s)
print('@',some_list)

calculate(some_list)


