import one
import two

falderin = '/home/user/tst'
falderout = '/home/user/out'

#Задание выполненное на семинаре


def test_1_find_text_in_command():

    assert two.find_text_in_command(f'cd {falderin}; 7z a {falderout}/arh1',
                                   'Everything is Ok'), 'test1 FAIL'


#Задание 1. ДЗ
#Условие:
#Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).


def test_2_find_text_in_command():

    assert two.find_text_in_command(f'ls {falderout}',
                                   'arh1.7z'), 'test2 FAIL'

#*Задание 2. * ДЗ
#Установить пакет для расчёта crc32
#sudo apt install libarchive-zip-perl
#Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.

def test_3_find_text_in_command():

    temp = one.crc32(f'{falderout}/arh1.7z').lower()
    assert two.find_text_in_command(f'crc32 {falderout}/arh1.7z',
                                   temp), 'test3 FAIL'