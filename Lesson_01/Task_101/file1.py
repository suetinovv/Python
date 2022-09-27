# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели и проверяет, является ли этот день выходным.

number = int(input("Введите цифру от одного до 7: "))
if 1 <= number <= 5:
    print("Workday")
elif 6 <= number <= 7:
    print("Weekend")
else:
    print("It's not a day of the week!")