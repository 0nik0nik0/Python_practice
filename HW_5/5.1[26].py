# #### 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя

#     Примеры/Тесты:
#     <function_name>(2,0) -> 1
#     <function_name>(2,1) -> 2
#     <function_name>(2,3) -> 8
#     <function_name>(2,4) -> 16


def exponentiation(num, degree):
    if degree == 0:
        return 1
    return exponentiation(num,degree-1) * num
print(exponentiation(2,0))
print(exponentiation(2,1))
print(exponentiation(2,3))
print(exponentiation(2,4))
