from collections import defaultdict

_dict = {}

value = 1
_dict.setdefault('key', []).append(value)

_dict.setdefault('key', []).append('hi')


################


def_dict = defaultdict(list)

def_dict['a'].append('hello')

def_dict['a'][0] = 'hi'
