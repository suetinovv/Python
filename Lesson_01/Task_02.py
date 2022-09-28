# Напишите программу для проверки истиности утверждения
# -(X v Y v Z) = -X A -Y A -Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))
            print(x, y, z)