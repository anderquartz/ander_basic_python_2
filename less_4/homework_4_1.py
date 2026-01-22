s = "Python для автоматизации"

# print(s.upper())
# print(s.lower())

msg = "абракадабра"
# print(msg.count('ра'))
# print(msg.count(('а'),2))

# print(msg.find('ка'))
# print(msg.find(('а'), -1)) # почему-то при вводе -1 приписка start не появляется
# print(msg.find('xyz')) # если искать то чего нет, find всегда будет выдавать -1

# text = "Я изучаю Java"
# text=(text.replace('Java','Python'))
# print(text.replace(' ',''))

# print('Python'.isalpha())
# print('12345'.isdigit())
# print('123abc'.isdigit())
#
# code = "42"
# print(code.rjust(5,'0'))
# print('text'.ljust(10,'*'))

# str1 = "яблоко, груша, банан"
# print(str1.split(', '))
#
# str2="Python;Java;C++"
# print(str2.split(";"))

# str3 = ["Привет", "мир", "!"]
# print((' '.join(str3)))
# # print(str3.replace(',',''))
#
# str4 = ["apple", "banana", "cherry"]
# print((', '.join(str4)))

# print(" Python".lstrip())
# print("Python ".rstrip())
# print(" Python ".strip())

# text = "программирование"
# print(text.count('р'))
# print(text.find("и"))
# print(text[::-1])

# text = "Hello\nPython"
# print(text) # потому что мы используем \n он переносит строку
#
# t = "Python\tAutomation"
# print(t) # добавляет tab пробел в строке
#
# path = "C:\new\test.txt"
# print(path) # использовались переносы и табуляция
#
# path = "C:\\new\\test.txt"
# print(path)
#
# str6 = "Марка вина \"Ягодка\""
# print(str6)
#
# path = r"C:\new\test.txt" # с r(raw) не нужно делать два слеша чтобы вывести в консоль слеш
# print(path)

ss = "Hello\b World" # стирает символ сзади, вероятно это backspace
print(ss)

sss = "Hello\fPython" # переход страницы, странный символ, устарело и не используется
print(sss)