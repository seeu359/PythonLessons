# №1
# Реализуй функцию my_substr(), которая извлекает из строки подстроку
# указанной длины. Она принимает на вход два аргумента (строку и длину) и
# возвращает подстроку, начиная с первого символа:

# Примеры:
# string = 'If I look back I am lost'
# print(my_substr(string, 1))  # => 'I'
# print(my_substr(string, 7))  # => 'If I lo'

...


# №2
# Реализуй функцию reverse_string, которая разворачивает строку

# Примеры:

# reverse_string('Game Of Thrones')  # 'senorhT fO emaG'
# reverse_string('Kirill')  # 'lliriK'


...


# №3
# Реализуй функцию is_contains_char(), которая проверяет, содержит ли строка
# указанную букву, вне зависимости от регистра. Функция принимает два параметра:
#
# Строка
# Буква для поиска
# И возвращает результат проверки – булево значение.

# print(is_contains_char('Hexlet', 'H'))  # => True
# print(is_contains_char('Hexlet', 'h'))  # => True
# print(is_contains_char('Awesomeness', 'd'))  # => False

...


# №4

# Реализуй функцию chars_count(). Она принимает на вход строку и символ и
# считает количество вхождений этого символа в строку. Используй цикл for

# chars_count('hexlet!', 'e')  # 2
# chars_count('hExlet!', 'e')  # 2
# chars_count('hExlet!', 'E')  # 2
#
# chars_count('hexlet!', 'a')  # 0


...


# №5

# Реализуй функцию filter_string(). Она принимает на вход строку и символ и
# возвращает новую строку, в которой удалён переданный символ во всех его
# позициях. Если строка не содержит указанный символ, то она возвращается без
# изменений. Регистр исключаемого символа не имеет значение.

# text = 'If I look forward I win'
# filter_string(text, 'i')  # 'f  look forward  wn'
# filter_string(text, 'O')  # 'If I lk frward I win'


...


# №6
# Создай функцию get_num_dividers(). Функция принимает число.
# С помощью цикла for найти все делители этого
# числа. Найденные делители выводить сразу в столбик без формирования списка.

...