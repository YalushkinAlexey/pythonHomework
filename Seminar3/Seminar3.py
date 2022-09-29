
n = int(input("number N = "))
some_list = [num for num in range(20)]
some_set = set(some_list)
if n in some_set:
    print(f'число {n} присутствует в списке', some_list)


