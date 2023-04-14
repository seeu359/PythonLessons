def func1():
    a = func2()
    return a + 1

def func2():
    return 2 + 2

print(func1())

