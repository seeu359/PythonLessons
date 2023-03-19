# №1 Реализуй функцию get_phones_dict, которая принимает себя неограниченное
# количество телефонных номеров и формирует из них словарь. В словаре
# ключом будут являться, коды стран, а значениями непосредственно
# номер телефона. Чтобы не усложнять, представим, что код страны -
# это первая цифра в номере. Значениями в словаре должны быть списки. Если код
# уже есть в словаре, то номер телефона нужно добавлять в список по
# соответствующему ключу.


# get_phone_dict('+79031135525', '+98881234455', '+19234234333',
# '+7903331122233')
# => {'+7': ['+79031135525', +7903331122233], '+9: ['+98881234455],
# '+1': ['19234234333']}


...


# №2 Цель упражнения — функция count_all(). Эта функция должна принимать
# на вход итерируемый источник и возвращать словарь. Ключами этого словаря
# должны стать элементы источника, при этом значения должны отражать
# количество повторов элемента в коллекции-источнике.


# count_all(["cat", "dog", "cat"])  # {"cat": 2, "dog": 1}
# count_all("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# count_all("*" * 20)  # {'*': 20}


...


# №3 Query String (строка запроса) — часть URL, содержащая константы и
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

# №4 ДНК и РНК это последовательности нуклеотидов.
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


# №5 Реализуй функцию gen_diff, которая сравнивает два словаря и возвращает
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
