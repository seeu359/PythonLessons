from lesson_1 import repetition
from lesson_1 import practice

def test_string_len():
    assert repetition.string_length == 23


def test_add_two_numbers():
    assert repetition.result == 258


def test_string_mul():
    assert repetition.result2 == "I'm string" * 5


def test_string_concatenation():
    assert repetition.result3 == '2 times'


def test_slices():
    assert repetition.tmp_result == 'rst'
    assert repetition.tmp_result2 == 'on'
    assert repetition.result4 == 'rston'


def numbers_from_string():
    assert repetition.numbers_from_string == 16


def lower_string():
    assert repetition.result_string == repetition.upper_string.lower()


def test_abs():
    assert isinstance(practice.value, int)
    assert practice.value == 42


def test_symbols_in_names():

    assert practice.symbols_in_names == 12


def test_interpolation():
    assert practice.arya_hungry == "Do you want to eat ?\nYes, I'm hungry, mom"


def test_yes():
    assert practice.without_yes == 'I say no and another no for your offer'


def test_upper():
    assert practice.string_upper == practice.another_string.upper()