# Пример 1

# def outer_function(x): # 10
#     def inner_function(y):
#         return x + y # x = 10
#     return inner_function
#
#
# closure = outer_function(10) # ссылка на inner_function
# print(closure(5))


# # Пример 2
# #
# # x = 20
# #
# # def func():
# #     x += 1
# #     return x
# #
# # print(func())
#
#
# # Пример 3
#
# def outer():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print("inner:", a)
#     inner()
#     print("outer:", a)
#
# outer()
#
#
# # Пример 4
#
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

a = '1 2 10 14 16' # => [1, 2, 10, 14, 16]
