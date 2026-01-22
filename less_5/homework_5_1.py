cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = ['vasya',228, 13.37, -5, True, False, ['kek', 14, True]]
print(cities)
print(numbers)
print(mixed)

# print(cities[0])
# print(numbers[-1])
# # print(cities[10]) # ошибка, отсутствует в диапозоне
#
# numbers[1] = 10
# mixed[-1] = 'Python'
# print(cities)
# print(numbers)
# print(mixed)
#
#
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
#
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

print([1, 2, 3] + [4, 5])
print(["Python", "is", "awesome"] * 3)

print(3 in numbers)
print("Москва" in cities)
mixed.append([1, 2])
print([1, 2] in mixed)

del cities[2]
del cities[-1]

print(numbers)
print(cities)


a = (list('Python'))
print(a)
print(min(a))
print(max(a))
# print(sum(a)) строки нельзя складывать


