# Вывод чисел от 1 до N

# N = int(input('Введите число N: '))
# i = 0
# while i <= N:
#     i += 1
#     print(i)




# Сумма четных чисел до N

# N = int(input('Введите число N: '))
# i = 0
# sum_1 = 0
# while i <= N:
#     if i % 2 == 0:
#         sum_1 += i
#     i += 1
# print(sum_1)




# Подсчет количества цифр в числе

# n = int(input('Введите число: '))
# count = 0
# while n > 0:
#     n //= 10      # убираем последнюю цифру
#     count += 1
# print(count)




# Определение максимальной цифры в числе
#
# n = int(input('Введите число: '))
# maxx = 0
# while n > 0:
#     digit = n % 10    # получаем последнюю цифру
#     if digit > maxx:
#         maxx = digit
#     print('n = ', n)                     #смотрим n
#     print('max = ', maxx)                #смотрим текущую максимальную цифру
#     n //= 10                             #убираем последнюю цифру
#     print('diggit = ', digit, '\n')      #смотрим смотрим какую цифру мы убрали
# print("Наибольшее число: ", maxx)




# Запрос пароля

# password = input('Введите пароль: ',)
# correct_password = "qwerty123"
# while password != correct_password:
#     print('Incorrect password, try again')
#     password = input('Введите пароль: ',)
# print('Correct password!')

# ------------------------------------------------------------------------------------------

# Поиск первого четного числа

# numbers = [1337, 9, 17, 7, 228]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#         break
#     i += 1
# else:
#     print("Четное число не найдено")



# Пропуск отрицательных чисел

# n = int(input('Введите число больше нуля: ',))
# sum_1 = n
# while n != 0:
#     n = int(input('Введите число: ', ))
#     if n < 0:
#         continue
#     sum_1 += n
# print(sum_1)



# Вывод нечетных чисел из диапазона

# a = int(input('Введите число a: ',))
# b = int(input('Введите число b: ',))
# while a <= b:
#     if a % 2 == 0:
#         a += 1
#         continue
#     print(a)
#     a += 1



# Проверка на простое число (РЕШИЛ ПОЛНОСТЬЮ НЕ САМ, ТЯЖЕЛО

# n = int(input("Введите число N: "))
#
# if n < 2:
#     print("Не простое")
# else:
#     i = 2
#     while i < n:  # проверяем все числа до n
#         if n % i == 0:
#             print("Не простое")
#             break
#         i += 1
#     else:
#         print("Простое")



# Поиск максимального числа

# n=1
# maxx = 0
# while n != 0:
#     n = input('Введите число: ')
#     if n == '' or n == 0:
#         break
#     n = int(n)
#     if n > maxx:
#         maxx = n
# print(maxx)


# ------------------------------------------------------------------------------------------

# Вывести все символы строки в обратном порядке

# text = input("Введите строку: ")
# chars = list(text)
# chars.reverse()
# for char in chars:
#     print(char)



# Замена четных элементов списка на 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0
# print(numbers)



# Генерация списка степеней двойки УЖАСНО НЕ ПОНЯТНО

# N = int(input("Введите число N: "))
#
# # Создаем пустой список
# powers_of_two = []
#
# # Генерируем степени двойки от 0 до N
# for i in range(N + 1):  # N+1 чтобы включить 2^N
#     power = 2 ** i      # 2 в степени i
#     powers_of_two.append(power)
#
# print(f"Степени двойки от 2^0 до 2^{N}: {powers_of_two}")




# Вывод всех чисел от A до B с шагом K

A = int(input("Введите начало диапазона (A): "))
B = int(input("Введите конец диапазона (B): "))
K = int(input("Введите шаг (K): "))

for number in range(A, B + 1, K): # на этом моменте я почти понял как работает range
    print(number)