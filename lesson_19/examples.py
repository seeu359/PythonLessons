from operator import mul

# Пример 1

numbers = [2, 3, 8, 15, 34, 42]

# Пример 2
def _mul(x):
    return x * 2

print(list(map(_mul, numbers)))


# Пример 3
def is_even(num):
    return num % 2 == 0


filter(is_even, numbers)

print(list(map(mul, "abc", [3, 5, 7])))
