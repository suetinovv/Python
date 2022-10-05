# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

def fibonachi(s): # генерирует список фибоначчи
    result = [1, 0 ,1]
    for i in range(s-1):
        result.append(result[-1] + result[-2])
        result.insert(0, -result[0] + result[1])
    return result


size = int(input("Введите число: "))
numbers = fibonachi(size)
print(numbers)