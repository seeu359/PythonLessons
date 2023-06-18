# Example 1

raise ValueError('Age too low!')

# Example 2

l = []
try:
    l[100500] = 42
except IndexError:
    print('Catched!')

# Example 3

try:
    user = users[input('May I have your name? ')]
except Exception:
    sys.exit(1)  # молча завершаем программу
except (KeyError, IndexError):
    print('No users with such name found!')


# Examples 4

f = open('data.txt')
try:
    text = f.read()
    words = len(text.split())
finally:
    f.close()