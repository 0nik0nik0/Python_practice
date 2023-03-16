# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9


items = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
items.sort()
value = int(input("Enter integer for checking: "))


subtract_num = abs(value - items[0])
min_num = items[0]

for el in items:
    difference = abs(value - el)
    if difference < subtract_num:
        subtract_num = difference
        min_num = el
print(min_num)









# def nearest_value(items, value):
#     abs_list = list(map(item: abs(item - value), items))
#     return items[abs_list.index(min(abs_list))]
# print(nearest_value(items, value))
