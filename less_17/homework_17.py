# items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
# for item in items:
#     if isinstance(item, str) or isinstance(item, list):
#         print(item, end=' ')

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
lst =[]
for item in items:
    if isinstance(item, str) or isinstance(item, list):
        lst.append(item)
print(lst)



def describe_type(x):
    if isinstance(x, str):
        print('Это строка')
    elif type(x) is int or isinstance(x, float):
        print('Это число')
    elif isinstance(x, bool):
        print('Это булевое значение')
    else:
        print('Неизвестный тип')

describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])



def filter_list(f, data: list[int]) -> list[int]:
    result = []
    for item in data:
        if f(item):
            result.append(item)
    return result

print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))



def print_info(name: str, age: int, tags: str) -> None:
    print(name, age, tags)



def analyze(data: list):
    if data:
        print('Количество элементов: ', len(data))
        print("Среднее значение элементов: ", sum(data)/len(data))

analyze([1, 2, 3])



flags = [True, True, True, False]
print(all(flags))
print(any(flags))



field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
def is_x(cell):
    return cell == 'x'

print(all(map(is_x, field[0:3])))



P = ['0', '0', '0', '*', '0']
def mines(cell):
    return cell == '*'

print(any(map(mines, P)))


import random
colors = ["red", "green", "blue", "yellow", "purple"]
print("Выбран цвет: ", random.choice(colors))



random.seed(228)
print([random.randint(0,100) for _ in range(10)])



def greet(name: str) -> str:
    return f"Привет, {name}!"

print(greet('Анна'))




def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

print(multiply(2, 3))



def area(length: float, width: float) -> float:
    return length * width

print(area.__annotations__)