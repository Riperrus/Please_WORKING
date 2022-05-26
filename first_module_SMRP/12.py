# данный алгоритм распределяет по двум списка числа в первый even чётные, а в odd нечётные
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
#odd = even = [] в данном случае обе переменные odd и even ссылаются на один и тот же объект
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(*odd)
print(*even)