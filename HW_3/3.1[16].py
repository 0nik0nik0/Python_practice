# 3.1[16]: Дан список целых чисел.  Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# 	Примеры/Тесты:
#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#     Output:  2

#     Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#     Output:  -1
# Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

# ```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь тернарным оператором.



list_num = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
x = int(input("Enter desired number: "))

# sum = list_num.count(x)
# if sum == 0:
#     print(-1)
# else:
#     print(f"{sum} times Your number '{x}' occurs in this list")

print(f"{list_num.count(x)} times Your number '{x}' occurs in this list" if list_num.count(x) != 0 else "No such number in your list: -1")