# № 1 Реализуй функцию get_nested_list(), которая принимает на вход строку - строка является стихотворением вроде:

# Мороз и солнце день чудесный
# Еще ты дремлешь друг прелестный
# Пора красавица проснись

# Твоя сохранить этот стих в виде вложенного списка с разбивкой по строкам и словам. Функция должна возвращать
# вложенный список как в примере ниже:
# [['Мороз', 'и', 'солнце', 'день', 'чудесный'], ['Еще', 'ты', 'дремлешь', 'друг', 'прелестный'],
# ['Пора', 'красавица', 'проснись']]

...


# №2 Реализуй функцию is_have_word, которая принимает на вход 1 аргумент - слово. Твоя функция должна проверять, есть в
# списке MATRIX переданное в функцию слово. Если есть - вернуть True, в противном случае False

MATRIX = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]


...

# №3 Реализуй функцию is_unique_number на вход принимает коллекцию чисел. Причем числа могут быть как строкой,
# так и элементами списка, так и просто набором чисел. Пример:
#  123141414
#  '1231314'
#  [1, 3, '4', 5, '6']
#  Твоя задача вернуть множество уникальных чисел, которые отсортированы в
#  порядке возрастания. Примеры:
#
#  is_unique_number([1, 2, 6, '4', 2, '3']) => {1, 2, 3, 4, 6}
#  is_unique_number('232443981') => {1, 2, 3, 4, 8, 9}


# №4 Реализуй функцию receive_number(), которая на вход принимает случайную
# строку. Функция должна выделить из строки все неповторяющиеся
# цифры (символы от 0 до 9) и вывести на экран в одну строку через пробел
# их в порядке возрастания значений

# Пример:
# receive_number('Python 3.9.11 - best language!') => 1 3 9


# №5 Реализуй функцию validate_user_data(). Функция принимает словарь. В словаре будут храниться данные,
# которые пользователь вводит при регистрации на сайтах. Одно поле - одна пара ключ-значение.
# Наш сайт обязывает пользователя заполнить как минимум 6 полей, три из которых должны быть такими: username, email и
# password, repeat_password.
# 1) Реализуй валидацию веденных данных:
#   Как я и сказал, пользователь должен заполнить как минимум 6 полей(4 обязательных и 2 любых).
#   Три из заполненных полей должны быть: username, email, password, repeat_password
#   Если все обязательные ключи присутствуют, должны выполняться еще 2 условия:
#     Пароль >= 8 символов;
#     password и repeat_password должны быть равны и соответствовать условию выше.
#     В почте есть обязательный символ собачки.

# ВАЖНЫЙ МОМЕНТ: за каждую из проверок должна отвечать отдельная функция. Наша основная функция - validate_user_data() -
# всего лишь абстракция, внутри которой будут вызываться проверки!!

...


# **№6 Реализуй функцию gen_diff, которая сравнивает два словаря и возвращает
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
