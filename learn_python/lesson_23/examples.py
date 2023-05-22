def iterate(x0, m):
    x = x0
    while True:
        yield x  # вместо print()
        x *= m


# for n in iterate(1, 1.2):
#     print(n)
#     if n > 3:
#         break


def f():
    print('Initializing...')
    yield 'one'
    print('Continue...')
    yield 'two'
    print('Stopping...')

i = f()

b = iter(i)