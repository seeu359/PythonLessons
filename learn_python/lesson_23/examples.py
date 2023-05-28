def iterate(x0, m):
    x = x0
    while True:
        yield x  # вместо print()
        x *= m


# a = iterate(1, 1.1)
# for _ in range(20):
#     print(next(a))


# def f():
#     print('Initializing...')
#     yield 'one'
#     print('Continue...')
#     yield 'two'
#     print('Stopping...')
#
#
# i = f()
# print(next(i))
# print(next(i))
# print(next(i))


def get_prime_numbers(numbers):