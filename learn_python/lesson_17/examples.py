def f(*args, **kwargs):
    return (args, kwargs)


print(f(1, 2, 3, 4, kx='a', ky='b', kz='c'))


def f(x, *args, **kwargs):
    return (x, args, kwargs)


print(f(1, 2, 3, kx='a', ky='b'))


def f(*args, ky=42, **kwargs):
    return (args, ky, kwargs)


print(f(1, 2, 3, 4, kz='c'))

print(f(1, 2, 3, 4, ky='b', kz='c'))