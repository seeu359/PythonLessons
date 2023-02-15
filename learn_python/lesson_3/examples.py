def pow(number, base=2):
    return number ** base


def some_func(a=None, name=None, length=None):
    return


def truncate(length=3, text='My Text'):
    return length, text


a = truncate(text='Some text', length=12)
b = truncate(text='Another text')


def is_infant(age):
    return age < 1


def first_letter_is_a(string):
    return string[0] == 'a'
