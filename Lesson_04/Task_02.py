# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

def generetedListNumber(n):
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return result



number = int(input("Введите число: "))
listNumbers = generetedListNumber(number)
print("Cписок простых множителей числа", listNumbers)