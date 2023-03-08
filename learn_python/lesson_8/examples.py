# a = [1]
# b = a
# print(b)

#######

a = []
new_list = []

print(a == new_list)

# ######
#
# a = []
# pair = (a, a)
# pair[0].append(1)
# pair[1].append(2)
# print(pair)
#
#
# ########
#
# some_list1 = ['world', 'hello', 'some_str']
#
# for i in enumerate(some_list1):
#     print(i)
#
#
# # либо так
#
#
# for index, value in enumerate(some_list1):
#     print(index)
#     print(value)


my_list = ['hello', 'hi', '1233', 111]

a = ('hi', 'wef')

n, m = a


def some_func(symbol, iterable_):
    for index, value in enumerate(iterable_):
        if symbol == value:
            return index
    return None


print(some_func('t', 'cal'))
