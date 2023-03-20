# # 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение

# Наборы(списки) чисел можно считать заданными и не вводить с клавиатуры

# 	Примеры/Тесты:
#     Input1: 2 4 6 8 10 12 10 8 6 4 2
#     Input2: 3 6 9 12 15 18
#     Output: 6 12     Обратите внимание: Без скобочек, в одну строку

#     Input1: 2 4 6 8 10 10 8 6 4 2
#     Input2: 3 9 12 15 18
#     Output: Повторяющихся чисел нет


Input_1 = "2 4 6 8 10 12 10 8 6 4 2"
new_list1 = Input_1.split(" ")
Input_2 = "3 6 9 12 15 18"
new_list2 = Input_2.split(" ")

result = sorted(set(new_list1).intersection(set(new_list2)), reverse=True)
print(*result if len(result) > 0 else {"There are no duplicate numbers!"})




# print(" ".join(map(str, sorted(intersection_set))) if len(intersection_set) else "Повторяющихся чисел нет")