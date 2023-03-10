# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

import os
os.system('cls')

sum = int(input(" Paper cranes crafted in total  = "))
peter = sergio = 1
kate = (peter + sergio)*2
all = peter+sergio+kate

if sum % all == 0:
    performance_factor = sum // all
    print(f"""
Conclusion:
Peter crafted {peter * performance_factor} paper crane(s);
Kate crafted {kate * performance_factor} paper crane(s);
Sergio crafted {sergio * performance_factor} paper crane(s).
""")
else:
    print("Invalid total amount, please try again")