# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

import math
import random


def generetNumberList(s): # генерирует список случайных чисел с заданым размером
    result = []
    for i in range(s):
        result.append(round(random.uniform(0, 10), 2))
    return result

def maxMin(num): 
    minimum = num[0] - math.floor(num[0])
    maximum = num[0] - math.floor(num[0])
    for i in num:
        if minimum > i - math.floor(i):
            minimum = i - math.floor(i)
        if maximum < i - math.floor(i):
            maximum = i - math.floor(i)
    print("Min: ", round(minimum, 2), "Max: ", round(maximum, 2), "Difference: ", round(maximum - minimum, 2))

size = int(input("Задайте размер списка: "))
numbers = generetNumberList(size)
print(numbers)
maxMin(numbers)