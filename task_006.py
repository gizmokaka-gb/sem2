# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел
# S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

summ = int(input("Катерина, сумма чисел равна: "))
prod = int(input("А если мы их перемножим, то получится: "))
for x in range(1, 1001):
    y = summ - x
    if x <= y and x * y == prod:
        print(f'Петя загадал {x} и {y}.')

# Не могу придумать, как прописать условие для случая, если пары не существует ((