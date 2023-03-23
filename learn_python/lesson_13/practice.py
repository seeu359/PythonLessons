# №1 Цель упражнения — написать функцию collect_indexes(). Эта функция должна:
#
# Принимать на вход коллекцию — некий итератор или итерируемый элемент.
# Возвращать словарь или подобную ему коллекцию. Ключом будет элемент коллекции,
# а значением для ключа — список индексов коллекции, по которым встречается
# этот элемент
from collections import defaultdict


# d = collect_indexes("hello")
# d["h"]  # [0]
# d["e"]  # [1]
# d["l"]  # [2, 3]


# №2 Реализуй функцию get_phone_numbers() используя новые навыки
# В функцию поступает неограниченное количество пар номеров телeфонов в формaте
# (номер, имя) где ключами будут имена, а значениями -
# список номеров телефонов для этого имени. Обратите внимание, что одному имени
# может принадлежать несколько разных номеров. Полученный словарь вывести
# командой:



# №3 Создай функцию get_html_by_url(), которая принимает на вход url -
# адрес сайта.
# Твоя задача реализовать так называемый кеш. Если url уже передавался в
# функцию ранее ты должен вывести на экран строку:
# "Взято из кэша: HTML-страница для адреса <URL-адрес>"
# Если url передается впервые - ты должен вывести на экран строку
# "HTML-страница для адреса <URL-адрес>" и сохранить страницу в кеш.

# get_html_by_url('https://google.com') => HTML-страница для адреса https://google.com
# get_html_by_url('https://ya.ru') => HTML-страница для адреса https://ya.ru
# get_html_by_url('https://examples.ru') => HTML-страница для адреса https://examples.ru
# get_html_by_url('https://google.com') => Взято из кэша: HTML-страница для адреса https://google.com


...



# №4 Реализуй функцию-предикат scrabble, которая принимает на вход два
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


# **№5 Реализуй функцию gen_diff, которая сравнивает два словаря и возвращает
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

...

# gen_diff(
#     {"one": "eon", "two": "two", "four": True},
#     {"two": "own", "zero": 4, "four": True},
# ) #{"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}