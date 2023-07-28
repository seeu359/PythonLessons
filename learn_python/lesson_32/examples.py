class Validator:
    type: None

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, number):
        if isinstance(number, self.type) is True and self.min_value < number < self.max_value:
            return True
        else:
            return False


class IntegerValidator(Validator):
    type = int

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)



class FloatValidator(Validator):
    type = float

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)



allowed_methods = ('GET', 'POST')

request = {'key': 'value', 'key2': 'value2'}
print(request.get('key3', 'Привет'))
