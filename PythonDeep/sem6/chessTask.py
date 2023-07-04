# @@@ Данная программа умеет расставлять 8 ферзей на доску 64 клеток, чтобы они друг друга не грызли
# Все выводит 92 комбинации. Рекурсивно устанавливая ферзей по одному, и возвращаясь на шаг назад если установка не возможна
# В конце добавлена функция выбора количества комбинаций для отображения


n = 8 #размер доски, при изменении величины изменить переменную alpha
deskList = []
desk = [[0 for i in range(n)] for j in range(n)]

def setF(i:int,j:int):
    global n
    for k in range(n):
        desk[k][j] += 1
        desk[i][k] += 1
        if 0 <= i+j-k < n: desk[i+j-k][k] +=1
        if 0 <= i-j+k < n: desk[i-j+k][k] +=1
    desk[i][j] =-1

def delF(i:int,j:int):
    global n
    for k in range(n):
        desk[k][j] -=1
        desk[i][k] -=1
        if 0 <=i+j-k < n: desk[i+j-k][k] -=1
        if 0 <=i-j+k < n: desk[i-j+k][k] -=1
    desk[i][j] = 0

def printResult():
    global n
    alpha = 'abcdefgh'
    myList = []
    global deskList
    for i in range(n):
        for j in range(n):
            if desk[i][j] == -1:
                myList.append(alpha[j] + str(i+1))
    print('  '.join(myList))
    deskList.append(myList)
def calcF(i:int):
    for j in range(8):
        if desk[i][j] == 0:
            setF(i,j)
            if i == 7:
                printResult()
            else :
                calcF(i+1)
            delF(i,j)

def printVariants(x:int):
    global n
    myList = []
    for i in range(x):
        myList.append(deskList[i])
        print(" ".join(myList[i]))
calcF(0)
x = int(input('Укажите кол-во вариантов -->> '))
printVariants(x)
