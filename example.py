example = "Hello World!"

# Вывод первого символа строки
print(example[0]) # H

# Вывод последнего символа строки
print(example[-1]) # !

# Вывод второй половины строки
if len(example) % 2 == 0:
    print(example[len(example) // 2:]) # World!
else:
    print(example[len(example) // 2 + 1:]) # World

# Вывод слова наоборот
print(example[::-1]) # !dlroW olleH

# Вывод каждого второго символа строки
for i in range(0, len(example), 2):
    if i + 1 < len(example):
        print(example[i], example[i+1], end='')
    else:
        print(example[i])
        
#Вариант попроще вместо длинного if
print(example[1::2])