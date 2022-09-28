# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
size = len(numbers)
for i in range(0, size):
    temp = randint(0, size-1)
    numbers[i], numbers[temp] = numbers[temp], numbers[i]
print(numbers)