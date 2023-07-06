
#Задача №3
# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами. ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение: ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого. ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле. ✔ При достижении конца более короткого файла, возвращайтесь в его начало

def openFile(filename:str):
    with open (filename,"r") as f:
        text = f.readlines()
    return text

def multiplyDigits(text):
    text = (text[-1])       #вытащим последнюю запись
    a = int(text[0:text.index('|')])
    b = float(text[text.index('|')+1:len(text)])
    print(f'Произведение двух чисел из первого файла {a*b}')
    return a*b

#передаем сюдой два листа
def trashFunc(text:list, text2:list):
    if len(text)>= len(text2): maxLen = len(text)
    else: maxLen = len(text2)
    with open ("text3.txt", "a+") as f:
        text = openFile("text1")
        multAB = multiplyDigits(text)
        if multAB < 0 :
            j = 0       #без этой шляпы тяжко будет
            for i in range(maxLen):
                if j >= len(text2): j = 0
                f.write(str(abs(multAB))+'\t'+str(text2[j]).upper())   #если произв отриц то имена ТАКИМИ БУКВАМИ
                j+=1
        else :
            j = 0
            for i in range(maxLen):
                if j >= len(text2): j = 0
                f.write(str(round(multAB))+ '\t' + str(text2[j]).lower())
                j += 1

text = openFile("text1")
text2 = openFile("text2")
trashFunc(text,text2)
