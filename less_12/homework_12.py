sqr = lambda x: x ** 2
print(sqr(10))

even = lambda x: x % 2 == 0
print(even(10))

words = ["banana", "apple", "cherry"]
sorted_words  = sorted(words, key=lambda word: word[-1])
print(sorted_words)


def multiply_by(n):
    def multiply_by2(x):
        return x * n
    return multiply_by2

times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))


def counter(start=0):
    n = start              # Сохраняем начальное значение
    def counter2():
        nonlocal n        # Говорим, что используем n из внешней функции
        n+=1
        return n         # ⬅ ВАЖНО: возвращаем новое значение
    return counter2      # Возвращаем функцию-счетчик

c1 = counter(5)      # Счетчик начинается с 5
c2 = counter()       # Счетчик начинается с 0 (по умолчанию)

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2