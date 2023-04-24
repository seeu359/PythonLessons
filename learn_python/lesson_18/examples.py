# Пример 1

def mul2(number):
    return number * 2


function = mul2

# Пример 2

def filter_str(sequence, function: callable):
    results = []
    for obj in sequence:
        if function(obj):
            results.append(obj)
    return results


def is_string(string):
    return isinstance(string, str)



# Пример 3

def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(times_2(5))
print(times_3(5))


# Пример 4

def repeat(func, n):
    for i in range(n):
        func()

def hello():
    print("Hello, world!")


# repeat(hello, 3)


# Пример 5
_sum = lambda x, y: x + y


# Пример 6

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)

print(list(squares))


