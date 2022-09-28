# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причем X != 0 и Y != 0 и выдает номер четверти плоскости
# в которой находится эта точка.

x = int(input('Введите x: '))
y = int(input('Введите y: '))
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
else:
    print('Error, 0 entered!')