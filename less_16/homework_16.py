lst = ["Python", 123, "Java", 456, "C++", 789]
gen = (x for x in lst if type(x) == str)
result = " ".join(gen)
print(result)


import random
gen = (random.randint(1, 100) for x in range(10))
lst = list(gen)
print(lst)
print('Max num: ', max(lst))


with open('words.txt', 'r') as f:
    words = f.read()
    ww = (word for word in words.split() if len(word) > 5)
    result = " ".join(ww)
    print(result)



with open('text.txt', 'r') as f:
    words = f.readlines()
    ll = (line for line in words if "Python" in line)
    result = "".join(ll)
    print(result)



def randomer():
    while True:
        num = random.randint(1, 100)
        yield num
        if num == 50:
            break

for value in randomer():
    print(value, end=" ")







def gen4ik2(n):
    x = 0
    for x in range(1, n + 1):
        yield f"Получены данные {x}"

gennn = gen4ik2(5)
print(next(gennn))
print(next(gennn))
print(next(gennn))
print(next(gennn))
print(next(gennn))


# kek = map(lambda x: x ** 2,  int(input('Введите числа через пробел: ').split()))
# print(list(kek))


num = list(map(int, input('Введите числа через пробел: ').split()))
sqrr = map(lambda x: x ** 2, num)
print(*sqrr)


cities =  ["Москва", "Санкт-Петербург", "Казань"]
up_cities = list(map(lambda x: x.upper(), cities))
print(up_cities)


nums = [15, 30, 45, 22, 60, 77, 90, 100]
ssort = filter(lambda x: x % 3 == 0 and x % 5 == 0, nums)
print(*ssort)


# spisokk = ["hello", "world42", "python3", "abc", "123", "data1science"]
# sort_num = filter(lambda x: 0 <= x <= 9, spisokk)
# print(*sort_num)

# скопировал с нейронки, я не понимаю откуда такие задания..
def has_digit(s):
    for ch in s:
        if ch.isdigit():
            return True
    return False

spisokk = ["hello", "world42", "python3", "abc", "123", "data1science"]
sort_num = filter(has_digit, spisokk)
print(*sort_num)


countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
sovmest = dict(zip(countries, capitals))
print(sovmest)

data = [(1, 'a'), (2, 'b'), (3, 'c')]
a, b = zip(*data)
a = list(a)
b = list(b)
print(a)
print(b)



names = ["петр", "Иван", "мария", "Анна"]
sort_names = sorted(names, key=lambda x: ord(x[0]))
print(*sort_names)


products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
products.sort(key=lambda x: x[1])
print(products)