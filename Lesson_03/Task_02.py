# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint

def generetNumberList(s): # генерирует список случайных чисел с заданым размером
    result = []
    for i in range(s):
        result.append(randint(0, 10))
    return result

def proizvedPar(num): # Находит произведение пар чисол первых и последних
    result = []
    for i in range(0, int(len(num)/2)):
        result.append(num[i] * num[len(num) - 1 - i])
    if len(num) % 2 == 1:
        result.append(num[int(len(num)/2)])
    return result

size = int(input("Задайте размер списка: "))
numbers = generetNumberList(size)
print(numbers)
print(proizvedPar(numbers))