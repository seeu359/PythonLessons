from lesson_1 import repetition


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
