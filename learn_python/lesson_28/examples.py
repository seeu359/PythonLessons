from learn_python.lesson_28.example2 import example_func

# Example 1
import sys

# raise Exception('Method POST is not allowed')


# Example 2

l = []

# try:
#    1 / 0
# except:
#     print('На ноль делить нельзя')

# Example 3
#
# users = {'Alex': 'Hello'}
#
# try:
#     user = users['Kirill']
# except (KeyError, IndexError):
#     print('No users with such name found!')
# except Exception:
#     print('Возникла какая-то ошибка ')




try:
    f = open('data.txt')
    text = f.read()
    words = len(text.split())
    f.close()
finally:
    print('Hello')
    f.close()

# try:
#     example_func()
# except ValueError:
#     print('Произошла ошибка в логике работы программы')
# except IOError:
#     print('Закончилось место на диске')
# except Exception:
#     print('Произошла какая-то ошибка')
