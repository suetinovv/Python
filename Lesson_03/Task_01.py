# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

from random import randint

def generetNumberList(s): # генерирует список случайных чисел с заданым размером
    result = []
    for i in range(s):
        result.append(randint(0, 10))
    return result

def sum(num): # суммирует елементы списка стоящие на нечетных позициях
    result = 0
    for i in range(0, len(num), 2):
        result += num[i]
    return result

size = int(input("Задайте размер списка: "))
numbers = generetNumberList(size)
print(numbers)
print(sum(numbers))