from itertools import chain

# Пример 1
# Получаем поток четных чисел
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, range(20)))

def dup(x):
    return [x, x]

dup_even_numbers = list(chain(*map(dup, even_numbers)))

# Вариант в виде однострочника:

list(chain(*map(lambda x: [x, x], filter(lambda x: x % 2 == 0, range(20)))))

# Пример 2
# Коды прописных букв из заданной строки
result1= [ord(c) for c in "Hello!!" if c.isalpha() and c.islower()]

# Квадраты чисел
result2= [x*x for x in [1, 2, 3]]
