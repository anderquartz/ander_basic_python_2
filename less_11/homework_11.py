def hello(name):
    print(f"Привет, {name}! Добро пожаловать! " )
greet = 'Анна'
hello(greet)


def square(num):
    return num * num
print(square(5))


def is_even(num):
    return num % 2 == 0
print(is_even(4))
print(is_even(7))


def repeat_string(text, times):
    return text * times
print(repeat_string("Python", 3))


def add(a, b):
    return a + b
print(add(3, 7))


def get_max(a, b, c):
    return max(a, b, c)
print(get_max(10, 25, 7))


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
print(calculate(10, 5, '+'))
print(calculate(10, 5, '-'))
print(calculate(10, 5, '*'))
print(calculate(10, 5, '/'))

def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s1, s2 = s1.lower(), s2.lower()
    if ignore_spaces:
        s1, s2 = s1.strip(), s2.strip()
    return s1 == s2

print(compare_strings("Hello", " hello "))
print(compare_strings("Hello", "HELLO", ignore_case=False))
print(compare_strings("Hello ", "Hello", ignore_spaces=False))


def summarize(*args):
    s = 0
    for i in args:
        if isinstance(i, (int, float)) and not isinstance(i, bool): # isinstance проверяет является ли объект экземпляром указанного класса или его подкласса
            s += i
    return s
print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))


def create_profile(name, age, **extra):
    print(f'Профиль пользователя: \nИмя: {name}, \nВозраст: {age}')
    if extra:
        print("Дополнительная информация:")
        for k, v in extra.items():
            print(f'{k}: {v}')
create_profile("Иван", 30, city="Москва", job="Инженер")


def process_orders(*orders, discount=0):
    ss = sum(orders)
    print('Сумма заказа: ', ss)
    if discount:
        print('С учётом скидки: ', int(ss - (ss * (discount/100))))
process_orders(100, 200, 300, discount=10)


def merge_lists(*lists):
    combine = []
    for sp in lists:
        combine.extend(sp)
    return combine
print(merge_lists([1, 2], [3, 4], [5, 6]))


def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))