# spisok = [1, 2, 3]
# it = iter(spisok)
# print(next(it))
# print(next(it))
# print(next(it))


# str_1 = 'sosiska'
# it_2 = iter(str_1)
# print(next(it_2))
# print(next(it_2))
# print(next(it_2))
# print(next(it_2))
# print(next(it_2))
# print(next(it_2))
# print(next(it_2))



# N = 5
# a = [x ** 2 for x in range(N)]
# print(a)



# b = [x for x in range(-10, 10) if x % 2 == 0]
# print(b)


# spisok_2 = ['kot', 'vasiliy', 'мышеловка', "пергаментообразный"]
# c = [len(spisok_2) for spisok_2 in spisok_2]
# print(c)


# s = ["чётное" if x % 2 == 0 else "нечетное" for x in range(-10, 10)]
# print(s)


# spisok_3 = ["cat", 33, [34, 42]]
# it = iter(spisok_3)
# for element in spisok_3:
#     print(True)
# else:
#     print(False)


spisok_3 = ["cat", 33, [34, 42]]

# Генератор списка (list comprehension)
results = [
    type(element) == str or type(element) == list  # Выражение
    for element in spisok_3  # Цикл
]

print(results)  # [True, False, True]
