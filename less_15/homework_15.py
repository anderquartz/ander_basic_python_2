f = open('data.txt', encoding='utf-8')
text = f.read()
print(text)
f.close()

f = open('data.txt', encoding='utf-8')
text2 = f.readline()
print(text2)
f.close()

f = open('data.txt', encoding='utf-8')
text3 = f.read(10)
print(text3)
f.close()


f = open('data.txt', encoding='utf-8')
text4 = f.readlines()
lst = [words for words in text4]
print(lst)
f.close()

f = open('data.txt', encoding='utf-8')
text4 = f.readlines()
for words in text4:
    print('Строка: ', words, end='')
f.close()

f = open('data.txt', encoding='utf-8')
text5 = f.read(5)
print('\n', text5)
f.seek(0)
text5 = f.read(5)
print(text5)
f.close()


f = open('data.txt', encoding='utf-8')
text6 = f.readlines()
print("Размер файла: ",f.tell())
f.close()


with open('data.txt', encoding='utf-8') as f:
    text = f.read()
    print(text)

try:
    f = open('data.txt', encoding='utf-8')
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Файл не найден")


try:
    f = open('data.txt', encoding='utf-8')
    text = f.read()
    print(text)
finally:
    f.close()


try:
    with open('data.txt', encoding='utf-8') as f:
        numbers = f.read()
except FileNotFoundError:
    print("Ошибка: Файл не найден")


try:
    with open('numbers.txt', encoding='utf-8') as f:
        numbers = f.readlines()
        s = 0
        for nums in numbers:
            s += int(nums)
        print(s)
except FileNotFoundError:
    print("Ошибка: Файл не найден")


import datetime
file_1 = "log.txt"
with open(file_1, 'a+', encoding='utf-8') as f:
    f.writelines(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S\n"))
    print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), " Запуск программы")
