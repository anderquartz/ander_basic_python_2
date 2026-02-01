# fruits = {'bananas': 100, "apple": 80, "pears": 75}
# fruits.setdefault('kiwi', 120)
# print(fruits)



# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# for name, grade in grades.items():
#     if grade >= 4:
#         print(name)



# countries = dict(Russia='Moscow', Britain="London", Serbia="Belgrade" )
# user_country = input('Введите страну: ')
# if user_country in countries:
#     capital = countries[user_country]
#     print(capital)
# else:
#     print('Страна не найдена')



# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]
#
# courses = dict(Python=["Анна", "Виктор", "Дмиитрий"], Java='Борис', С="Галина")
# print(courses)


# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]
# courses = {}
# for name, course in students:
#     courses.setdefault(course, []).append(name)
# print(courses)



# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
# min_student = min(grades, key=grades.get)
# removed_student = grades.pop(min_student)
# print(grades)



# students = ["Анна", "Борис", "Виктор", "Галина"]
# students_dict = {}
# for student in students:
#     students_dict[student] = None
# print("Словарь с None:", students_dict)
# students_dict["Анна"] = 20
# students_dict["Борис"] = 21
# students_dict["Виктор"] = 19
# students_dict["Галина"] = 22
# print("Словарь с возрастом:", students_dict)



# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
#
# # Пользователь вводит валюту
# currency = input("Введите валюту (USD, EUR или GBP): ").upper()
#
# # Проверяем, есть ли валюта в словаре
# if currency in exchange_rates:
#     rate = exchange_rates[currency]
#     print(f"Курс {currency}: {rate} руб.")
# else:
#     print("Неизвестная валюта")
#     # Добавляем новую валюту со значением None
#     exchange_rates[currency] = None
#     print(f"Валюта {currency} добавлена со значением None")
#     print("Обновленный словарь:", exchange_rates)



# dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
# dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
# # Копируем dict1, чтобы не изменять оригинал
# result = dict1.copy()
# # Объединяем с dict2
# result.update(dict2)
# print("Объединенный словарь:")
# for key, value in result.items():
#     print(f"{key}: {value}")
# print(result)


# dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
# dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
# res3 = {**dict1, **dict2}
# print(res3)


# dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
# dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
# dict1.update(dict2)
# print(dict1)


# -----------------------------------------------------------------------------------------------------------------------


# t1 = ("sobaka", 123, True, "sever", [5, 8, 4])
# print(t1)
# print(t1[1], ", ", t1[-1])


# nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
# print(nums.count(4))
# print(nums.index(7))


# lst = ["Python", "Java", "C++", "JavaScript"]
# t3 = tuple(lst)
# print(t3)
# print(type(t3)) #Присутствует с++


# t4 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(t4[:3])
# print(t4[-3:])
# print(t4[::2])


t11 = ({"sobaka": 123, "TTrue": "sever"}, [5, 8, 4])
t11[1][1] = 228
print(t11)