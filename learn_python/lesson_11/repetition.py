# Тебе нужно реализовать функцию greet(), которая должна принимать несколько
# имён (как минимум одно!) и возвращать строку приветствия (см. примеры ниже).

# greet('Bob')
# # 'Hello, Bob!'
# greet('Moe', 'Mary')
# # 'Hello, Moe and Mary!'
# greet(*'ABC')
# # 'Hello, A and B and C!'

...


# №4 Почти всегда данные, которые поступают в нашу программу с какого-то сайта
# передаются в JSON формате - это практически тот же самый словарь. Реализуй
# функцию get_user_request(), которая принимает словарь с данным запроса,
# а вторым именованным аргументом принимает список допустимых HTTP-методов в
# виде списка. Тебе нужно проверить, есть ли в нашем словаре ключ method.
# Если он есть, проверить, соответствует ли значение ключа method списку
# разрешенных методов. Если ключа нет - возвращать строку "Method is not
# defined". Если метод не допустим - выводить строку "Method {method} is not
# allowed"В противном случае, выводить значение ключа data, который также
# должен быть в словаре.
# Основные HTTP-методы - GET, POST, PUT, PATCH, DELETE


# request = {'method: 'POST', data: 'Some data for request'}
# request2 = {'data': 'Some wrong data', 'headers': 'Some headers'}

# get_user_request(request, methods=('POST', 'PUT',)) => 'Some data for request
# get_user_request(request, methods=('GET',)) => 'Method POST is not allowed
# get_user_request(request2, methods=('DELETE',)) => Method is not defined


def get_user_request(user_request: dict, allows_methods=('POST', 'PUT')):
    if 'method' not in user_request:
        return 'Method is not defined'

    method_value = user_request.get('method')
    if method_value in allows_methods:
        return user_request.get('data')
    return f'Method {method_value} is not allowed'
