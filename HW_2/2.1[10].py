# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.

#     Примеры/Тесты:
#     Введите кол-во монет>? 5
#     Положение монеты 0: 0 или 1>? 1
#     ...
#     1 0 1 1 0
#     Кол-во монет, чтобы перевернуть: 2


import random
coins_amount = int (input ("Enter amout of coins>? "))
coins_sides = [random.randint(0, 1) for i in range(coins_amount)]
print (f' Current position of {coins_amount} coins : 0 или 1>?: {coins_sides} ')

eagle = 0
tails = 0
for coin in coins_sides:
    if coin:
       eagle += 1
    else:
        tails += 1
print (f'Minimal amount of coins which you need to turnover: {eagle if eagle <= tails else tails}')
    

