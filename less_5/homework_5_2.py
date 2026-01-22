# from less_5.homework_5_1 import cities
#
# gorod = ['Msk', 'Ekb', 'Spb', "Nvb"]
# print(gorod)
# gorod2 = gorod[:]
# gorod3 = gorod2.copy()
#
# print(id(gorod))
# print(id(gorod2))
# print(id(gorod3))
#
#
# print(gorod[1:3])
# print(gorod[2:])
# print(gorod[:3])
# print(gorod[:])
# print(gorod[-3:-1])
#
# print(gorod[::2])
# print(gorod[::-1])
# print(gorod[::-2])
#
# gorod[1] = 'So4'
# gorod[2] = 'NN'
# print(gorod)
#
# # gorod[::2] = ['gorodok'] не получилось
# # print(gorod)
#
# gorod[1:3] = "Волгоград", "Омск"
# print(gorod)
#
# print([1,2,3]+[4,5,6])
# print(["Python", "rocks"] * 2)

print([1, 2, 3] == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
print([1, 2, 3] == [1, 2, "abc"]) # проверить на тождество можно, оно false, больше меньше нельзя