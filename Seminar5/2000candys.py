import random
candy = 202  # стартовое знач конфет


def take_candy(candy_left):  # сколько конфет снимаем с доски
    while True:
        candy_taken = int(input('сколько конфет убрать? '))
        if 0 <= candy_taken <= 28 and candy_taken <= candy_left:
            return candy_taken

        else:
            print('неправильное кол-во. можно взять от 1 до 28, но не более чем осталось')
            continue


def who_first():                    # жеребьевка
    if random.randint(0, 1) == 1:
        user_tag = 'player1'
        print('Первый ход', user_tag)
        return user_tag
    else:
        user_tag = 'player2'
        print('Первый ход', user_tag)
        return user_tag


def desk_view(user_tag, candy):  # прорисовка игрового поля
    print('*'*80)
    print('Осталось', candy, 'конфет, ход ', user_tag)
    print('_'*80)


def move():  # основная ф-ия
    print('@'*80)
    user_tag = who_first()
    candy_left = candy
    desk_view(user_tag, candy_left)
    while candy_left > 0:
        candy_left = candy_left - take_candy(candy_left)
        if candy_left <= 0:
            break
        if user_tag == 'player1':
            user_tag = 'player2'
        else:
            user_tag = 'player1'
        desk_view(user_tag, candy_left)
    desk_view(user_tag, 0)
    print('Победил', user_tag)


def who_first():                    # жеребьевка
    if random.randint(0, 1) == 1:
        user_tag = 'player1'
        print('Первый ход', user_tag)
        return user_tag
    else:
        user_tag = 'computer'
        print('Первый ход', user_tag)
        return user_tag


def comp_take(candy_left):  # мозг компьютера
    if candy_left > 56:
        candy_taken = random.randint(1, 28)
        print('комп снял ', candy_taken, ' конфет')
        return candy_taken
    elif 30 < candy_left <= 56:
        candy_taken = candy_left - 30
        print('комп снял ', candy_taken, ' конфет')
        return candy_taken
    elif candy_left == 30:
        return 1
    elif candy_left == 29:
        return 2
    else:
        return candy_left


def with_comp():  # игра с компом
    print('+'*80)
    user_tag = who_first()
    candy_left = candy
    desk_view(user_tag, candy_left)
    while candy_left > 0:
        if user_tag == 'player1':
            candy_left = candy_left - take_candy(candy_left)
        else:
            candy_left = candy_left - comp_take(candy_left)
        if candy_left <= 0:
            break
        if user_tag == 'player1':
            user_tag = 'comp'
        else:
            user_tag = 'player1'
        desk_view(user_tag, candy_left)
    desk_view(user_tag, 0)
    print('Победил', user_tag)


if __name__ == '__main__':
    # move()                     #чтобы вдвоем за 1 столом поиграть
    with_comp()  # чтобы с компом сиграть
