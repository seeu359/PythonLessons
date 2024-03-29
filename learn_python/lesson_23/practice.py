from itertools import count

# Практика 1
# Необходимо определить функцию-генератор с именем get_sum, которая бы возвращала текущую сумму чисел
# последовательности длины N в диапазоне целых чисел [1; N]. Например:

# - для первого числа 1 сумма равна 1;
# - для второго числа 2 сумма равна 1+2 = 3
# get_sum(5) ->
# 1
# 3
# 6
# 10
# 15


...

# Практика 2
# Необходимо определить функцию-генератор get_passwords, которая бы выдавала пароль длиной N символов из случайных букв, цифр и
# некоторых других знаков. Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных
# символов chars длиной N и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Переменная chars
# находится в модуле lesson_23.utils

...


# Практика 3
# Определи функцию-генератор get_prime_numbers, которая бы возвращала простые числа. (Простое число - это натуральное
# число, которое делится только на себя и на 1).

# a = get_prime_numbers()
# next(a) => 3
# next(a) => 5
# next(a) => 7
# next(a) => 13
# next(a) => 19




# Практика 4
# Создай функцию infinite(lst, tries), которая будет проходиться по элементам списка lst (целые числа) заданное количество раз (tries) циклически.
# Один раз - один элемент списка.
# После вывода последнего значения последовательности процедура начнется с самого начала.

# Например, если в списке 2 элемента, а функция получила значение 3, то сначала выведется первый объект, потом последний, а потом опять первый.
# Результат работы функции представьте в виде строки, состоящей из tries количества символов.

# print(infinite([2, 5, 8], 7)) => 2582582
# print(infinite([], 1000)) => Пустая строка
# print(infinite([7], 4)) => 7777

...

a = [1, 2, 3, 4]

print(a)