# #1

# Реализуй функцию print_winters(), которая будет выводить на экран строку
# "Winter is Coming!"

...

# #2
# Реализуй функцию get_my_name_three_times, которая возвращает твое имя 3 раза
# Результат сохрани в переменной result

...


# #3
# В Python есть функция abs(). Создай свою функцию get_abs_sum(num1, num2),
# которая на вход принимает два числовых параметра и, используя функцию abs(),
# выводит на экран модуль суммы двух переменных num1 и num2. Результат сохрани
# в переменной abs_sum

...


# #4
# Реализуй функцию truncate(), которая должна обрезать переданную строку до
# указанного количества символов, добавлять в конце многоточие и возвращать
# получившуюся строку. Результат работы сохрани в переменной truncate_result.
# Подобная логика часто используется на сайтах, чтобы отобразить длинный текст
# в сокращенном виде.

# Пример работы
# truncate('hexlet', 2)  # 'he...'

...

# #5*
# Реализуй функцию get_hidden_card(card_number, stars_count),
# которая принимает на вход номер кредитки (состоящий из 16 цифр) в виде строки
# и возвращает его скрытую версию, которая может использоваться на сайте
# для отображения. Результат сохрани в переменную card_number.

# Если исходная карта имела номер 2034399002125581, то скрытая версия выглядит
# так ****5581. Другими словами, функция заменяет первые 12 символов,
# на звездочки. Количество звездочек определяется вторым параметром. Например:

# get_hidden_card('2034399002121100', 1)  # *1100
# get_hidden_card('1234567812345678', 2)  # **5678
# get_hidden_card('1234567812345678', 3)  # ***5678

...