import hw1
import unittest

class testDate(unittest.TestCase):

    def testDays(self):
        text = "21.11.2001"
        self.assertEqual(True, hw1.funcDate(text))
       # self.assertEqual(False, hw1.funcDate(text))   # Это выбросит ошибку, т.к. дата нормальная и функция выдаст True
        self.assertEqual(False, hw1.funcDate("32.11.2000"))

import pytest
myList = [1, 9, 5, 3, 2]
def sortList(myList):
    resList = sorted(myList)
    return resList

def testList():
    assert [1, 2, 3, 5, 9] == sortList(myList)
    #assert [] == sortList(myList)  Этот фэйлится т.к. список для проверки пуст в отличии от списка отправленного на сортировку