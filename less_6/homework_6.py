# x = int(input('Введите число: '))
# if x > 0:
#     print('Число положительное')
# else:
#     if x < 0:
#         print('Число отрицательное')
#     else:
#         print("Число равно нулю")


# x = int(input('Введите число: '))
# if x % 2 == 0:
#     print('Число чётное')
# else:
#     print("Число нечетное")


# x = int(input('Введите число: '))
# if 1 <= x <= 10:
#     print("Число в диапазоне")
# else:
#     print("Число не в диапазоне")


# a = int(input('Введите число: '))
# b = int(input('Введите число: '))
# if a < b:
#     a, b = b, a
# print(sorted([a,b]))


# a = int(input('Введите число a: '))
# b = int(input('Введите число b: '))
# if a < b:
#     print(a)
# else:
#     print(b)


# marks = [3, 4, 5, 2, 5, 4]
# if 2 in marks:
#     print("Есть неудовлетворительная оценка")
# else:
#     print("Все оценки положительные")

# x = int(input('Введите число: '))
# if x % 3 == 0 and x % 5 == 0:
#     print("Число делится на 3 и 5")
# else:
#     if x % 3 == 0:
#         print("Число делится только на 3")
#     else:
#         if x % 5 == 0:
#             print("Число делится только на 5")
#         else:
#             print("Число не делится на 3 и 5")


# x = input('Введите пароль: ')
# if x == "admin123":
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# amount = int(input('Введите сумму покупки: '))
# if amount >= 5000:
#     print("Выдана скидка 10%, сумма покупки: ", amount - (amount * 0.1))
# else:
#     if amount >= 1000:
#         print("Выдана скидка 5%, сумма покупки: ", amount - (amount * 0.05))
#     else:
#         print('Сумма покупки: ', amount)



# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Год високосный')
# else:
#     print("Год не високосный")


# ------------------------------------------------------------------------------


# x = int(input('Введите оценку: '))
# if x == 5:
#     print('Отлично')
# elif x == 4:
#     print('Хорошо')
# elif x == 3:
#     print('Удовлетворительно')
# elif x == 2 or x == 1:
#     print('Неудовлетворительно')
# else:
#     print('Некорректная оценка')


# x = int(input('Введите время: '))
# if 6 <= x <= 11:
#     print('Утро')
# elif 12 <= x <= 17:
#     print('День')
# elif 18 <= x <= 21:
#     print('Вечер')
# elif (22 <= x <= 23) or (0 <= x <= 5):
#     print('Ночь')
# else:
#     print("Некорректное время")


# x = int(input('Введите температуру: '))
# if x < -10:
#     print('Очень холодно')
# elif -10 <= x <= 0:
#     print('Холодно')
# elif 1 <= x <= 10:
#     print("Прохладно")
# elif 11 <= x <= 25:
#     print('Тепло')
# else:
#     print('Жарко')


# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0:
#     print('Год високосный')
# elif year % 400 == 0:
#     print('Год високосный')
# else:
#     print("Год не високосный")


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# operation = input('Введите операцию: ')
# if operation == '+':
#     print(a + b)
# elif operation == '-':
#     print(a - b)
# elif operation == '*':
#     print(a * b)
# elif operation == '/' and b !=0:
#     print(a / b)
# elif operation == '/' and b == 0:
#     print("Ошибка: деление на ноль!")
# else:
#     print("Некорректная операция")


# ---------------------------------------------


# chet = "Чётное"
# nechet = 'Не чётное'
# a = int(input('Введите число: '))
# res = chet if a % 2 == 0 else nechet
# print(res)



# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# res = a if a > b else b
# print(res)



# a = int(input('Введите число: '))
# res = "Положительное" if a > 0 else "Отрицательное" if a < 0 else "Ноль"
# print(res)


# a = int(input('Введите возраст: '))
# res = 'Вход разрешен' if a >= 18 else 'Вход запрещен'
# print(res)


amount = int(input('Введите сумму покупки: '))
res = amount - amount * 0.1 if amount > 5000 else amount
print(res)