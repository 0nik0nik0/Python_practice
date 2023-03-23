# #### 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
    
# 	Примеры/Тесты:
#     <function_name>(0,0) -> 0
#     <function_name>(0,2) -> 2
#     <function_name>(3,0) -> 3


def integers_sum(num_A: int, num_B: int) -> int:
    if not (isinstance(num_A, int) and isinstance(num_B, int)): return None
    if num_B == 0: return num_A
    return integers_sum(num_A+1, num_B-1)


print(integers_sum(0, 0))
print(integers_sum(0, 2))
print(integers_sum(3, 0))
print(integers_sum(3, "gap"))
print(integers_sum("gap", 3))