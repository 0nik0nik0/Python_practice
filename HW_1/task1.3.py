""" 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд 
и получали билет с номером.Счастливым билетом называют такой билет с шестизначным номером,
 где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – 
 счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет 
 счастливость билета.

Примеры/Тесты:
385916 >>> yes
123456 >>> no
(*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор
 """
import os
os.system('cls')
ticket = input("Type the 6-digit number of your ticket => ")
first_half = 0
second_half = 0

for element in ticket[:3]:
    first_half += int(element)
for element in ticket[-3:]:
    second_half += int(element)

print("Congratulations, You are lucky guy!" if first_half == second_half else "Don't despair, try Your luck with a new ticket!")

    
