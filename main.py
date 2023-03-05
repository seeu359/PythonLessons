from utils import is_string

a = ('1', '2', 'hello', '1')


def find_non_str(_tuple):
    index = 0
    for elem in _tuple:
        if is_string(elem) is False:
            return f'Element with index {index} is non str'
        else:
            index = index + 1
    return True


print(find_non_str(a))
