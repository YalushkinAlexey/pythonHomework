import subprocess
import sys

def find_text_in_out_command(command, text):
    """
    Функция для поиска текста в выводе команды
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    result_out = result.stdout
    # print(result_out)
    if text in result_out:
        print('TRUE')
    else:
        print('FAIL')

if __name__ == '__main__':
    """
    Программа принимает аргументы через командную строку
    example: python3 hw.py 'ls' 'venv'
    Если не будет задан один из параметров, либо NULL
    То в функцию будут переданы следующие параметры:
    command: 'cat /etc/os-release', text: 'jammy'
    """
    try:
        arguments = sys.argv
        command = arguments[1]
        text = arguments[2]
        find_text_in_out_command(command, text)
    except:
        find_text_in_out_command('cat /etc/os-release', 'jammy')