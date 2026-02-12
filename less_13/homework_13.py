from unittest import result

import time


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__}')
        res = func(*args, **kwargs)
        res = res.upper()
        return res
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Количество повторений: {n}')
            for i in range(n):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")
hello()


def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Результат взят из кэша:")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))


def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Количество повторений: {repeat}')
            print(f'Вызов функции {func.__name__}')
            total_time = 0
            for i in range(repeat):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                fulltime = end - start
                total_time += fulltime
                print(f"Повторение {i + 1}: {fulltime:.4f} сек")
            avg_time = total_time / repeat
            print(f"Среднее время выполнения: {avg_time:.4f} сек")
            res = avg_time
            return res
        return wrapper
    return decorator

@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
