# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def coding(fileName, fileCodeName):
    r = open(fileName, "r")
    print(r)
    data = r.read()
    r.close

    result = ""
    temp = data[0]
    count = 1
    print(data) # вывод в консоль для проверки

    for i in range(1, len(data)):
        if temp is data[i]:
            count += 1
        else:
            result += str(count) + temp
            temp = data[i]
            count = 1
    result += str(count) + temp
    print(result) # вывод в консоль для проверки

    w = open(fileCodeName, "w")
    w.write(result)
    w.close
    
words = "C:/Users/nikal/OneDrive/Рабочий стол/Python/Lesson_05/text_words.txt"
code_words = "C:/Users/nikal/OneDrive/Рабочий стол/Python/Lesson_05/text_code_words.txt"
coding(words, code_words)