# Практика 1

# С помощью механизма замыканий создай функцию счетчик, которая от вызова к вызову будет сохранять
# значение этого самого счетчика. Внешняя функция должна принимать в себя стартовое значение счетчика, и шаг,
# который ты будешь прибавлять к счетчику

# Примеры
# c = counter(start=10, step=2)
# c() => 12
# c() => 14
# c() => 16
# c2 = counter(start=0, step=1)
# c2() => 1
# c2() => 2
# c2() => 3


# Практика 2

# Используя замыкания функций, объяви внутреннюю функцию, которая заключает в тег h1 строку s (s - строка, параметр
# внутренней функции).
# Пример добавления тега h1 к строке "Python":
# <h1>Python</h1>


# Практика 3

# Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.


...

# Практика 4
# Представь, что ты реализовываешь функцию, которая вычисляет среднюю цену закрытия биржевого товара за всю историю
# торгов. Каждый день ряд пополняется новой ценой, при вычислении среднего учитываются все прежние цены.
# Твоя задача, создать функцию make_avenger, которая позволяет пополнять список новой цены и после возвращает
# средний результат. Функция должна сохранять в себе результат предыдущих вызовов.
# Пример
# avg = make_avenger()
# avg(10) => 10.0
# avg(11) => 10.5
# avg(12) => 11.0

