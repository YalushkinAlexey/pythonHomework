# Крестики-нолики
# tic tac toe

desk = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # номера клеток
win = [(7, 4, 1), (8, 5, 2), (9, 6, 3), (1, 2, 3), (4, 5, 6),
       (7, 8, 9), (1, 5, 9), (7, 5, 3)]  # победные комб


def desk_view():  # рисуем доску
    print('___________________')
    for i in range(2, -1, -1):
        print('| ', desk[0 + i*3], ' | ',
              desk[1 + i*3], ' | ', desk[2 + i*3], ' |')
        print('___________________')


def input_cell(user_tag):  # вводим № клетки
    while True:
        cell = input("выберите свободную клетку для " + user_tag + ' - ')
        if cell not in '123456789':
            print('повторите ввод. неверный ввод')
            continue
        if str(desk[int(cell) - 1]) in 'X0':
            print('клетка занята')
            continue
        desk[int(cell)-1] = user_tag
        break


def winner():  # проверка выигрыша
    for cort in win:
        if desk[cort[0]-1] == desk[cort[1]-1] == desk[cort[2]-1]:
            return desk[cort[0]-1]
    else:
        return False


def main():
    count = 0
    while True:
        desk_view()
        if count % 2 == 0:
            input_cell('X')
        else:
            input_cell('0')
        if count > 3:
            who = winner()
            if who:
                desk_view()
                print('победа ', who)
                break
        count += 1
        if count > 8:
            desk_view()
            print('ничья')  
            break


if __name__ == '__main__':
    main()
