# Example 1
import sys

# raise Exception('Method POST is not allowed')


# Example 2

l = []

# try:
#    1 / 0
# except IndexError:
#     print('Страница временно недоступна, пожалуйста зайдите позже')

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


# Examples 4

f = open('data.txt')
try:
    text = f.read()
    words = len(text.split())
    f.close()
finally:
    f.close()