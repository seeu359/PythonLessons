age = 5


def generate():
    return age + 3


result = generate()

#########

age1 = 5


def generate1():
    age1 = 10
    return age1 + 3


result1 = generate1()

#####

_list = [1, 2, 'hello', True]

_list.append('new value')

print(_list)

#####

another_list = [10, 20, 30]

_list.extend(another_list)

print(_list)
