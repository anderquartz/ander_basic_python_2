from math import sqrt, pow

print(sqrt(64))
print(pow(5, 3))


import random
print('Случайное число: ', random.randint(1, 10))
strr = ['Python', 'Java', 'C++']
print("Выбранный язык: ", random.choice(strr))


import my_module
print(my_module.add(3, 5))
print(my_module.multiply(4, 6))


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Код выполнялся: ", end - start)
    return wrapper

@timer
def time_def(*args):
    time.sleep(2)

time_def()


import requests

response = requests.get("https://api.github.com")
print(response.status_code)



import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

plt.plot(x, y, marker='o')
plt.title("Пример графика")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
