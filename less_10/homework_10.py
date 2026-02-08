a = {1, 2, 3, 'kek', "lol"}
a.add(4)
a.add(2)
print(a)

b = ['Msk', "Nvb", "Spb", "Ekb", 'Msk']
c = set(b)
print(c)
print(len(c))

d = {1,2,3,4,5,6,7,8,9,10}
d.remove(5)
d.discard(15)
# d.remove(15)
print(d)

str_1 = 'abrakadabra'
set_1 = set(str_1)
print(set_1)
print(len(set_1))

set_0 = set()
set_0.add(10)
set_0.add('hello')
set_0.update([(1, 2, 3)])
# set_0.update([[4, 5, 6]]) нельзя добавить изменяемый тип в множества(списки, словари, множества)
print(set_0)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
peresechenie = s1 & s2
print(s1.intersection(s2))
print(peresechenie)

objedinenie = s1 | s2
print(s1.union(s2))
print(objedinenie)

raznost = s1 - s2
print(raznost)
print(s2.difference(s1))

simraznost = s1 ^ s2
print(s1.symmetric_difference(s2))
print(simraznost)


even_numbers = {2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers & odd_numbers)
print(even_numbers | odd_numbers)


python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
two_courses = python_students & java_students
print(two_courses)
print(python_students.symmetric_difference(java_students))
not_only_one = (python_students | java_students)
print(not_only_one)


text1 = set("программирование")
text2 = set("автоматизация")
obshie = text1 & text2
first = text1 - text2
unique = text1 | text2
print(obshie)
print(first)
print(unique)


# ------------------------------------------------------------------

aa = {a ** 2 for a in range(11) if a % 2 == 0}
print(aa)


words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
bb = {word.upper() for word in words}
print(bb)


grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
cc = {name: 'отлично' if grade >=80 else 'удовлетворительно' for name, grade in grades.items()}
print(cc)


text = {"Python", "automation", "programming", "testing"}
dict_1 = {slovo: len(slovo) for slovo in text}
print(dict_1)


n = 10
dict_2 = dict_2 = {i: {j ** 2 for j in range(1, i + 1)} for i in range(1, n + 1)}
print(dict_2)