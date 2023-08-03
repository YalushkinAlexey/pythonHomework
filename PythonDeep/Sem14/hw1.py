

import calendar

def funcDate(text):
    #text = input('DD.MM.YYYY - >>> ')   #ручной ввод
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1] #дней в месяце
    if int(text[0]) <= days and int(text[1])<= 12 :
        print('Нормальная дата')
        return True
    else :
        print('не корректная дата')
        return False


if __name__=='__main__':
    funcDate("01.11.2001")
