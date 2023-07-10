import os
import json
import csv
import pickle

myList = []
p = 'c:\\temp'

def sumFunc(p):
    sumF = 0                                #в эту переменную буду помещать размер файла
    sum = 0                                 #а сюда докладывать сумму папок
    for i in os.walk(p, topdown=False):     #topdown false ибо с нижнего яруса наверх пойдем
        pathF = i[0]                        #адрес
        dirName = os.path.split(i[0])[1]    #непонятная переменная
        adres = i[0]                        #ышо одна
        fileList = i[2]                     #список файлов в папке
        if len(fileList)>0 :                #проверка на вшивость
            for j in fileList:
                sizeF = os.path.getsize(adres+'\\'+j)
                myList.append({ 'type': 'file',
                                'name': j,
                                'adres': adres,
                                'size': sizeF})
                sum += sizeF
            myList.append({'type': 'Dir',
                           'name' : dirName,
                           'adres': adres,
                           'size' : sum})
    print(myList)
    return myList

def writeToFiles(data, nameF):
    with open(nameF+".json", "w") as outfile_j:
            json.dump(data, outfile_j)
    with open(nameF + ".csv", 'w', newline='', encoding='utf-8') as outfile_c:
            csv_write = csv.DictWriter(outfile_c, fieldnames=[*data[0]])
            csv_write.writeheader()
            csv_write.writerows(data)
    with open(nameF + ".pickle", 'wb') as outfile_p:
        pickle.dump(data, outfile_p)

sumFunc(p)
writeToFiles(myList, 'sumSize')