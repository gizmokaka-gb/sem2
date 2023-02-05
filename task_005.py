# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0

import random
cash = int(input("Сколько монеток лежит на столе? "))
countEagle = 0
countTail = 0
for i in range(cash):
    coin = random.randint(0, 1)
    if coin == 0:
        countEagle += 1
    else:
        countTail += 1
print(f' Орлов лежит - {countEagle}, решек - {countTail}')
if countEagle < countTail:
    print(f' Перевернуть нужно {countEagle}.')
else:
    print(f' Перевернуть нужно {countTail}.')
