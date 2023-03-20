# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с
# клавиатуры, можно задать непосредственно в коде программы

#     Примеры/Тесты:
#     Input1: 1, 2, 3, 4, 5, 6, 7, 8
#     Output1: Макс. кол-во ягод 21, собрано для куста 7

#     Input1: 11, 92, 1, 42, 15, 12, 11, 81
#     Output1: Макс. кол-во ягод 184, собрано для куста 1


bush_capacity = [11, 92, 1, 42, 15, 12, 11, 81]
berries_max = 0
for bush in range(len(bush_capacity)):
    if bush == 0:
        berries_count = bush_capacity[bush] + \
            bush_capacity[len(bush_capacity)-1] + bush_capacity[bush+1]
    elif bush == len(bush_capacity) - 1:
        berries_count = bush_capacity[bush] + \
            bush_capacity[0] + bush_capacity[bush-1]
    else:
        berries_count = bush_capacity[bush] + \
            bush_capacity[bush-1] + bush_capacity[bush+1]
    if berries_max < berries_count:
        berries_max = berries_count
        best_bush = bush


print(f'Макс. кол-во ягод {berries_max}, собрано для куста {best_bush+1} ')
