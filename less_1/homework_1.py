from operator import ifloordiv

name = 'Andrey'
age = 24
height = 167.5
print(f'''Имя: {name}
Возраст: {age}
Рост: {height}
''')

x=10
print(type(x))
x=25.5
print(type(x))
x = 'Python'
print(x)
print(type(x))

a=7
b=a
print(a)
print(b)
a=10
print(b)
print('потому что б ссылается на а, которое равно семи, но не было новой записи, что б ссылатся на а с новым значением')

x=y=z=100
print(x,y,z)
print(id(x))
print(id(y))
print(id(z))
x,y,z=10,20,30
print(x,y,z)
print(id(x),id(y),id(z))

a=5
b=10

a,b=b,a
print(a,b)

# a = True
# b = print
# c=if
print('слова зарезервированы')

import keyword
print(keyword.kwlist)

var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1),type(var2),type(var3))
var1='sosiska'
print(type(var1))

kek='lol'
lol='kek'
haha=1337
ghoul=1000-7
hihi=13.37
ghoulbool=1000<7

print(type(kek),type(lol),type(haha),type(ghoul),type(hihi),type(ghoulbool))

Антон="идисюда"
print(Антон)