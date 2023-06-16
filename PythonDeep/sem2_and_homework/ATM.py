#задание 6 ATM
def invoice(money):
    print(f'На счету {round(money, 2)} y.e.')
def menuAtm():
    print('--'*20)
    print(f'Вывести сумму на счете, нажмите : 1')
    print(f'Снять со счета, нажмите : 2')
    print(f'Положить на счет, нажмите : 3')
    print('--' * 20)
    print(f'Для выхода нажмите 0')
    print('--' * 20)
def invoiceOut(money):
    invoice(money)
    while True:
        print(f'Сколько хотите снять со счета? ')
        outMoney = float(input(' ->> '))
        if outMoney > money :
            print(f'{invoice(money)}, введите сумму корректно')
            continue
        if bankTaxMax > outMoney - outMoney/bankTax > bankTaxMin : outMoney = outMoney - outMoney/bankTax
        elif bankTaxMin > outMoney - outMoney/bankTax : outMoney = outMoney - bankTaxMin # Тут снимаем минимальную таксу, не со счета потому что на счете может не быть суммы для банка
        else : outMoney = outMoney - bankTaxMax
        if money > rich :
            money = money - money/tax - outMoney
            break
        else :
            money = money - outMoney
            break
    return money
def invoiceIn(money):
    while True :
        print(f'Сколько хотите положить? (кратно 50)')
        moneyIn = int(input(' ->> '))
        if moneyIn%50 != 0 :
            print(f'Введите сумму кратную 50 ')
            continue
        elif moneyIn % 50 == 0 :
            money = money + moneyIn
            break
    return money

# constants
money = 0
bankTax = 1.015
bankTaxMin = 30
bankTaxMax = 600
bankPercent = 1.03
rich = 5000000
tax = 1.1
# программа
opCount = 1
while True:
    menuAtm()
    if opCount % 3 == 0 : money = money * bankPercent
    button = input(' ->> ')
    if button == '1' : invoice(money)
    elif button == '2' : money = invoiceOut(money)
    elif button == '3' : money = invoiceIn(money)
    elif button == '0' : break
    else: print(f'Непонятно чего там нажали, повторите ')
    opCount +=1