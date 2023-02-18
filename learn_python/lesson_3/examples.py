def pow(number, base=2):
    return number ** base


def some_func1(a=None, name=None, length=None):
    return


def truncate(param, length=3, text='My Text'):
    return length, text


_a = truncate('param', text='Some text', length=12)
_b = truncate('param1', length=1)


def is_infant(age):
    return age < 1


def first_letter_is_a(string):
    return string[0] == 'a'


def is_even(number):
    return number % 2 == 0
