# # Пример 1
#
# def debug_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Вызов функции:", func.__name__)
#         print("Аргументы:", args, kwargs)
#         result = func(*args, **kwargs)
#         print("Результат:", result)
#         return result
#     return wrapper
#
#
# @debug_decorator
# def add_numbers(x, y):
#     return x + y
#
# print(add_numbers(2, 3))



###################


def count_calls(func):
    num_calls = 0
    def wrapper(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"Функция была вызвана {num_calls} раз(а)")
        return func(*args, **kwargs)
    return wrapper


@count_calls
def my_func():
    print("Hello, world!")
