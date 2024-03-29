# №1 Query String (строка запроса) — часть URL, содержащая константы и
# их значения.
# Она начинается после вопросительного знака и идет до конца адреса:
# query string: page=5
# https://ru.some-site.io/blog?page=5

# Если параметров несколько, то они отделяются амперсандом &:

# query string: page=5&per=10
# https://ru.some-site.io/blog?per=10&page=5

# Напиши функцию build_query_string, которая принимает на вход словарь с
# параметрами и возвращает строку запроса, сформированную из этих параметров:


# build_query_string({'per': 10, 'page': 1})


...

# №2 ДНК и РНК это последовательности нуклеотидов.
#
# Четыре нуклеотида в ДНК это аденин (A), цитозин (C), гуанин (G) и тимин (T).
#
# Четыре нуклеотида в РНК это аденин (A), цитозин (C), гуанин (G) и урацил (U).
#
# Цепь РНК составляется на основе цепи ДНК последовательной заменой каждого
# нуклеотида:
#
# G -> C
# C -> G
# T -> A
# A -> U

# Напиши функцию to_rna, которая принимает на вход цепь ДНК и возвращает
# соответствующую цепь РНК (совершает транскрипцию РНК).

# to_rna('ACGTGGTCTTAA') # 'UGCACCAGAAUU'


...


# №3 Реализуй функцию-предикат scrabble, которая принимает на вход два
# параметра: набор символов (строку) и слово, и проверяет, можно ли из
# переданного набора составить это слово. В результате вызова функция
# возвращает True или False.
#
# При проверке учитывается количество символов, которые нужны для составления
# слова, и не учитывается их регистр.
#
# Для решения используй встроенный инструмент Counter из модуля collections

# scrabble('rkqodlw', 'world')  # True
# scrabble('avj', 'java')  # False
# scrabble('avjafff', 'java')  # True
# scrabble('', 'hexlet')  # False
# scrabble('scriptingjava', 'JavaScript')  # True


...

# **№4 Реализуй функцию gen_diff, которая сравнивает два словаря и возвращает
# результат сравнения в виде словаря. Ключами результирующего словаря будут
# все ключи из двух входящих, а значением строка с описанием отличий: added,
# deleted, changed или unchanged.
#
# Возможные значения:
#
# added — ключ отсутствовал в первом словаре, но был добавлен во второй
# deleted — ключ был в первом словаре, но отсутствует во втором
# changed — ключ присутствовал и в первом и во втором словаре, но
# значения отличаются
# unchanged — ключ присутствовал и в первом и во втором словаре с
# одинаковыми значениями


# gen_diff(
#     {"one": "eon", "two": "two", "four": True},
#     {"two": "own", "zero": 4, "four": True},
# ) #{"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}
