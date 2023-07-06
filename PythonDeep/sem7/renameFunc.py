import pathlib
#Переименование файлов. Задаем желаемое имя, количество цифр для нумерации, старое и новое расширение




# nameOfFile = input('Желаемое имя файла ->> ')
# count = input('кол-во цифр в порядковом номере ->> ')
# extOld = input('расширение файла ->> ')
# extNew = input('новое расширение ->> ')

def numNum(number:int, count:int):
    sNum = '' + str(number)
    for i in range(count):
        sNum = str(0)+sNum
    return sNum


def renameFiles(nameOfFile:str, count:int, extOld:str, extNew:str):
    p = pathlib.Path('files/')
    temp = []
    for i in p.iterdir():
        temp.append(i.name)
    print(temp)
    number = 0
    for i in range(len(temp)):
        name = temp[i].split('.')
        if name[1] == extOld:
            number +=1
            oldName = 'files/'+name[0]+'.'+extOld
            z = pathlib.Path(oldName)
            newName = 'files/'+nameOfFile+ numNum(number, count) + '.' +extNew
            n = pathlib.Path(newName)
            z.rename(n)

#path = 'C:/Users/frost/PycharmProjects/pythonProject/Sem7/files/'
nameOfFile ='Kakoitofile'
count =7
extOld = 'xml'
extNew = 'txt'
renameFiles(nameOfFile, count, extOld, extNew)

