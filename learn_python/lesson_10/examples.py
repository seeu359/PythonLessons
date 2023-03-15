def func_with_args(required_args, *args):
    print(args)
    if len(args) > 0:
        return required_args + args[0]


print(func_with_args(1, 45, 55, 65))


dictionary = {
        "foo": "bar",
        "baz": 42,
        "items": {
            "first_item": "apple",
            "second_item": "orange",
            "third_item": "lemon",
        },
    }


dictionary_key = dictionary['foo']
dictionary_key2 = dictionary['baz']
dictionary_key3 = dictionary['items']
dictionary_key4 = dictionary['items']['first_item']
# dictionary_key5 = dictionary['unknown_item']

print(dictionary.get('bazzzz'))
