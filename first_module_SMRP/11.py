value = (1,2)
addition = (3,4)

print(value, id(value))
value = value + addition # можно пронаблюдать, что создаётся новый объект
print(value, id(value))
value = (1,2)
value += addition # в данном же случае изменяется исходный объект
print(value, id(value))

print("\n\n\n\n\n\n\n")
#  в данном случае оба способа присвоения абсолютно одиннаковы
a=1000
b=2000
print(a, id(a))
a = a + b
print(a, id(a))
a=1000
a+=b
print(a, id(a))