# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

data = "авб абв бав абв вба бав вба абв абв абв"

def filt(text):
    result = []
    if (len(text) < 3):
        print("The data is incorrect")
    else:
        result = list(filter(lambda x: x != "абв", text.split()))
    return result
    
result = filt(data)
print(result)