# from learn_python.lesson_6 import utils
from learn_python.lesson_6.utils import util_func


def work_with_import():
    if util_func(2) == 4:
        return True
    return False


def div_mod(a, b):
    quotient = a // b
    modulo = a % b
    return (quotient, modulo)


name_and_age = ('Bob', 42)

name = name_and_age[0]  # 'Bob'
age = name_and_age[1]  # 42

name1, age1 = name_and_age
