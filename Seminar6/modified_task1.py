#Задача №1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def work(n):
    if 0 < n < 6: 
        return True
    else:
        return False


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']   
num_of_day = [i for i in range(1,8)]        # list comprehension
lst = list(zip(num_of_day, days))           #       zip 
working_days = list(zip (days,list(filter(work, num_of_day))))  # zip & filter

if __name__=='__main__':
    
    # while n < 0 and n > 8 :
    #     if 0 > n <= 7 :
    #         print('break')
    #         break
    #     else:
    #         n = int(input('N = '))
    while True:
        n = int(input('N = '))
        if n in range(1,8):
            break 
        
    print(f'в неделе 7 дней {lst}')
    print('~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~')
    print('No time to chill - ' if work(n) else 'Ustas to Alex - can make a relax. Today - ', lst[n-1][1])
    tmrw = lambda n: n+1 if 0< n <= 6 else 7-n+1        #lambda
    print(f'Tomorrow is {tmrw(n)} day of week ', lst[tmrw(n)-1][1]) # lambda & ternary operator

