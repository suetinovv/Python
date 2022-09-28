# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input("Введите число больше нуля: "))
numbers = []
result = 0
for i in range(0, n):
    numbers.append(int((1 + 1/n)**n))
for i in numbers:
    result += i
print(numbers)
print(result)