some_dict = {}

some_dict['key'] = 'value'
some_dict['another_key'] = 'another value'

# some_dict['new_key'] = 'new_value'
#
# some_dict['key'] = 'what?'


value = some_dict.pop('key')
value2 = some_dict.pop('some_key', None)

#################

cars_color = {'bmw': 'red', 'nissan': 'white', 'mercedes': 'black'}

cars_color2 = {'bmw': 'green', 'lada': 'blue',
               'nissan': 'black', 'kia': 'yellow'}

cars_color.update(cars_color2)


#######

_dict = {'first_key': 1, 'second_key': 2, 'list': [53]}

new_dict = _dict.copy()

new_dict['first_key'] = 'value'
new_dict.get('list').append(25)
print(new_dict)
print(_dict)
