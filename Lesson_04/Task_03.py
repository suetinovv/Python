# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
# в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint

def generetNumberList(s): # генерирует список случайных чисел с заданым размером
    result = []
    if s < 1:
        print("Нужно ввести число больше нуля!")
        return result
    for i in range(s):
        result.append(randint(0, 10))
    print(result)
    return result

def filtrList(num): # Формирует список неповторяющихся элементов из преданного списка
    result = []
    for i in num:
        if num.count(i) == 1:
            result.append(i)
    return result

size = int(input("Задайте размер списка: "))
numbers = generetNumberList(size)
print(filtrList(numbers))