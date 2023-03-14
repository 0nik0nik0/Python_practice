# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#  Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

#     Примеры/Тесты:
#     4 4 -> 2 2
#     5 6 -> 2 3

# **Примечание.**
# Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
# Кто не помнит, как решать квадратное уравнение - посмотрите  в сети. Обойдите дополнительной проверкой возможность комплексных решений. Можно игнорировать то,
#  что получаться рациональные решения вместо натуральных.

# Для вычисления квадратного корня используйте возведение в степень 0.5 или  ```(*)``` **Усложнение.** найдите самостоятельно в сети какая функция стандартной
#  библиотеки вычисляет квадратный корень и как до нее добраться.


import math

numbers_sum = int(input ('Enter the sum of the numbers -> '))
numbers_mul = int(input ('Enter the multiplication of the numbers -> '))


discriminant = numbers_sum**2 -4*numbers_mul

if discriminant == 0:
    hidden_num_x = hidden_num_y = numbers_sum/2
    print(numbers_sum, numbers_mul, '->', int (hidden_num_x), int (hidden_num_y))
    # print(numbers_sum, numbers_mul, '->', (hidden_num_x), (hidden_num_y)) // для рациональных чисел
elif discriminant > 0:
    hidden_num_x = (-(numbers_sum) + math.sqrt(discriminant))/(-2)
    hidden_num_y = numbers_sum - hidden_num_x
    print(numbers_sum, numbers_mul, '->', int (hidden_num_x), int (hidden_num_y))
    # print(numbers_sum, numbers_mul, '->', (hidden_num_x), (hidden_num_y)) // для рациональных чисел
else:
    # no solution
    print("There are no such positive integer numbers")


