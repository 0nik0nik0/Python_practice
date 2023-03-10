""" 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек 
отломить k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

Примеры/Тесты:
3 2 4 -> yes
3 2 1 -> no
"""
import os
os.system('cls')
pcs_vertical = int(input("Pieces in vertical => "))
pcs_horizontal = int(input("Pieces in horizontal => "))
cut_piece = int(input("How many to cut? => "))
if pcs_vertical*pcs_horizontal <= cut_piece:
    print ("You can't cut more than/equal the size of chocolate, please think before typing")
else:
    print("YES, you can cut" if (pcs_vertical*pcs_horizontal - cut_piece) % pcs_vertical == 0 or (pcs_vertical*pcs_horizontal - cut_piece) % pcs_horizontal == 0 else "NO, you can't cut")
